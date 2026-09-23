# Knowledge depth standard

## Purpose

The project is designed to build and demonstrate connected expertise across finance, quantitative methods, machine learning, deep learning, applied AI, and research engineering. Depth means the learner can derive, implement, test, interpret, and defend a method in its financial context.

Using a library or naming a concept is not evidence of depth.

## Pillar 1: financial statements and accounting

### Knowledge

- income statement, balance sheet, and cash-flow statement links;
- revenue recognition, deferred revenue, backlog, and remaining obligations;
- gross margin, operating leverage, and contribution economics;
- capex, depreciation, leases, working capital, and free cash flow;
- stock compensation, dilution, debt, interest, and refinancing;
- segment reporting, non-GAAP adjustments, and accounting comparability;
- filing dates, amendments, restatements, and point-in-time availability.

### Project application

- normalize company-quarter fundamentals;
- reconcile calculated metrics to filings;
- identify accounting distortions in AI infrastructure and software;
- distinguish reported, calculated, estimated, and imputed values.

### Proof

An independent reviewer can choose a company-quarter and trace every major feature to a filing and formula.

## Pillar 2: corporate finance, valuation, and capital cycles

### Knowledge

- cost of capital and discount-rate sensitivity;
- enterprise value, equity value, and capital structure;
- revenue, EBITDA, earnings, and cash-flow multiples;
- discounted cash flow and reverse DCF;
- scenario, sensitivity, and terminal-value analysis;
- return on invested capital and incremental returns;
- competitive advantage, industry structure, and capital-cycle behavior;
- financing, dilution, liquidity, and bankruptcy risk.

### Project application

- estimate embedded operating expectations;
- compare valuation within coherent segments;
- measure AI capital efficiency;
- connect supplier revenue to customer capex and financing;
- build explicit bull, base, bear, and falsification cases.

### Proof

The learner can explain which assumptions drive valuation, why the denominator is valid, and what evidence would invalidate the thesis.

## Pillar 3: mathematics, statistics, and econometrics

### Knowledge

- vectors, matrices, projections, eigen concepts, and numerical linear algebra;
- derivatives, gradients, optimization, convexity, and learning rates;
- probability distributions, conditional expectation, variance, covariance, and Bayes reasoning;
- estimation, sampling error, confidence intervals, hypothesis tests, and power;
- regression assumptions, regularization, multicollinearity, heteroskedasticity, and residual analysis;
- time-series dependence, stationarity, autocorrelation, and structural change;
- panel data, fixed effects, event studies, factor models, and causal limitations;
- multiple testing, selection bias, and false discovery.

### Project application

- implement core algorithms from first principles;
- construct point-in-time panel and event tests;
- distinguish statistical significance from economic usefulness;
- quantify uncertainty and model instability;
- test whether results survive alternative specifications.

### Proof

The learner can derive the core equations, implement them, diagnose violated assumptions, and explain why the evaluation design matches the data-generating process.

## Pillar 4: machine-learning fundamentals

### Knowledge

- supervised versus unsupervised objectives;
- loss functions, optimization, regularization, bias, and variance;
- feature construction, scaling, leakage, and missingness;
- linear and logistic models;
- trees, ensembles, clustering, anomaly detection, and recommendation;
- train, validation, test, cross-validation, and walk-forward design;
- discrimination, ranking, calibration, and decision thresholds;
- interpretability, ablation, drift, and failure slices.

### Project application

- valuation and expectation models;
- event-probability models;
- regime and anomaly research;
- cross-sectional ranking;
- semantic feature validation;
- model comparison against financial baselines.

### Proof

The learner can build a baseline, justify complexity, reproduce evaluation, and explain why a model succeeds or fails in different periods and segments.

## Pillar 5: deep-learning fundamentals

### Knowledge

- forward propagation, backpropagation, initialization, normalization, and optimization;
- representation learning and embeddings;
- sequence modeling, attention, and transformers;
- overfitting, transfer learning, and distribution shift;
- architecture selection, computational cost, and ablation;
- probabilistic outputs and calibration limits.

### Project application

- filing and earnings-call representations;
- sequence or temporal models where justified;
- cross-document change detection;
- multimodal evidence only if reliable data becomes available;
- comparisons with simpler text and time-series baselines.

### Proof

A deep model enters the system only when it solves a documented limitation, improves valid out-of-sample evidence, and survives an ablation against a simpler method.

## Pillar 6: applied AI systems

### Knowledge

- structured extraction and typed outputs;
- embeddings, retrieval, context construction, and source attribution;
- TypeSafe/Jev Choice, Score, Noul, probabilities, and confidence;
- language-model evaluation, hallucination, prompt sensitivity, and abstention;
- labeled-set construction, rubric design, calibration, and human review;
- model, prompt, state, and evidence versioning;
- latency, cost, privacy, security, and drift.

### Project application

- extract claims from filings and calls;
- judge one semantic dimension at a time;
- compare current language with earlier disclosures;
- produce constrained explanations from structured evidence;
- route weak or uncertain outputs to human review.

### Proof

The system can show a labeled evaluation report, known failure cases, full probabilities, evidence links, and a deterministic rule for how semantic outputs may influence research.

## Pillar 7: portfolio mathematics and risk

### Knowledge

- returns, compounding, volatility, covariance, correlation, and beta;
- factor exposure and residual return;
- diversification, concentration, and marginal risk;
- portfolio optimization assumptions and instability;
- drawdown, tail risk, stress tests, and scenario loss;
- turnover, transaction costs, slippage, liquidity, and capacity;
- long-short mechanics and borrow constraints.

### Project application

- factor-aware signal evaluation;
- constrained paper portfolios;
- performance and risk attribution;
- scenario and drawdown analysis;
- signal decay and capacity limits.

### Proof

Paper results remain credible after costs, exposure attribution, alternative construction rules, and adverse-period analysis.

## Pillar 8: research and software engineering

### Knowledge

- Python, NumPy, pandas or equivalent tabular tools, testing, typing, and packaging;
- immutable data snapshots and schema validation;
- experiment tracking and deterministic builds;
- modular architecture and dependency boundaries;
- Git history, code review, documentation, and reproducible commands;
- monitoring, failure recovery, and audit trails.

### Project application

- rebuild a result from source snapshot to report;
- separate data, features, models, signals, and presentation;
- preserve learner-authored code and assistance history;
- operate scheduled live paper research safely.

### Proof

A reviewer can clone the repository, follow documented commands, reproduce a declared result, and inspect the exact code and data versions used.

## Depth progression

Each capability moves through five evidence levels:

1. **Explain:** state the concept, assumptions, and finance meaning.
2. **Derive:** work through the relevant mathematics or accounting logic.
3. **Implement:** write the core behavior by hand where pedagogically appropriate.
4. **Evaluate:** test original, changed, failure, and out-of-sample cases.
5. **Defend:** answer professional objections, alternatives, and limitations.

The project claims depth only at the highest level supported by saved evidence.
