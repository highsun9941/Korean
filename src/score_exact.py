#!/usr/bin/env python3
"""Score A/B/C/D pilot outputs and write a scored JSONL file."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ANSWER_RE = re.compile(r"(?<![A-Za-z])[ABCD](?![A-Za-z])", re.IGNORECASE)


def extract_choice(text: str) -> str | None:
    match = ANSWER_RE.search(text or "")
    return match.group(0).upper() if match else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    total = 0
    correct = 0

    with input_path.open("r", encoding="utf-8") as src, output_path.open(
        "w", encoding="utf-8"
    ) as dst:
        for line in src:
            record = json.loads(line)
            predicted = extract_choice(record.get("output_text", ""))
            expected = record["expected_answer"].strip().upper()
            is_correct = predicted == expected

            record["predicted_answer"] = predicted
            record["is_correct"] = is_correct
            record["needs_manual_review"] = predicted is None

            total += 1
            correct += int(is_correct)

            dst.write(json.dumps(record, ensure_ascii=False) + "\n")

    accuracy = (correct / total) if total else 0.0
    print(f"Scored {total} responses")
    print(f"Accuracy: {correct}/{total} = {accuracy:.3f}")


if __name__ == "__main__":
    main()
