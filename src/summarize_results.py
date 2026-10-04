#!/usr/bin/env python3
"""Summarize scored robustness results by perturbation category."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Scored JSONL file")
    args = parser.parse_args()

    counts: dict[str, list[int]] = defaultdict(lambda: [0, 0])

    with Path(args.input).open("r", encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            variant = row["variant_type"]
            counts[variant][0] += int(bool(row["is_correct"]))
            counts[variant][1] += 1

    if not counts:
        raise SystemExit("No scored records found.")

    accuracies = {
        variant: correct / total
        for variant, (correct, total) in counts.items()
        if total
    }
    standard = accuracies.get("standard")

    print("variant,correct,total,accuracy,robustness_gap_vs_standard")
    for variant in sorted(counts):
        correct, total = counts[variant]
        accuracy = accuracies[variant]
        gap = ""
        if standard is not None:
            gap = f"{standard - accuracy:.6f}"
        print(f"{variant},{correct},{total},{accuracy:.6f},{gap}")


if __name__ == "__main__":
    main()
