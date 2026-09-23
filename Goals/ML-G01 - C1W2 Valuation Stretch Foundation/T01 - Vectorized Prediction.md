---
type: task
id: ML-G01-T01
goal: ML-G01
status: ready
challenge_level: stretch
evidence_status: planned
updated: 2026-09-23
---

# ML-G01-T01: Vectorized prediction

## Central difficulty

Translate a company-feature table into correct loop and vectorized predictions while keeping the meaning and shape of every value clear.

This task does not implement cost or gradient descent. Those remain separate tasks so the tutor can see whether vectorization itself is understood.

## Before you build

**What:** create two ways to predict a model value for every fictional company, one with loops and one with vectorized NumPy operations.

**Why:** the same calculation must make sense as a finance row, a mathematical dot product, and executing Python code.

**What you get:** a checked prediction table, a hand-verified example, and a clear account of array shapes and one failure mode. This is the base used by the later cost and gradient tasks.

## Working file

`../../Projects/AI Capital Cycle Quantamental Research Engine/src/01_vectorized_prediction.py`

The file is intentionally empty. The learner writes every implementation line.

## Finance setup

Use a small synthetic universe. Each row represents a company observation. Use these five comparable-scale ratio features in this order:

1. revenue growth;
2. gross margin;
3. operating margin;
4. free-cash-flow margin;
5. R&D intensity.

The target used later is a log valuation multiple. This task only predicts from supplied trial weights and a bias.

Use this frozen synthetic fixture. The names do not represent real companies.

| Company | Revenue growth | Gross margin | Operating margin | FCF margin | R&D intensity |
|---|---:|---:|---:|---:|---:|
| AstraCompute | 0.55 | 0.72 | 0.28 | 0.25 | 0.18 |
| NexaCloud | 0.40 | 0.68 | 0.22 | 0.20 | 0.16 |
| VertexChips | 0.65 | 0.75 | 0.35 | 0.32 | 0.21 |
| ModelWorks | 0.30 | 0.62 | 0.12 | 0.08 | 0.25 |
| DataForge | 0.25 | 0.58 | 0.15 | 0.14 | 0.12 |
| CobaltAI | 0.50 | 0.65 | 0.05 | -0.02 | 0.40 |

Use trial parameters `w = [1.2, 0.8, 1.0, 0.9, -0.3]` and `b = 1.0`. These are supplied inputs, not learned parameters. Their economic signs are not a validated valuation claim.

Read [DATA_DICTIONARY.md](../../DATA_DICTIONARY.md) for the feature and shape contracts.

## Calibration before coding

Answer briefly without searching:

1. If `X` has 6 company rows and 5 features, what are the shapes of `X`, `w`, and the prediction vector?
2. In one sentence, what does `np.dot(X, w)` calculate for each row?
3. Why must adding scalar `b` not change the prediction vector's shape?

The answers diagnose readiness; they are not graded as the task itself.

## Learner challenge

Design and write the implementation yourself. It should represent the feature names, companies, matrix, weights, and bias; return predictions from a loop implementation and a vectorized implementation; show the shapes and per-company results; and check agreement within a stated floating-point tolerance. Then change one input and repeat the check.

Choose names that express finance meaning. Avoid shadowing Python built-ins such as `sum` and `list`.

## Required prediction before run

Before executing, write down:

- the expected output shape;
- one hand-calculated row prediction;
- whether the loop and vectorized arrays should match exactly or within floating-point tolerance.

## Required failure experiment

Intentionally create one incompatible weight shape, run it, and read the error. Then restore the correct shape and explain what dimension failed to align.

## Acceptance and task progress

Each passed and explained check contributes 20 percentage points to T01. The mentor records evidence for each check in `PROGRESS.md`. A result that runs but cannot be explained remains open.

1. Shapes and one hand prediction are correct and explained.
2. A learner-written loop implementation returns all predictions.
3. A learner-written vectorized implementation agrees on the original fixture.
4. Both implementations agree after a changed row or weight.
5. The incompatible-shape failure is diagnosed, repaired, and explained; the learner states what the predictions mean and why they are not yet a valuation conclusion.

## Tutor behavior

Start with the calibration and cold attempt. Follow [Mentor Mode](../../MENTOR_MODE.md) for explanation, help, code review, and the solution boundary.

## Completion evidence

Record the exact command, outputs, changed input, shape error, learner explanation, and assistance level. Passing T01 unlocks a detailed T02 cost-function brief.
