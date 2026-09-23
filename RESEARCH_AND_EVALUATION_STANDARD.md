# Research and evaluation standard

## Research discipline

Every model begins with a written claim:

- What is the unit of observation?
- What is known at prediction time?
- What exactly is the target?
- What decision or research question could use the result?
- What simpler baseline could answer it?
- What result would falsify the idea?

Without these answers, a model is an experiment without a defined meaning.

## Baselines

Use at least one baseline before accepting complexity:

- historical or cross-sectional mean;
- last known value;
- simple linear or logistic model;
- equal-weight paper portfolio;
- transparent finance rule.

A complex model that does not beat a relevant simple baseline out of sample has not earned a place in the platform.

## Validation design

- Use chronological splits for market and filing research.
- Prefer rolling or expanding walk-forward evaluation once real time series begin.
- Keep a final untouched period.
- Fit preprocessing only on the training window.
- Report results by regime, company, industry, and liquidity slice.
- Use nested selection or a clearly separated validation process when tuning many choices.

Random row splits are allowed only when the observation structure makes time irrelevant and that assumption is explained.

## Leakage checklist

- future prices in a feature;
- financial statements before their public filing time;
- restated values used as if originally known;
- future universe membership;
- normalization using test data;
- semantic summaries that mention later events;
- labels accidentally included in derived inputs;
- multiple rows from the same event split across train and test.

## Metrics

### Regression

- mean squared error or root mean squared error;
- mean absolute error;
- residual distribution and residuals by slice;
- rank correlation when ranking is the intended use;
- parameter and prediction stability across windows.

### Classification

- precision, recall, and confusion matrix;
- precision-recall area for rare events;
- calibration and Brier score where probabilities matter;
- threshold results tied to decision cost.

### Portfolio research

- return and volatility;
- drawdown and recovery;
- turnover and transaction costs;
- gross and net exposure;
- sector and single-name concentration;
- capacity and liquidity assumptions;
- performance by market regime;
- comparison with equal-weight and simple rules.

Statistical performance and economic performance are reported separately.

## Bubble-model evaluation

Bubble research has no single perfect label. Evaluation must therefore triangulate:

- historical episodes with predeclared definitions;
- forward drawdowns across explicit horizons;
- explosive-root statistics and their false positives;
- cross-sectional valuation reversals;
- expert-labeled evidence cases;
- stability under alternative weights and thresholds;
- counterexamples where high valuation was justified by later fundamentals.

## Semantic evaluation

Before a TypeSafe/Jev feature influences a score:

- define one narrow question;
- create a labeled set from source-linked excerpts;
- lock a rubric with distinct descriptive levels;
- measure agreement, calibration, confidence behavior, and failure slices;
- compare with a deterministic or simple-text baseline where possible;
- version model, rubric, prompt state, and output;
- define low-confidence review behavior.

## Reproducibility record

Every experiment should eventually save:

```text
experiment_id
code_version
data_snapshot_ids
feature_schema_version
target_definition
split_definition
model_specification
random_seed
metrics
artifacts
limitations
decision
```

## Claim language

Use language that matches evidence:

- "associated with," not "caused by," unless causal design supports it;
- "outperformed in this test period," not "will outperform";
- "valuation stretch," not "bubble proof";
- "conditional fragility," not "crash prediction";
- "model confidence," not "certainty."
