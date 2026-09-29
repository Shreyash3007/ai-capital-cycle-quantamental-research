---
type: task
id: ML-G01-T02
goal: ML-G01
status: in-progress
evidence_status: assisted-first-error-run
updated: 2026-09-29
---

# ML-G01-T02: Cost and residuals

## Purpose

Given the six frozen T01 predictions and six synthetic target log multiples, calculate each error and the C1W1 squared-error cost. A residual is observed minus predicted; it is a descriptive model gap, not proof of mispricing or a bubble.

## Teaching boundary

T01's clean named-output script runs, but its independent transfer and defense remain open. T02 may be taught now for pace. The mentor first works an unrelated two-observation example, then gives exact first-pass lines for a new concept and lets the learner type and run them. Mark the first pass assisted; later require an independent changed-target case.

## Frozen teaching inputs

The prediction values come from the T01 baseline in company order. They are supplied here to isolate the cost calculation before teaching cross-file imports.

| Company | Predicted log multiple | Synthetic observed log multiple |
|---|---:|---:|
| AstraCompute | 2.687 | 2.800 |
| NexaCloud | 2.376 | 2.200 |
| VertexChips | 2.955 | 3.100 |
| ModelWorks | 1.973 | 1.900 |
| DataForge | 2.004 | 2.100 |
| CobaltAI | 2.032 | 2.400 |

The target values are invented teaching data, not market observations. Preserve the row order and check that targets and predictions both have shape `(6,)`.

## Model and finance meaning

```text
prediction error = predicted - observed
valuation residual = observed - predicted
J(w,b) = sum((predicted - observed)^2) / (2m)
```

Here `m` is the number of company rows. Squaring removes sign and penalizes larger misses; dividing by `2m` gives the course's cost convention. The residual keeps its sign: a positive value says the synthetic observed valuation is above the trial model estimate. With arbitrary trial weights and six synthetic rows, neither cost nor residual is an investable conclusion.

## Learner work block

Use the empty `../../Projects/AI Capital Cycle Quantamental Research Engine/src/02_cost_and_residuals.py`. The learner types all code.

1. Enter the frozen prediction and target arrays. Print their shapes and one hand-checked error, squared error, and residual.
2. Write a function that checks equal one-dimensional lengths and returns the C1W1 cost without a training library. Print the cost and explain its units and what lowering it would mean on this fixture.
3. Print a named residual table using `observed - predicted`. Change one target, predict the direction of its residual change, rerun, then restore the frozen target.
4. Make a small residual plot with a zero line and company names, visibly labeled as synthetic. Save it under `outputs/`. The mentor teaches plotting syntax on an unrelated example before the learner writes this part.

## Acceptance evidence

- The hand calculation, array shapes, and cost formula agree.
- The learner-written function runs on original and changed-target cases, including a length mismatch failure.
- The residual sign, cost meaning, and limitation are explained in the learner's words.
- The saved plot is inspected and traceable to the executed code and frozen inputs.
- Assistance and a later independent transfer case are recorded before closing T02.

## Current checkpoint

Both frozen arrays and the first-row error, squared error, and residual were typed by the learner and rerun by the mentor. This was an assisted first pass; the learner's hand explanation, full cost, changed-target case, failure case, plot, and independent transfer remain open. See [the session record](../../Journey/2026-09-29-ML-G01-T02.md).
