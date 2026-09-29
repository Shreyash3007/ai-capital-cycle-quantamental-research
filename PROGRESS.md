# Project progress

Updated: 2026-09-29

## Current position

```text
Mentor Mode: ACTIVE
Course coverage: MLS Course 1 Weeks 1 and 2 completed (learner-reported)
Early later-course concepts: none introduced yet
Next course week: C1W3 not yet confirmed
Active phase: P00 - C1W2 first-principles valuation engine
Active goal: ML-G01
Active teaching task: ML-G01-T02 - Cost and residuals
Open earlier task: ML-G01-T01 - Vectorized prediction
Evidence state: T01 ASSISTED RUN OBSERVED; T01 EXPLANATION AND TRANSFER PENDING; T02 FIRST ERROR RUN OBSERVED
```

## Progress summary

```text
Current task     [--------------------]   0%
Phase P00        [--------------------]   0%
Overall project  [--------------------]   0%
```

The learner's guarded loop and vectorized prediction functions agree on all six named companies. The mentor reran the saved script and observed `Methods agree: True` with predictions `[2.687, 2.376, 2.955, 1.973, 2.004, 2.032]` (the first printed with ordinary floating-point rounding). A changed-input run and intentional four-weight failure were also observed. This was an assisted first pass; independent transfer and explanation remain open, so T01 earns no completed check yet. In T02, the learner's two arrays and AstraCompute error, squared error, and residual ran correctly. The hand explanation and full cost are not yet observed.

The [software engineering path](ENGINEERING_LEARNING_PATH.md) is planned across these phases, from Python file structure through SQL, APIs, frontend work, and system design. It earns no separate completion credit from documentation; each phase will require observed engineering evidence at its own gate.

## Curriculum progress

| Course boundary | Coverage status | Project evidence | Use in project |
|---|---|---|---|
| C1W1 | learner-reported complete | linear regression, cost, and gradient descent not yet demonstrated here | available in T01-T03 |
| C1W2 | learner-reported complete | multiple regression and related methods not yet demonstrated here | current boundary |
| C1W3 | not confirmed | none | may be taught early if needed |
| Course 2 | not confirmed | none | may be taught early if needed |
| Course 3 | not confirmed | none | may be taught early if needed |
| Deep Learning Specialization | future | none | may be taught early if needed |

Coverage means the learner reports completing the course material. Evidence means the learner independently used and explained it in this project. An early concept is listed separately and does not change course coverage.

## Overall phase weights

| Phase | Weight | State | Phase completion | Overall contribution |
|---|---:|---|---:|---:|
| P00 - C1W2 first-principles valuation engine | 10% | active | 0% | 0.0% |
| P01 - Point-in-time finance and data foundation | 12% | planned | 0% | 0.0% |
| P02 - Quantitative market and econometric research | 14% | planned | 0% | 0.0% |
| P03 - Supervised ML signal research | 16% | planned | 0% | 0.0% |
| P04 - AI evidence and deep-learning research | 12% | planned | 0% | 0.0% |
| P05 - Bubble, catalyst, and fragility system | 12% | dependency-gated | 0% | 0.0% |
| P06 - Portfolio construction and signal book | 14% | dependency-gated | 0% | 0.0% |
| P07 - Live paper research and final defense | 10% | dependency-gated | 0% | 0.0% |
| **Total** | **100%** |  |  | **0.0%** |

Overall completion is the sum of each phase weight multiplied by its evidence-backed completion.

## Active phase task weights

| Task | Weight inside P00 | State | Completion | Evidence |
|---|---:|---|---:|---|
| ML-G01-T01 - Loop and vectorized prediction | 15% | open transfer | 0% | [named run; explanation pending](Journey/2026-09-28-ML-G01-T01.md) |
| ML-G01-T02 - Cost function and residual meaning | 15% | in progress | 0% | [first error run](Journey/2026-09-29-ML-G01-T02.md); full cost and explanation open |
| ML-G01-T03 - Gradients and batch gradient descent | 20% | planned | 0% | planned |
| ML-G01-T04 - Feature scaling and convergence | 15% | planned | 0% | planned |
| ML-G01-T05 - Feature engineering and nonlinear terms | 15% | planned | 0% | planned |
| ML-G01-T06 - Quantamental output and independent defense | 20% | planned | 0% | planned |
| **P00 total** | **100%** |  | **0%** |  |

## Active task checks

Each T01 check is worth 20% of the task. Evidence must include the learner's explanation, not only a passing run.

| T01 check | State | Evidence |
|---|---|---|
| Two-row, one-feature shapes and hand predictions | open: dimension-matching explanation pending | [hand predictions and `X` shape](Journey/2026-09-23-ML-G01-T01.md); [remaining shapes](Journey/2026-09-24-ML-G01-T01.md) |
| Learner-written loop on starter data | open: starter result shown in dialogue; explanation and durable run record pending | [current two-feature code](Journey/2026-09-28-ML-G01-T01.md) |
| Vectorized prediction agrees on starter data | open: starter agreement shown in dialogue; comparison meaning pending | [current two-feature code](Journey/2026-09-28-ML-G01-T01.md) |
| Two- and five-feature agreement plus changed input | open: original and changed-input agreement observed; independent explanation pending | [verified runs](Journey/2026-09-28-ML-G01-T01.md) |
| Shape failure and finance meaning explained | open: failure observed and repaired; learner diagnosis and finance meaning pending | [shape-failure run](Journey/2026-09-28-ML-G01-T01.md) |

If T01 reaches 100%, P00 gains 15 percentage points and the overall project gains 1.5 percentage points (`10%` phase weight x `15%` task weight). Other tasks have their own weights and acceptance checks.

## Update rules

- A ready or attempted task remains at 0% until an acceptance check is passed.
- Task completion is the fraction of its named acceptance checks passed; T01 has five equally weighted checks. A later task brief defines its checks before the learner begins.
- Phase completion is the weighted sum of task completion. Overall completion is the weighted sum of phase completion. Display one decimal place overall and whole numbers for task and phase.
- Assisted completion is visible and may require transfer before full task credit.
- Phase completion changes only from task evidence.
- Overall completion is recalculated after every task state change.
- Curriculum status changes only after the learner explicitly confirms completing the next course week. Early concepts are recorded without changing that status.
- `00_CURRENT_CONTEXT.md` is refreshed last so it matches this ledger.

## Next milestone

The frozen arrays and first error have run. Ask for the AstraCompute hand explanation, then complete a shape-checked cost function and named residual table. Continue through a changed target, failure case, and residual plot. Return to T01 for independent transfer and a short defense before closing it; neither task has earned mastery credit yet.
