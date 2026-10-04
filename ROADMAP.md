# Research Roadmap

## Phase 1 — Pilot preparation

**Goal:** validate the methodology on a small benchmark.

Tasks:

- [x] Define research questions
- [x] Define Korean perturbation taxonomy
- [x] Create starter pilot prompts
- [x] Create API collection script
- [x] Create deterministic scoring script
- [x] Define quality-control rules
- [ ] Manually review every pilot variant
- [ ] Run first API pilot
- [ ] Audit extraction/scoring errors
- [ ] Revise ambiguous prompts

**Exit criterion:** the pilot can be run end-to-end without undocumented manual changes.

## Phase 2 — Benchmark expansion

**Goal:** grow from the starter set to approximately 200–500 base tasks.

Tasks:

- [ ] Expand arithmetic and logic tasks
- [ ] Add controlled classification tasks
- [ ] Add instruction-following tasks with objective scoring
- [ ] Add carefully validated commonsense tasks
- [ ] Create perturbation variants
- [ ] Review meaning preservation
- [ ] Freeze benchmark version for the primary run

**Exit criterion:** benchmark items have unambiguous expected answers and validated perturbations.

## Phase 3 — Full API evaluation

**Goal:** measure robustness under a documented protocol.

Tasks:

- [ ] Record model IDs and run configuration
- [ ] Run standard and perturbed prompts
- [ ] Preserve raw API responses
- [ ] Score deterministic tasks
- [ ] Flag uncertain cases for manual review
- [ ] Repeat selected conditions where response variability matters

**Exit criterion:** all primary benchmark items have traceable raw outputs and scores.

## Phase 4 — Analysis

**Goal:** quantify where robustness succeeds or fails.

Planned analyses:

- [ ] Accuracy by perturbation
- [ ] Robustness gap vs. standard prompts
- [ ] Variant consistency
- [ ] Failure concentration by task type
- [ ] Cross-model comparisons where available
- [ ] Confidence intervals
- [ ] Qualitative review of notable failures

## Phase 5 — Reporting

**Goal:** communicate useful findings regardless of whether the hypotheses are confirmed.

Planned outputs:

- [ ] Methods report
- [ ] Aggregate tables/figures
- [ ] Documented limitations
- [ ] Reproducibility instructions
- [ ] Public benchmark materials where appropriate
- [ ] Research report or preprint if results justify it

## Change policy

Methodological changes after the pilot will be documented in Git history. Once the primary benchmark is frozen, items will not be removed solely because a model performs poorly on them.
