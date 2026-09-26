"""Checks for causal comparisons, paired replay, and report interchange."""

import json
import subprocess
import sys
import tempfile
import unittest
from array import array
from pathlib import Path

from susceptibility_probe import analyze_trials, collect_trials, read_trials_csv


ROOT = Path(__file__).resolve().parents[1]


class SusceptibilityProbeTests(unittest.TestCase):
    def test_baseline_shift_does_not_masquerade_as_changed_susceptibility(self):
        # A bug that compares raw outputs instead of within-history changes fails here.
        rows = [
            {"history": h, "probe": p, "seed": seed,
             "response": (10 if h == "B" else 0) + (2 if p == "pulse" else 0) + seed / 10}
            for h in ("A", "B") for p in ("none", "pulse") for seed in (0, 1, 2)
        ]
        report = analyze_trials(rows, baseline="none", reference="A")
        row = next(r for r in report["rows"] if r["history"] == "B" and r["probe"] == "pulse")
        self.assertAlmostEqual(row["baseline_shift"][0], 10)
        self.assertAlmostEqual(row["delta"][0], 2)
        self.assertAlmostEqual(row["contrast"][0], 0)
        self.assertAlmostEqual(row["contrast_norm"], 0)

    def test_paired_seeds_cancel_noise_and_rank_discriminating_probe(self):
        # A bug that doesn't pair each probe with its own sham and seed fails here.
        rows = [
            {"history": h, "probe": p, "seed": seed,
             "response": [7 * seed + (3 if h == "B" else 1) * (p == "selective"),
                          -5 * seed + (2 if h == "B" else 0) * (p == "other")]}
            for h in ("A", "B") for p in ("none", "selective", "other")
            for seed in (0, 1, 2, 3)
        ]
        report = analyze_trials(rows, baseline="none", reference="A")
        got = {(r["history"], r["probe"]): r for r in report["rows"]}
        self.assertEqual(got["B", "selective"]["contrast"], [2.0, 0.0])
        self.assertEqual(got["B", "other"]["contrast"], [0.0, 2.0])
        self.assertEqual(got["B", "selective"]["contrast_se"], [0.0, 0.0])
        self.assertEqual({x["probe"] for x in report["ranking"]}, {"selective", "other"})

    def test_missing_pairs_and_duplicate_rows_are_rejected(self):
        # A bug that silently averages unmatched measurements invents a contrast.
        spec = {"histories": {"A": [0], "B": [1]}, "present": [0],
                "probes": {"none": [0], "pulse": [1]}, "seeds": [0, 1],
                "baseline": "none", "reference": "A"}
        rows = collect_trials(spec, lambda history, present, probe, seed: history[0] + probe[0])
        with self.assertRaisesRegex(ValueError, "missing"):
            analyze_trials(rows[:-1], baseline="none", reference="A")
        with self.assertRaisesRegex(ValueError, "duplicate"):
            analyze_trials(rows + [rows[0]], baseline="none", reference="A")

    def test_non_replayable_receiver_is_rejected(self):
        # A receiver that leaks state across calls invalidates the intervention.
        spec = {"histories": {"A": [0], "B": [1]}, "present": [0],
                "probes": {"none": [0], "pulse": [1]}, "seeds": [0],
                "baseline": "none", "reference": "A"}
        count = 0

        def leaky(history, present, probe, seed):
            nonlocal count
            count += 1
            return count

        with self.assertRaisesRegex(ValueError, "replay"):
            collect_trials(spec, leaky)

    def test_numeric_array_output_can_be_analyzed_without_an_array_dependency(self):
        # A receiver returning a vector (including NumPy arrays) must not be treated as a scalar.
        spec = {"histories": {"A": [0], "B": [1]}, "present": [0],
                "probes": {"none": [0], "pulse": [1]}, "seeds": [0, 1],
                "baseline": "none", "reference": "A"}
        rows = collect_trials(
            spec, lambda history, present, probe, seed:
            array("d", [history[0] * probe[0], 2 * probe[0]]),
        )
        report = analyze_trials(rows, baseline="none", reference="A")
        row = next(r for r in report["rows"] if r["history"] == "B" and r["probe"] == "pulse")
        self.assertEqual(row["contrast"], [1.0, 0.0])

    def test_example_cli_and_csv_reanalysis_agree(self):
        # A broken CLI or CSV roundtrip would prevent use with recorded experiments.
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "report"
            result = subprocess.run(
                [sys.executable, str(ROOT / "susceptibility_probe.py"), "run", "--spec",
                 str(ROOT / "examples" / "probe.json"), "--adapter",
                 str(ROOT / "examples" / "receiver.py"), "--out", str(out)],
                cwd=ROOT, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads((out / "report.json").read_text())
            self.assertGreater(report["ranking"][0]["max_contrast_norm"], 0)
            rows = read_trials_csv(out / "trials.csv")
            again = analyze_trials(rows, baseline="none", reference="alternating")
            self.assertEqual(again["rows"], report["rows"])
            self.assertIn("Difference in response", (out / "report.html").read_text())


if __name__ == "__main__":
    unittest.main()
