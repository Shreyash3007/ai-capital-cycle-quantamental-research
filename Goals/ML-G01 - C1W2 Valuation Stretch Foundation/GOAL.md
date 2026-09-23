---
type: goal
id: ML-G01
status: active
phase: P00
completion: 0
project: AI Capital Cycle Quantamental Research Engine
evidence_status: planned
updated: 2026-09-23
---

# ML-G01: C1W2 valuation-stretch foundation

## Objective

Independently implement, run, visualize, and explain a multiple linear regression model from first principles for a synthetic AI-capital-cycle valuation problem, using C1W1 cost and gradient descent plus the full C1W2 boundary, including multiple features, vectorization, feature scaling, and feature engineering.

## Why this goal exists

This goal turns the current course knowledge into a real finance research primitive. It also strengthens Python through functions, loops, NumPy arrays, shapes, assertions, plotting, and debugging.

## Research statement

Given comparable-scale fundamental ratios for a small synthetic company universe, estimate a log valuation multiple. Define:

```text
valuation_stretch = observed_log_multiple - predicted_log_multiple
```

A positive value means the observation is more expensive than this model predicts. It does not establish mispricing, a bubble, or a future decline.

## Task sequence

| Task | State | Central difficulty |
|---|---|---|
| [ML-G01-T01](T01%20-%20Vectorized%20Prediction.md) | ready | start with two rows and one feature; grow to loop and vectorized five-feature predictions |
| ML-G01-T02 | planned | implement and verify squared-error cost |
| ML-G01-T03 | planned | implement gradients and batch gradient descent |
| ML-G01-T04 | planned | implement feature scaling and explain its effect on convergence |
| ML-G01-T05 | planned | test a financially justified engineered feature and nonlinear term |
| ML-G01-T06 | planned | produce a research output and pass an independent transfer defense |

The complete task path is in [PHASE_00_C1W2_PLAN.md](../../PHASE_00_C1W2_PLAN.md). Detailed briefs for T02-T06 will be finalized from observed work before each task begins.

The tasks are a difficulty ladder, not six large assignments to solve at once. Each begins with a tiny hand example and a learner-written Python run, then adds one source of difficulty at a time. Partial checkpoints can be committed while the goal remains incomplete.

## Required artifacts

- `src/01_vectorized_prediction.py`
- later numbered learner scripts for cost, training, and visualization;
- deterministic outputs under `outputs/`;
- small tests under `tests/`;
- evidence note after the final demonstration.

## Acceptance checks

The goal is complete only when the learner can:

- explain `m`, `n`, `X`, `y`, `w`, `b`, predictions, errors, and their shapes;
- match one vectorized prediction to a hand calculation;
- show loop and vectorized results agree on two inputs;
- implement squared-error cost without a training library;
- derive and implement the gradients for every parameter;
- run batch gradient descent and explain simultaneous parameter updates;
- demonstrate decreasing cost under a suitable learning rate;
- diagnose an unsuitable learning rate from output and plots;
- implement a training-only feature scaler, compare convergence, and explain leakage;
- justify and test an engineered feature against the original baseline;
- save and interpret actual-versus-predicted, cost-history, and residual plots;
- run a fresh transfer fixture without a finished solution;
- explain at least three financial or statistical limitations;
- state why the residual is a research signal rather than bubble proof.

## Tool boundary

Allowed: Python standard library, NumPy, Matplotlib, assertions, and tutor-created tests or fixtures.

The learner implements the model rather than using `scikit-learn` fitting. This goal's acceptance checks target C1W2. A later-course method may be taught as an optional extension under Mentor Mode, but it cannot substitute for the from-scratch C1W2 demonstration. No copied course lab, generated assignment solution, or live endpoint enters this goal.

## Evidence rule

This file describes planned capability. Completion remains `0` until task evidence exists. A successful run after substantial help is recorded as assisted and requires fresh transfer before demonstration.

## Links

- [Phase plan](../../PHASE_00_C1W2_PLAN.md)
- [Mentor Mode](../../MENTOR_MODE.md)
- [Progress ledger](../../PROGRESS.md)
- [Project hub](../../Projects/AI%20Capital%20Cycle%20Quantamental%20Research%20Engine/PROJECT_HUB.md)
