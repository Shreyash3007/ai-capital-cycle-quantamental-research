# Project progress

Updated: 2026-09-24

## Current position

```text
Mentor Mode: ACTIVE
Course coverage: MLS Course 1 Weeks 1 and 2 completed (learner-reported)
Early later-course concepts: none introduced yet
Next course week: C1W3 not yet confirmed
Active phase: P00 - C1W2 first-principles valuation engine
Active goal: ML-G01
Active task: ML-G01-T01 - Vectorized prediction
Task state: READY
Evidence state: PLANNED
```

## Progress summary

```text
Current task     [--------------------]   0%
Phase P00        [--------------------]   0%
Overall project  [--------------------]   0%
```

The documentation system is established, but it does not count as demonstrated research capability. The learner's two starter hand predictions and all three shapes were correct. The dimension-matching explanation and Python implementation are still open, so no T01 check has passed yet.

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
| ML-G01-T01 - Loop and vectorized prediction | 15% | ready | 0% | planned |
| ML-G01-T02 - Cost function and residual meaning | 15% | planned | 0% | planned |
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
| Learner-written loop on starter data | open | none |
| Vectorized prediction agrees on starter data | open | none |
| Two- and five-feature agreement plus changed input | open | none |
| Shape failure and finance meaning explained | open | none |

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

Write and run the first learner-authored Python step for two fictional companies and one feature, and explain why the feature and weight counts match. Then extend to vectorization, two and five features, a changed input, and an incompatible-shape failure. The learner writes every code line.
