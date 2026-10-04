#!/usr/bin/env python3
"""Run a Korean prompt robustness evaluation with the OpenAI API.

Example:
    export OPENAI_API_KEY="..."
    python src/run_evaluation.py \
        --input data/pilot_prompts.csv \
        --output results/pilot_raw.jsonl \
        --model YOUR_MODEL_ID
"""

from __future__ import annotations

import argparse
import csv
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="CSV benchmark path")
    parser.add_argument("--output", required=True, help="JSONL output path")
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL"))
    parser.add_argument("--limit", type=int, default=None)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.model:
        raise SystemExit("Provide --model or set OPENAI_MODEL.")

    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set.")

    client = OpenAI()
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(args.input, "r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    if args.limit is not None:
        rows = rows[: args.limit]

    with output_path.open("a", encoding="utf-8") as out:
        for row in rows:
            response = client.responses.create(
                model=args.model,
                input=row["prompt"],
            )

            record = {
                "prompt_id": row["prompt_id"],
                "base_id": row["base_id"],
                "task_category": row["task_category"],
                "variant_type": row["variant_type"],
                "expected_answer": row["expected_answer"],
                "prompt": row["prompt"],
                "requested_model": args.model,
                "returned_model": getattr(response, "model", None),
                "response_id": getattr(response, "id", None),
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "output_text": response.output_text,
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()

            print(f'{row["prompt_id"]}: {response.output_text!r}')


if __name__ == "__main__":
    main()
