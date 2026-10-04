# Results Directory

This directory is reserved for experiment outputs and analysis artifacts.

## Important status note

**No empirical result is currently claimed.**

Raw API response files are excluded from Git by default because they may be large and may contain metadata that should be reviewed before publication.

When results are available, this directory may contain:

- aggregate CSV summaries,
- plots,
- documented error analyses,
- a run manifest containing model IDs and settings,
- anonymized or shareable excerpts of failure cases.

## Reproducibility convention

A published result should be traceable to:

1. a benchmark version,
2. an exact model identifier,
3. the run date,
4. the raw output file,
5. the scoring script version,
6. any documented manual-review decisions.

Pilot findings and full-benchmark findings should be labeled separately.
