# Research Protocol

## Title

**Korean Prompt Robustness: Measuring Sensitivity to Meaning-Preserving Variations in Korean User Input**

## 1. Objective

The objective is to measure how much model performance changes when the *meaning of a task stays the same* but the Korean surface form changes in ways that occur naturally in real use.

The study is designed as a controlled robustness evaluation rather than an attempt to infer model internals.

## 2. Research questions

### RQ1
How much does task accuracy change across meaning-preserving Korean prompt variations?

### RQ2
Which perturbation categories are associated with the largest robustness gaps?

### RQ3
Do robustness effects differ by task category?

### RQ4
Where model access permits, are the same robustness weaknesses observed across different model families?

## 3. Hypotheses

- **H1:** Natural paraphrases will usually produce smaller performance changes than noisy variations.
- **H2:** Typographical errors and non-standard spacing will produce larger robustness gaps than clean paraphrases.
- **H3:** Some tasks will show interaction effects: a perturbation that is harmless for one task category may substantially affect another.
- **H4:** Strong clean-prompt accuracy will not necessarily imply equally strong robustness under ordinary Korean user variation.

These hypotheses are directional expectations, not assumptions that must be confirmed.

## 4. Benchmark construction

### 4.1 Target size

The full benchmark is planned to contain approximately **200–500 base tasks**. The exact final size will depend on pilot quality-control results and available API budget.

### 4.2 Task selection

The first version will prioritize tasks with objectively verifiable answers, including:

- arithmetic reasoning,
- logical reasoning,
- multiple-choice classification,
- instruction following,
- short-form commonsense tasks that can be converted to deterministic labels.

Tasks with highly subjective scoring will be excluded from the primary benchmark.

### 4.3 Prompt variants

Each base task will have a clean standard-Korean version and several variants drawn from the following taxonomy:

1. paraphrase,
2. formality shift,
3. typographical error,
4. spacing variation,
5. word-order variation,
6. conversational/abbreviated phrasing,
7. irrelevant but natural context.

A variant is eligible only if it preserves the intended task and expected answer.

## 5. Pilot phase

A small pilot will be used to test:

- whether the categories are distinct enough to code consistently,
- whether the prompts remain meaning-equivalent,
- whether expected answers are unambiguous,
- whether automated scoring behaves correctly,
- whether API metadata are captured sufficiently for reproducibility.

Pilot items may be revised or removed for ambiguity. Any such changes will be documented before the full-scale run.

## 6. API evaluation procedure

For each included prompt:

1. submit the prompt through the API,
2. record the exact prompt text and metadata,
3. store the raw response separately from the benchmark,
4. compute an automated score where possible,
5. flag uncertain scoring cases for manual review.

The evaluation script requires the model identifier to be specified explicitly rather than hard-coding a particular model. This is intended to keep the protocol usable as model availability changes.

For primary deterministic tasks, low-variance generation settings will be used where supported. A secondary repeated-run analysis may be used to estimate response variability.

## 7. Primary metrics

### Accuracy

`correct responses / total responses`

### Robustness gap

For perturbation type \(p\):

`accuracy(standard) - accuracy(p)`

A positive gap means performance declined relative to the standard prompt.

### Variant consistency

For each base task, measure whether semantically equivalent variants lead to the same scored answer.

### Failure concentration

Estimate what fraction of total errors occur in each perturbation category and task category.

## 8. Statistical analysis

The primary analysis will be descriptive and paired at the base-task level.

Planned analyses include:

- accuracy by perturbation category,
- paired standard-vs-variant comparisons,
- confidence intervals for accuracy and robustness gaps,
- error rates by task category,
- cross-model comparisons where available.

Where sample size permits, bootstrap confidence intervals will be used to avoid relying unnecessarily on strong distributional assumptions.

Exploratory analyses will be clearly labeled as exploratory.

## 9. Quality control

A prompt variant will be excluded if it:

- changes the correct answer,
- introduces material ambiguity,
- adds knowledge not required by the base task,
- accidentally reveals the answer,
- is implausible as natural Korean usage.

See `docs/scoring_and_quality_control.md` for the detailed checklist.

## 10. Reproducibility record

Each experiment should preserve, where available:

- prompt ID,
- base-task ID,
- perturbation category,
- exact prompt text,
- expected answer,
- requested model identifier,
- API response identifier,
- model identifier returned by the API,
- timestamp,
- raw response text,
- automated score,
- manual-review status.

Secrets such as API keys must never be committed.

## 11. Limitations

The study will not establish a universal measure of Korean-language capability. It evaluates a defined set of tasks and perturbations.

Other limitations include:

- difficulty of proving perfect semantic equivalence,
- benchmark sampling choices,
- API/model changes over time,
- automated-scoring errors,
- possible differences between API behavior and other product surfaces.

These limitations will be reported alongside findings.

## 12. Planned dissemination

If the project produces interpretable results, the goal is to release:

- benchmark methodology,
- non-sensitive prompt data that can be shared,
- evaluation code,
- aggregate results,
- documented limitations,
- and a concise report or preprint.

No result will be reported as completed before the corresponding experiment has actually been run.
