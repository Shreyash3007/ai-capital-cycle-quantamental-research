# Learning journey

This is the chronological record of decisions, attempts, evidence, and changes in understanding. It complements the Git history: a commit shows what changed; a session note explains what the learner tried, observed, and understood.

## Timeline

| Date | Event | Learner implementation evidence |
|---|---|---|
| 2026-09-22 | Standalone project created at `D:\ML-project`; initial research charter and course slides organized locally. | None. |
| 2026-09-23 | Project reframed as the AI Capital Cycle Quantamental Research Engine, with a segmented public universe and output-first research standard. | None. |
| 2026-09-23 | Mentor Mode activated; learner reported completing through C1W2, meaning C1W1 and C1W2. P00 tasks and progress weights defined. | None. |
| 2026-09-23 | [Public repository](https://github.com/Shreyash3007/ai-capital-cycle-quantamental-research) created; knowledge graph and Git workflow prepared. | None. |
| 2026-09-23 | [Baseline commit `d9d9db6`](https://github.com/Shreyash3007/ai-capital-cycle-quantamental-research/commit/d9d9db648c842648951a0f5c59c83b23778027e8) published and verified on `main`; the public tree contains docs and an empty learner starter file, but no course PDFs. | None. |
| 2026-09-23 | Mentor pace and P00 difficulty ladder revised: short concept-to-Python steps, beginning with two rows and one feature. | None. |
| 2026-09-23 | [T01 starter checkpoint](Journey/2026-09-23-ML-G01-T01.md): both hand predictions and `X` shape correct; `w`, output shape, and code remain open. | Hand calculation and one shape only. |
| 2026-09-23 | [Software engineering path](ENGINEERING_LEARNING_PATH.md) added across P00-P07: folder roles, Python structure, SQL, APIs, analyst interface, and system design. | Planned; no engineering implementation evidence. |
| 2026-09-24 | Initial navigation-only learner page created, then superseded by the integrated manual below. | Navigation only; T01 evidence unchanged. |
| 2026-09-24 | [Cumulative learning manual](LEARNING_MANUAL.md) added with the full current lesson; its flow and the [knowledge graph](KNOWLEDGE_GRAPH.md) now use rendered PNGs instead of Mermaid code. | Documentation only; T01 evidence unchanged. |
| 2026-09-24 | [T01 shape checkpoint](Journey/2026-09-24-ML-G01-T01.md): `w.shape == (1,)` and prediction shape `(2,)` answered correctly. | Correct shapes; explanation and Python run still open. |
| 2026-09-28 | [T01 first saved Python run](Journey/2026-09-28-ML-G01-T01.md): learner-written loop and vectorized two-feature predictions both returned `[1.76 2.14]`; `np.allclose` returned `True`. | Code execution observed; explanation and transfer checks still open. |
| 2026-09-29 | [T01 nested-loop continuation](Journey/2026-09-28-ML-G01-T01.md): learner generalized the loop over feature columns; saved script reran with matching two-feature outputs. | General loop execution observed; five-feature and explanation checks still open. |
| 2026-09-29 | [T01 one-row five-feature run](Journey/2026-09-28-ML-G01-T01.md): both methods returned `2.687` for AstraCompute; mentor supplied the matching hand arithmetic. | One-row transfer observed; full fixture and explanations remain open. |
| 2026-09-29 | [T01 full six-row run](Journey/2026-09-28-ML-G01-T01.md): loop and vectorized outputs matched on all five-feature company rows. | Full fixture executed; changed-input and explanation checks remain open. |
| 2026-09-29 | [T01 changed-input run](Journey/2026-09-28-ML-G01-T01.md): NexaCloud revenue growth increased by `0.10`; only its prediction rose by `0.120`, with both implementations agreeing. | Sensitivity run observed; independent explanation and shape-failure check remain open. |
| 2026-09-29 | [T01 shape-failure run](Journey/2026-09-28-ML-G01-T01.md): four weights against five feature columns made `np.dot` raise a dimension error; learner restored the script and mentor reran it. | Failure and recovery observed; learner diagnosis remains open. |
| 2026-09-29 | Mentor cadence changed at the learner's request: larger integrated work blocks, one worked different-domain example before every new assignment, and one combined review of code, runs, and explanation. [T01 capstone](LEARNING_MANUAL.md) is now the next block. | Process change only; no new capability credit. |
| 2026-09-29 | Learner clarified that new concepts need exact, line-by-line teaching before independent coding. Mentor Mode now records first-pass code as assisted and requires a later independent variation. The learner has started an incomplete `vector_pred` definition; the [manual](LEARNING_MANUAL.md) teaches its first body line. | Teaching preference updated; no new capability credit. |
| 2026-09-29 | [T01 function teaching pass](Journey/2026-09-28-ML-G01-T01.md): learner typed guarded vectorized and loop functions; both return the original six predictions. The manual now explains why this task precedes cost and gradient descent. | Assisted function run observed; independent transfer pending. |
| 2026-09-29 | [T01 named-output checkpoint](Journey/2026-09-28-ML-G01-T01.md): saved script reran with six company names and `Methods agree: True`; T02 cost and residuals opened for teaching. | Assisted T01 run; T02 has no learner run yet. |
| 2026-09-29 | [T02 first-error checkpoint](Journey/2026-09-29-ML-G01-T02.md): learner's saved arrays both have shape `(6,)`; AstraCompute error, squared error, and residual reran correctly. | Assisted first-row arithmetic; hand explanation and full cost still open. |
| 2026-09-29 | [T02 cost and residual checkpoint](Journey/2026-09-29-ML-G01-T02.md): learner's shape-checked function returned cost `0.017894916666666653`, and all six named residuals printed. | Assisted baseline run; changed-target, failure, plot, and explanation still open. |
| 2026-09-29 | [T02 changed-target checkpoint](Journey/2026-09-29-ML-G01-T02.md): copied target left the baseline intact; CobaltAI residual and total cost both fell. A sign and cost-denominator misunderstanding surfaced. | Changed-target run observed; explanation, guard failure, plot, and transfer open. |

The setup documents were prepared with mentor assistance. They are project planning, not learner-authored model code or proof of mastery.

## Current learning state

- [Progress ledger](PROGRESS.md): T01 0%, T02 0%, P00 0%, overall 0%.
- [Current context](00_CURRENT_CONTEXT.md): T02 teaching active; T01 transfer still open.
- [Learning manual](LEARNING_MANUAL.md): the current integrated lesson and next action.
- [Knowledge graph](KNOWLEDGE_GRAPH.md): current concepts and planned extensions.
- [Session records](Journey/README.md): hand-calculation, shape answers, and first Python run saved.
- [Evidence index](Evidence/README.md): no project implementation evidence yet.

## How a session enters this record

After meaningful work, create a dated note from the [session template](Journey/SESSION_TEMPLATE.md). Link the learner code, command, output, changed input, error experiment, explanation, help level, and next action. If checks pass, create an [evidence record](Evidence/EVIDENCE_TEMPLATE.md), update the concept node and progress ledger, then add a timeline row here. Commit the related files together under [GIT_WORKFLOW.md](GIT_WORKFLOW.md).

Record failed attempts and rejected hypotheses as carefully as successful ones. They show how the research changed.
