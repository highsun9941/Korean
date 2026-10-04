# Project Summary

## One-sentence description

This project evaluates whether OpenAI language models give equally accurate and consistent answers when Korean users express the same task with natural differences in wording, formality, spacing, typos, word order, and conversational style.

## Why this question matters

A model can score well on carefully written benchmark prompts yet still behave inconsistently for ordinary users. Korean offers a useful test case because normal usage permits substantial variation in formality, omitted subjects, word order, spacing, contraction, and colloquial phrasing.

The practical question is not merely whether a model can answer Korean prompts, but whether it can do so **reliably when the user's intended meaning is stable but the surface form changes**.

## Core research question

> How robust are language models to natural, meaning-preserving variations in Korean prompts?

Secondary questions:

- Which Korean perturbation types cause the largest loss in accuracy?
- Are some task categories more sensitive than others?
- Are robustness patterns shared across different model families?
- Does strong clean-prompt performance overstate real-world reliability?

## Method in brief

1. Build 200–500 base tasks with objectively verifiable answers.
2. Create controlled Korean variants for each base task.
3. Evaluate the variants through the API under documented settings.
4. Preserve prompts, raw responses, metadata, and scores.
5. Compare standard-prompt accuracy with accuracy under each perturbation.
6. Analyze failure cases and report limitations transparently.

## Planned perturbations

- paraphrase,
- formality shift,
- typographical error,
- spacing variation,
- word-order variation,
- conversational abbreviation,
- irrelevant but natural context.

## Main outcomes

The primary outputs will be:

- accuracy by perturbation category,
- robustness gaps relative to standard Korean prompts,
- within-task consistency across equivalent prompts,
- task-category-specific failure patterns,
- cross-model comparisons where access permits.

## Current stage

The project is at the **pilot-ready protocol stage**.

Completed in this repository:

- research questions and hypotheses,
- benchmark taxonomy,
- quality-control rules,
- starter pilot prompts,
- API evaluation code,
- deterministic scoring code,
- reproducibility and reporting plan.

Not yet claimed:

- completed API experiments,
- statistical findings,
- model comparisons,
- publication or peer review.

This distinction is intentional. The repository is meant to make the proposed work inspectable before results are known.
