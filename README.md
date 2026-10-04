# Korean Prompt Robustness

**A reproducible study of how natural Korean prompt variations affect the accuracy and consistency of language-model responses.**

## Project status

**Pilot-ready / protocol development.**  
This repository contains the research protocol, a small starter benchmark, and reproducible evaluation scripts. No empirical results are claimed yet; results will be added only after experiments are run.

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
- **Pairwise consistency** across variants of the same base prompt
- **Robustness gap**: performance difference between the standard prompt and each perturbation category
- **Failure concentration** by perturbation and task category
- **Cross-model comparison**, where access permits

The core analysis will prioritize simple, auditable metrics before introducing more complex statistical methods.

## Pilot plan

The pilot is intentionally small and serves three purposes:

1. validate the transformation taxonomy,
2. validate automated collection and scoring,
3. identify ambiguous tasks before scaling.

The starter benchmark in `data/pilot_prompts.csv` is a **methodological seed dataset**, not a completed benchmark. Each prompt should be manually reviewed before inclusion in the full study.

## Reproducibility

The repository is designed so that a reviewer can inspect the protocol independently of the eventual results.

```
.
├── README.md
├── data/
│   └── pilot_prompts.csv
├── docs/
│   ├── research_protocol.md
│   └── scoring_and_quality_control.md
├── src/
│   ├── run_evaluation.py
│   └── score_exact.py
├── .gitignore
└── requirements.txt
```

API keys are read from environment variables and must never be committed to the repository. Raw model outputs will be stored separately from the benchmark so that prompts, responses, and scores can be audited.

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
