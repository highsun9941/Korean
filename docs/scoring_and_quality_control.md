# Scoring and Quality-Control Plan

## Purpose

Robustness experiments can become misleading if a "perturbed" prompt accidentally changes the task itself. This document defines the checks used before a prompt is accepted into the benchmark.

## 1. Meaning-preservation checklist

For every variant, ask:

- Does the user still request the same task?
- Is the correct answer unchanged?
- Was any clue added that makes the problem easier?
- Was any essential information removed?
- Did the wording become unnaturally difficult rather than naturally noisy?
- Would an ordinary Korean speaker reasonably interpret the variant as equivalent?

If any answer is uncertain, the item is flagged for review rather than automatically included.

## 2. Perturbation coding

Each prompt receives exactly one primary perturbation label in the core analysis:

- `standard`
- `paraphrase`
- `formality`
- `typo`
- `spacing`
- `word_order`
- `conversational`
- `irrelevant_context`

Multi-perturbation prompts may be explored later but should not be mixed into the primary single-perturbation analysis.

## 3. Scoring strategy

The primary benchmark favors answers that can be scored deterministically.

For the starter dataset, tasks request a single multiple-choice label (A/B/C/D). The scoring script extracts the first valid standalone label and compares it with the expected answer.

For future task types:

- numeric answers: normalize commas, spaces, and simple unit formatting;
- categorical answers: map accepted labels to a canonical form;
- structured outputs: validate against a documented schema;
- subjective free text: exclude from primary automatic scoring unless a validated rubric is available.

## 4. Manual review

Manual review is required when:

- no valid answer can be extracted,
- multiple conflicting labels appear,
- the model refuses or gives an unrelated answer,
- the prompt itself appears ambiguous,
- the expected answer may be incorrect.

Manual review should not silently overwrite the raw response.

## 5. Dataset versioning

Changes to benchmark items should be made through normal Git history. When a prompt changes after pilot testing, the reason should be documented in the commit message or an accompanying issue.

## 6. Preventing result-driven benchmark editing

After the full evaluation begins, benchmark items should not be removed solely because a model fails them.

An item may still be removed for a pre-defined quality reason such as ambiguity or an incorrect expected answer, but the exclusion and reason should be documented.

## 7. Reporting

Reports should separate:

- pilot results,
- confirmatory full-benchmark results,
- exploratory analyses.

Negative, null, and mixed findings are valid outcomes and should be reported rather than filtered out.
