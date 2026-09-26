"""Constructed receiver for demonstrating the probe, not a neuroscience model."""

import random


def respond(history, present, probe, seed):
    # Earlier events change which later event shape can move this receiver.
    state = sum((1 if i % 2 == 0 else -1) * v for i, v in enumerate(history)) / len(history)
    shape = probe[2] - probe[3]
    common = probe[1] + probe[4]
    background = 0.2 * sum(history) + 0.1 * sum(present)
    return background + (1 + state) * shape + 0.3 * common + random.Random(seed).gauss(0, 0.02)
