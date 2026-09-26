"""Measure how replayed history changes a receiver's response to controlled probes.

No training, model framework, or third-party packages are required. The receiver
adapter owns reset/replay; each call must start from the same initial condition.
"""

from __future__ import annotations

import argparse
import csv
import html
import importlib.util
import json
import math
from pathlib import Path
from typing import Callable


Receiver = Callable[[list[float], list[float], list[float], int], float | list[float]]


def _vector(response: object) -> list[float]:
    if isinstance(response, (str, bytes, dict)):
        raise ValueError("response must be a scalar or a flat numeric sequence")
    try:
        values = list(response)
    except TypeError:
        values = [response]
    if not values:
        raise ValueError("receiver returned an empty response")
    try:
        result = [float(x) for x in values]
    except (TypeError, ValueError) as exc:
        raise ValueError("response must be a scalar or a flat numeric sequence") from exc
    if not all(math.isfinite(x) for x in result):
        raise ValueError("response contains a non-finite value")
    return result


def _mean(rows: list[list[float]]) -> list[float]:
    return [sum(v[i] for v in rows) / len(rows) for i in range(len(rows[0]))]


def _subtract(a: list[float], b: list[float]) -> list[float]:
    return [x - y for x, y in zip(a, b)]


def _standard_error(rows: list[list[float]]) -> list[float | None]:
    if len(rows) < 2:
        return [None] * len(rows[0])  # One repeat does not estimate variability.
    means = _mean(rows)
    return [math.sqrt(sum((v[i] - means[i]) ** 2 for v in rows) /
                      ((len(rows) - 1) * len(rows))) for i in range(len(means))]


def collect_trials(spec: dict, receiver: Receiver) -> list[dict]:
    """Replay each history with one shared present and paired sham/probe seeds."""
    histories, probes = spec["histories"], spec["probes"]
    seeds = spec.get("seeds", [0])
    baseline, reference = spec["baseline"], spec["reference"]
    if len(histories) < 2 or len(probes) < 2 or baseline not in probes or reference not in histories:
        raise ValueError("need at least two histories, a baseline and a non-baseline probe")
    if not seeds or len(set(seeds)) != len(seeds) or not all(isinstance(s, int) for s in seeds):
        raise ValueError("seeds must be distinct integers")
    present = spec["present"]

    def run(history: str, probe: str, seed: int) -> list[float]:
        # Defensive copies prevent an adapter from changing the spec across calls.
        return _vector(receiver(list(histories[history]), list(present), list(probes[probe]), seed))

    # A stateful adapter can create an apparent history effect just by call order.
    check = run(reference, baseline, seeds[0])
    rows = []
    for history in histories:
        for probe in probes:
            for seed in seeds:
                rows.append({"history": history, "probe": probe, "seed": seed,
                             "response": run(history, probe, seed)})
    if run(reference, baseline, seeds[0]) != check:
        raise ValueError("receiver is not replayable: identical input and seed changed its output")
    return rows


def analyze_trials(trials: list[dict], *, baseline: str, reference: str) -> dict:
    """Paired difference-in-differences removes a history's baseline output."""
    if not trials:
        raise ValueError("trials are empty")
    histories, probes, seeds = [], [], []
    lookup: dict[tuple[str, str, int], list[float]] = {}
    dimension = None
    for row in trials:
        history, probe, seed = row["history"], row["probe"], int(row["seed"])
        if history not in histories:
            histories.append(history)
        if probe not in probes:
            probes.append(probe)
        if seed not in seeds:
            seeds.append(seed)
        key = (history, probe, seed)
        if key in lookup:
            raise ValueError(f"duplicate trial: {key}")
        response = _vector(row["response"])
        if dimension is None:
            dimension = len(response)
        if len(response) != dimension:
            raise ValueError("response dimensions differ")
        lookup[key] = response
    if len(histories) < 2 or len(probes) < 2 or baseline not in probes or reference not in histories:
        raise ValueError("need two histories, a baseline, a reference, and a probe")
    for history in histories:
        for probe in probes:
            for seed in seeds:
                if (history, probe, seed) not in lookup:
                    raise ValueError(f"missing paired trial: {(history, probe, seed)}")

    rows = []
    for history in histories:
        baseline_shifts = [_subtract(lookup[history, baseline, seed],
                                     lookup[reference, baseline, seed]) for seed in seeds]
        for probe in probes:
            deltas = [_subtract(lookup[history, probe, seed],
                                lookup[history, baseline, seed]) for seed in seeds]
            contrasts = [_subtract(delta, _subtract(lookup[reference, probe, seed],
                                                    lookup[reference, baseline, seed]))
                         for seed, delta in zip(seeds, deltas)]
            contrast = _mean(contrasts)
            rows.append({
                "history": history, "probe": probe,
                "response": _mean([lookup[history, probe, seed] for seed in seeds]),
                "baseline_shift": _mean(baseline_shifts),
                "delta": _mean(deltas), "contrast": contrast,
                "contrast_norm": math.sqrt(sum(v * v for v in contrast)),
                "contrast_se": _standard_error(contrasts),
            })
    ranking = sorted(
        ({"probe": probe, "max_contrast_norm": max(
            row["contrast_norm"] for row in rows if row["probe"] == probe and row["history"] != reference)}
         for probe in probes if probe != baseline),
        key=lambda row: (-row["max_contrast_norm"], row["probe"]),
    )
    return {
        "baseline": baseline, "reference": reference, "n_seeds": len(seeds),
        "rows": rows, "ranking": ranking,
        "interpretation": "Contrast = (probe - baseline) after this history minus "
                          "(probe - baseline) after the reference history, paired by seed. "
                          "A nonzero contrast shows a changed response in this setup; "
                          "it does not establish a unique mechanism or consciousness.",
    }


