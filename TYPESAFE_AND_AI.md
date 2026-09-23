# TypeSafe, Jev, and AI integration

## Division of labor

The platform uses different tools for different kinds of work:

| Work | Owner |
|---|---|
| accounting formulas, returns, valuation, weights, thresholds, and risk rules | deterministic Python code |
| regression, classification, clustering, anomaly, and forecasting models | evaluated ML models |
| narrow semantic judgments over source-linked text | TypeSafe System One / Jev |
| readable synthesis of already-recorded evidence | a generative language model |
| high-stakes interpretation and final research judgment | human review |

No model receives authority merely because it is called AI.

## What Jev is for

According to the current [TypeSafe System One documentation](https://docs.typesafe.ai/concepts/system-one), Jev accepts text and returns typed answers and probabilities rather than generated explanations. The useful primitives include:

- **Choice:** select among unordered defined options;
- **Score:** place evidence on an ordered descriptive scale;
- **Noul:** return a probability-like true/false judgment.

Jev is therefore a candidate semantic-feature engine, not the writer of the final research report and not the calculator of finance metrics.

## Candidate semantic features

Each question must measure one dimension only. Possible later questions include:

- How specific is disclosed evidence of AI revenue monetization?
- How strongly does management language depend on future rather than realized demand?
- Is a stated capacity constraint supported by concrete disclosed facts?
- How material is customer concentration in the supplied excerpt?
- Does this filing passage strengthen, weaken, or leave unchanged a defined thesis?

The state supplied to Jev should contain the exact excerpt, document identity, filing date, company, and necessary local context. It should not contain later information when scoring a historical date.

## Confidence rule

TypeSafe documents `confidence` for Choice and Score as a summary of how concentrated the returned probability distribution is. It is not proof that the answer is correct. See [Confidence](https://docs.typesafe.ai/confidence) and [Score](https://docs.typesafe.ai/primitives/score).

The platform therefore stores:

- full probabilities;
- returned confidence where available;
- model and rubric version;
- labeled-set performance;
- evidence coverage and source quality;
- review status.

Low semantic confidence routes to review or exclusion. Thresholds are chosen from target-data evaluation and decision risk, not copied from an example.

## Composite rule

Complex judgments are split into narrow questions. Scores are normalized when their scales differ, then combined using visible weights in deterministic code. This follows the documented [composite scoring pattern](https://docs.typesafe.ai/patterns/composite-scoring), but the platform's questions, weights, and thresholds still require its own validation.

## Generative explanation layer

A later language-model call may receive a structured research state containing:

- numeric outputs and their units;
- source-linked evidence excerpts;
- pro and counter-evidence;
- confidence components;
- approved scenario language;
- missing-data warnings.

It may explain and compare. It may not calculate hidden metrics, add unsupported claims, remove counter-evidence, or turn a scenario into a forecast. The generated output must be traceable back to the structured state.

## Evaluation before use

1. Write a narrow question and rubric.
2. Create a source-linked labeled set with difficult counterexamples.
3. Run a deterministic or simple baseline where meaningful.
4. Measure correctness, calibration, confidence behavior, and slices.
5. Revise the rubric before changing downstream weights.
6. Freeze a version and store outputs.
7. Allow the feature into research only after its failure policy is defined.

## Integration timing

- **Now:** document the interface and evaluation contract only.
- **After numeric baselines and text handling:** build an offline labeled semantic experiment.
- **After satisfactory evaluation:** add Jev as one versioned feature provider.
- **After structured reports are stable:** add generated explanation.
- **Live:** monitor drift, costs, latency, failures, and confidence; never place real orders.

## Security

API credentials stay in environment variables or an approved secret store. They must never appear in prompts, committed source, datasets, logs, screenshots, or saved research artifacts.
