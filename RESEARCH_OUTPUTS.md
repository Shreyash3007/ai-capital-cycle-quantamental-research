# Research outputs and visualization

## Product definition

The product is a research engine and its evidence, not a dashboard. The primary outputs are versioned data products, tested signals, research reports, model evaluations, and paper-portfolio records.

A user interface may later inspect these artifacts, but it is optional and cannot be used to claim project completion.

## Output stack

### Layer 1: reproducible data artifacts

- universe membership and segment snapshots;
- raw-source manifests;
- normalized point-in-time fundamentals;
- feature tables;
- semantic judgment records;
- event definitions;
- model predictions and uncertainty;
- signal records.

### Layer 2: model evidence

- training and evaluation configuration;
- baseline comparison;
- walk-forward metrics;
- residual and calibration diagnostics;
- feature and ablation analysis;
- parameter and regime sensitivity;
- failure slices and model card.

### Layer 3: investment-research artifacts

- company quantamental dossier;
- value-chain and segment report;
- earnings or catalyst note;
- expectations and valuation scenario table;
- bubble and fragility report;
- promoted and rejected signal memos.

### Layer 4: portfolio-research artifacts

- ranked signal book;
- paper positions and rebalance log;
- exposure and constraint report;
- performance and risk attribution;
- cost and turnover report;
- drawdown review;
- monthly or quarterly postmortem.

## Company dossier contract

Each mature company dossier should contain:

1. business and AI-value-chain role;
2. segment peers and exposure graph;
3. normalized historical fundamentals;
4. AI unit-economics evidence;
5. capital allocation and financing analysis;
6. embedded-expectations valuation;
7. quantitative market state;
8. semantic evidence and source excerpts;
9. promoted signals and confidence vector;
10. catalysts, scenarios, counter-thesis, and falsifiers;
11. data and model limitations;
12. paper-portfolio implication, if any.

## Current C1W2 outputs

ML-G01 must save:

- loop and vectorized prediction comparison;
- cost history by iteration;
- actual versus predicted log valuation plot;
- valuation-stretch residual table and plot;
- learning-rate failure comparison;
- feature-scaling and convergence comparison;
- engineered-feature hypothesis and baseline comparison;
- a short research note stating what the residual does and does not mean.

These are diagnostic research artifacts, not a stock recommendation.

## Visualization standard

Plots exist to test reasoning. Every chart requires:

- a precise question;
- data and observation period;
- units and transformations;
- labeled axes and benchmark where relevant;
- visible missingness or exclusions;
- source and generation version;
- a written interpretation and alternative explanation.

No important conclusion may depend only on color or visual impression.

## Publishing formats

- typed tables: Parquet for serious datasets, CSV for small learning fixtures;
- structured metadata: JSON where an API or model consumes it;
- research writing: Markdown under version control, with PDF export only for final presentation;
- figures: deterministic PNG or vector output with generation metadata;
- experiment state: machine-readable configuration plus a model card;
- paper portfolio: append-only signal, position, transaction, and attribution records.

## Optional inspection tools

A command-line report generator comes before delivery tooling. In P07, a small analyst workbench will read versioned artifacts through a tested API so reviewers can inspect a conclusion, source, counter-thesis, and paper consequence. It must not own research calculations. A generic web dashboard is neither required nor prioritized. See [the engineering path](ENGINEERING_LEARNING_PATH.md).