def read_trials_csv(path: str | Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as stream:
        rows = []
        for row in csv.DictReader(stream):
            rows.append({"history": row["history"], "probe": row["probe"],
                         "seed": int(row["seed"]), "response": json.loads(row["response"])})
        return rows


def _format(values: list[float | None]) -> str:
    return ", ".join("—" if x is None else f"{x:+.4g}" for x in values)


def write_report(trials: list[dict], report: dict, out: str | Path) -> None:
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    with (out / "trials.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=("history", "probe", "seed", "response"))
        writer.writeheader()
        for row in trials:
            writer.writerow({**row, "response": json.dumps(row["response"])})
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    cells = []
    for row in report["rows"]:
        if row["probe"] == report["baseline"] or row["history"] == report["reference"]:
            continue
        cells.append("<tr>" + "".join(f"<td>{html.escape(value)}</td>" for value in (
            row["history"], row["probe"], _format(row["baseline_shift"]),
            _format(row["delta"]), _format(row["contrast"]), _format(row["contrast_se"]),
            f'{row["contrast_norm"]:.4g}')) + "</tr>")
    rank = "".join(f"<li>{html.escape(r['probe'])}: {r['max_contrast_norm']:.4g}</li>"
                   for r in report["ranking"])
    page = f"""<!doctype html><html lang="en"><meta charset="utf-8">
<title>Susceptibility probe</title><style>
body{{font:16px system-ui;max-width:1100px;margin:3rem auto;padding:0 1rem;color:#172833}}
table{{border-collapse:collapse;width:100%;overflow:auto;display:block}}th,td{{padding:.65rem;border-bottom:1px solid #cbd5d9;text-align:left}}
th{{background:#e9f3f3}}code{{background:#f2f5f5;padding:.15rem .3rem}}.note{{max-width:75ch;color:#435b60}}
</style><h1>Susceptibility probe</h1>
<p class="note">Same present input; paired seed and sham comparisons. Reference history:
<strong>{html.escape(report['reference'])}</strong>; baseline probe:
<strong>{html.escape(report['baseline'])}</strong>; seeds: {report['n_seeds']}.</p>
<h2>Difference in response</h2><p class="note">Contrast = change caused by a probe after this history,
minus change caused by that probe after the reference. Baseline shift is listed separately.
Standard error is descriptive across paired seeds; one seed cannot estimate it.</p>
<table><thead><tr><th>History</th><th>Probe</th><th>Baseline shift</th><th>Probe effect</th>
<th>Contrast</th><th>Contrast SE</th><th>Contrast norm</th></tr></thead><tbody>{''.join(cells)}</tbody></table>
<h2>Probes ranked by separation</h2><ol>{rank}</ol><p class="note">{html.escape(report['interpretation'])}</p>
</html>"""
    (out / "report.html").write_text(page, encoding="utf-8")


def _load_receiver(path: str | Path) -> Receiver:
    path = Path(path).resolve()
    spec = importlib.util.spec_from_file_location("probe_user_receiver", path)
    if spec is None or spec.loader is None:
        raise ValueError(f"cannot load receiver: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    receiver = getattr(module, "respond", None)
    if not callable(receiver):
        raise ValueError("adapter needs respond(history, present, probe, seed)")
    return receiver


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run", help="intervene on a Python receiver")
    run.add_argument("--spec", type=Path, required=True)
    run.add_argument("--adapter", type=Path, required=True)
    run.add_argument("--out", type=Path, required=True)
    analyze = commands.add_parser("analyze", help="analyze paired experimental CSV measurements")
    analyze.add_argument("--trials", type=Path, required=True)
    analyze.add_argument("--baseline", required=True)
    analyze.add_argument("--reference", required=True)
    analyze.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "run":
            spec = json.loads(args.spec.read_text(encoding="utf-8"))
            trials = collect_trials(spec, _load_receiver(args.adapter))
            report = analyze_trials(trials, baseline=spec["baseline"], reference=spec["reference"])
        else:
            trials = read_trials_csv(args.trials)
            report = analyze_trials(trials, baseline=args.baseline, reference=args.reference)
        write_report(trials, report, args.out)
    except (KeyError, ValueError, OSError, TypeError) as exc:
        parser.error(str(exc))
    print(f"{len(trials)} measurements; open {args.out / 'report.html'}")


if __name__ == "__main__":
    main()
