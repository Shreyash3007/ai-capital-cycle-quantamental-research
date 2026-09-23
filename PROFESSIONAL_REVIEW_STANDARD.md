# Professional review standard

## Purpose

The project should withstand rigorous questioning from four audiences. It does not need to impress them through breadth or visual polish. It must demonstrate technical depth, financial judgment, intellectual honesty, and independent execution.

## Hedge-fund analyst review

A strong reviewer should be able to ask:

- What is the variant perception?
- What is the market already pricing?
- Which operating metrics lead the thesis?
- What are the catalysts and their likely timing ranges?
- What would falsify the thesis?
- What is the downside path, not just the upside case?
- How do accounting quality, cash conversion, dilution, and capital needs affect value?
- Why is this company different from its segment peers?
- How would the view translate into risk-aware exposure?

The project must answer with sources, calculations, scenarios, and counter-evidence rather than generated prose alone.

## Quant-research review

A reviewer should be able to inspect:

- hypothesis formation before backtest selection;
- point-in-time data and universe construction;
- target and horizon definitions;
- baselines and ablations;
- time-aware validation;
- leakage and survivorship controls;
- multiple-hypothesis risk;
- parameter, window, and regime sensitivity;
- factor exposures and neutralization choices;
- costs, turnover, liquidity, and capacity;
- reproducibility from snapshot to result;
- negative and rejected experiments.

A high Sharpe ratio without this evidence is not a credible result.

## AI-finance engineering review

A reviewer should see:

- deterministic finance calculations separated from AI judgments;
- typed schemas and versioned evidence;
- labeled evaluation sets for semantic models;
- calibration, confidence, and abstention behavior;
- prompt, rubric, model, and data versioning;
- drift, latency, cost, and failure monitoring;
- protections against unsupported generated claims;
- human review at high-stakes boundaries.

AI integration must improve a measured research capability, not merely add a chat interface.

## MFE admissions review

The project should provide visible evidence of:

- linear algebra through vectorized models and matrix reasoning;
- calculus and optimization through gradients and convergence;
- probability and statistics through estimation, uncertainty, testing, and calibration;
- numerical reasoning through stability, scaling, and approximation;
- econometric thinking through panels, events, regimes, and point-in-time design;
- programming through clear Python, tests, data structures, and reproducibility;
- finance through accounting, valuation, markets, portfolio construction, and risk;
- research communication through concise, falsifiable reports.

The learner must be able to defend the work orally and reproduce central components without a generated solution.

The complete cross-disciplinary capability matrix is defined in [KNOWLEDGE_DEPTH_STANDARD.md](KNOWLEDGE_DEPTH_STANDARD.md).

## Evidence portfolio

The final body of work should contain:

1. learner-authored implementation history;
2. data dictionary and lineage records;
3. from-scratch core algorithms;
4. baseline and advanced model comparisons;
5. walk-forward evaluation and sensitivity analysis;
6. semantic AI evaluation report;
7. company and segment research dossiers;
8. event-study research;
9. bubble and fragility research with counterexamples;
10. paper-portfolio attribution and postmortems;
11. rejected hypotheses and lessons;
12. a reproducible final research paper or technical report.

## Disqualifying patterns

- a polished dashboard with weak research underneath;
- one notebook that cannot be reproduced;
- random train-test splits on time-dependent data;
- data revised after the supposed prediction date;
- hidden universe selection or survivorship bias;
- a complicated model without a simple baseline;
- unreported tuning and multiple testing;
- LLM summaries treated as ground truth;
- confidence presented as certainty;
- a backtest without costs, exposure, or drawdown analysis;
- exact bubble-burst dates;
- no record of failed ideas;
- code the learner cannot explain.

## Completion test

The project reaches professional portfolio status when an independent reviewer can trace a published conclusion from source evidence through transformations, model, evaluation, signal, and paper-portfolio consequence, and the learner can explain each link and its limitations without relying on hidden generated work.
