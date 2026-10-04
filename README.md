# Korean Prompt Robustness

**A reproducible study of how natural Korean prompt variations affect the accuracy and consistency of language-model responses.**

> **Research area:** Robustness / multilingual model evaluation  
> **Current stage:** Pilot-ready protocol and starter benchmark

This repository turns a simple research question into an inspectable, reproducible study:

> **When two Korean prompts mean the same thing, does a language model behave the same way?**

## Reviewer quick links

- **[One-page project summary](docs/project_summary.md)**
- **[Detailed research protocol](docs/research_protocol.md)**
- **[Scoring & quality-control plan](docs/scoring_and_quality_control.md)**
- **[Starter pilot benchmark](data/pilot_prompts.csv)**
- **[Research roadmap](ROADMAP.md)**
- **[API evaluation script](src/run_evaluation.py)**
- **[Scoring script](src/score_exact.py)**

## Project status

**Pilot-ready / protocol development.**

The research questions, perturbation taxonomy, quality-control rules, starter benchmark, and evaluation code are in place. No empirical results are claimed yet; findings will be added only after the corresponding experiments are actually run.

## Motivation

Real users do not write benchmark-perfect prompts. Korean users naturally vary:

- honorific and informal speech,
- spacing,
- word order,
- abbreviations,
- common typographical errors,
- paraphrases,
- and the amount of irrelevant context included in a request.

These changes may preserve the intended meaning while still changing model behavior. This project studies whether semantically equivalent Korean prompts receive equally accurate and consistent answers.

## Research questions

1. How robust are language models to meaning-preserving variations in Korean prompts?
2. Which types of Korean prompt variation cause the largest changes in task accuracy?
3. Are robustness patterns consistent across task categories and model families?
4. Does performance on clean, standardized Korean prompts accurately predict performance under realistic user input?

## Main hypothesis

Simple paraphrasing will produce relatively small changes in performance, while combinations involving Korean-specific spacing errors, informal phrasing, typographical errors, or unusual word order may produce larger drops in accuracy or consistency.

## Study design

The full benchmark is planned to contain approximately **200–500 base tasks** with objectively verifiable answers. Each base task will be transformed into multiple meaning-preserving variants.

Planned perturbation categories:

| Category | Description |
| --- | --- |
| Standard | Clean, conventional Korean |
| Paraphrase | Same meaning with different wording |
| Formality | Formal ↔ informal speech |
| Typo | Common, natural typographical errors |
| Spacing | Korean spacing variations |
| Word order | Meaning-preserving order changes |
| Conversational | Abbreviated or colloquial phrasing |
| Irrelevant context | Natural but non-essential information |

Initial task categories will emphasize questions that can be scored reliably:

- arithmetic reasoning,
- logical reasoning,
- classification,
- short-form commonsense reasoning,
- instruction following.

## Primary measurements

- **Accuracy** on objectively scored tasks
- **Variant consistency** across prompts that share the same intended meaning
- **Robustness gap**: performance difference between the standard prompt and each perturbation category
- **Failure concentration** by perturbation and task category
- **Cross-model comparison**, where access permits

The core analysis will prioritize simple, auditable metrics before introducing more complex statistical methods.

## Pilot benchmark

The starter benchmark in `data/pilot_prompts.csv` is a **methodological seed dataset**, not a completed benchmark.

It currently demonstrates the intended paired structure:

```
base task
├── standard Korean
├── paraphrase
├── formality shift
├── typo
├── spacing variation
└── word-order variation
```

Every variant should be manually reviewed for meaning preservation before inclusion in the full study.

## Reproducibility

The repository separates benchmark design, raw collection, scoring, and analysis.

```
.
├── README.md
├── ROADMAP.md
├── data/
│   └── pilot_prompts.csv
├── docs/
│   ├── project_summary.md
│   ├── research_protocol.md
│   └── scoring_and_quality_control.md
├── results/
│   └── README.md
├── src/
│   ├── run_evaluation.py
│   ├── score_exact.py
│   └── summarize_results.py
├── .gitignore
└── requirements.txt
```

API keys are read from environment variables and must never be committed. Raw outputs are kept separate from the benchmark so that prompts, responses, and scores can be audited.

## Minimal pilot workflow

After installing the dependency and setting an API key:

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="YOUR_KEY"
```

Run a small sample first:

```bash
python src/run_evaluation.py \
  --input data/pilot_prompts.csv \
  --output results/pilot_raw.jsonl \
  --model YOUR_MODEL_ID \
  --limit 10
```

Score deterministic multiple-choice outputs:

```bash
python src/score_exact.py \
  --input results/pilot_raw.jsonl \
  --output results/pilot_scored.jsonl
```

Summarize accuracy and robustness gaps:

```bash
python src/summarize_results.py \
  --input results/pilot_scored.jsonl
```

Model identifiers are intentionally supplied at run time instead of being hard-coded, so the protocol remains inspectable as available models change.

## Research principles

This project follows four principles:

1. **No fabricated results.** Findings will be reported only after experiments are completed.
2. **Meaning preservation.** Prompt variants should preserve the underlying task and expected answer.
3. **Reproducibility.** Model identifiers, settings, timestamps, prompts, outputs, and scoring rules will be recorded.
4. **Transparent limitations.** Ambiguous examples and methodological changes will be documented rather than silently removed.

## Why Korean?

Korean presents useful robustness questions because natural usage combines flexible word order, frequent subject omission, honorific systems, colloquial contraction, and spacing conventions. A system can therefore appear strong on standardized Korean while behaving differently on ordinary user input.

This project focuses on a practical question: **does a model understand the task robustly, or is its performance overly sensitive to how a Korean user happens to phrase it?**

## Planned outputs

Subject to the results of the pilot and full evaluation, planned outputs include:

- an expanded Korean robustness benchmark,
- prompt-transformation guidelines,
- reproducible evaluation scripts,
- aggregate robustness results,
- error analyses and documented failure cases,
- a concise research report or preprint.

## Researcher note

This is an early-stage independent research project. The repository is intended to make the proposed methodology concrete and reviewable from the beginning. Prior publication history is not being implied; the emphasis is on a clearly scoped question, reproducible execution, and transparent reporting.

## Contact

For project-related questions, please use the GitHub Issues section of this repository.
