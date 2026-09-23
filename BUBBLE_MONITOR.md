# Bubble and fragility monitor

## Research question

The monitor asks:

> How much of the current AI-equity state resembles a financially stretched and fragile regime, what evidence argues against that conclusion, and which observable changes would make a sharp repricing more or less likely?

It does not ask an AI model for an unsupported yes-or-no opinion.

## Why one score is not enough

"Bubble" can refer to different mechanisms. A company may have an extreme multiple but strong cash generation, or explosive price behavior without financing fragility. The platform therefore preserves dimensions before producing any composite.

## Planned dimensions

### 1. Valuation stretch

- observed valuation relative to a transparent fundamental model;
- peer and historical percentile;
- sensitivity to growth, margin, rate, and terminal assumptions.

### 2. Price explosiveness

- abnormal acceleration and persistence;
- explosive-root tests such as SADF or GSADF after the relevant time-series material is learned;
- distance from slower trend or fundamental anchors.

### 3. Fundamental gap

- price or multiple growth versus revenue, earnings, and cash-flow growth;
- deterioration in estimate delivery or unit economics;
- dependence on distant terminal value.

### 4. Speculation and crowding

- turnover, volatility, concentration, and retail or options proxies where licensed data exists;
- issuance and capital-flow behavior;
- correlated positioning across the AI theme.

### 5. Capital and funding fragility

- leverage, refinancing exposure, dilution, and cash-burn dependence;
- sensitivity to discount rates and credit conditions;
- ecosystem dependence on a small number of funders or customers.

### 6. Narrative-evidence gap

- strength of AI demand and monetization claims versus disclosed evidence;
- specificity, consistency, and changes in management language;
- later TypeSafe/Jev judgments on source-linked text.

### 7. Macro sensitivity

- rates, liquidity, credit spreads, and risk-appetite regimes;
- scenario effects rather than unsupported causal claims.

### 8. Counter-evidence

- durable revenue growth;
- expanding free cash flow;
- defensible market structure;
- falling unit costs;
- valuation compression through earnings rather than price decline;
- evidence that an apparent extreme is justified.

Counter-evidence is a first-class output, not a disclaimer at the bottom.

## Outputs

For every observation date, the mature monitor should return:

- each dimension score and raw contributing measures;
- a composite bubble-intensity range under declared weights;
- the result under plausible alternative weights;
- pro-bubble and anti-bubble evidence;
- current regime and historical analogues;
- trigger map and scenario horizons;
- confidence components and missing evidence;
- source links and calculation versions.

## Intensity, probability, and confidence

These are different quantities:

- **Intensity** describes how strongly current evidence matches a declared bubble profile.
- **Event probability** estimates a defined future event over a defined horizon, such as a 30% drawdown within 12 months. It requires labels and calibration.
- **Confidence** describes the quality and decisiveness of the evidence and model for this output.

The platform must never display intensity as if it were a calibrated crash probability.

## "When can it burst?"

The first answer is a conditional trigger map, not a date. Example trigger families include:

- earnings or cash-flow disappointment;
- capex or financing requirements rising faster than monetization;
- discount-rate or credit-spread shock;
- loss of market leadership or pricing power;
- major customer concentration shock;
- supply constraints easing and reducing scarcity rents;
- regulatory or accounting change;
- crowded positioning unwinding.

Later, after labeled data and calibration exist, the platform may estimate probabilities for explicit 3-, 6-, and 12-month events. It must publish base rates, calibration, and uncertainty.

## Composite design

Weights stay in deterministic, versioned code. Initial weights are hypotheses, not discovered truths. The composite must be tested for:

- sensitivity to each weight;
- stability across periods and universes;
- double-counted correlated inputs;
- behavior when a dimension is missing;
- false positives and counterexamples;
- calibration against explicit future events.

## Research foundations

The planned econometric branch should study the Phillips-Shi-Yu explosive-root framework, historical bubble evidence, and financial-stability transmission channels before implementation:

- [Phillips, Shi, and Yu: Testing for Multiple Bubbles](https://cowles.yale.edu/sites/default/files/2022-08/d1843.pdf)
- [Greenwood, Shleifer, and You: Bubbles for Fama](https://www.nber.org/papers/w23191)
- [Federal Reserve Financial Stability Report](https://www.federalreserve.gov/publications/financial-stability-report.htm)

These sources guide hypotheses. They do not by themselves validate this platform's score.

## Learning-stage path

- **C1W2:** valuation residual only; explicitly not a bubble score.
- **Finish C1:** event definitions, logistic probability, regularization.
- **C2:** nonlinear interactions, diagnostics, trees, and ensembles.
- **C3:** regimes, anomalies, analogues, and paper-allocation experiments.
- **DLS:** time and text representations if justified by baseline comparisons.
- **Live stage:** point-in-time monitoring, calibration, trigger updates, and paper research.
