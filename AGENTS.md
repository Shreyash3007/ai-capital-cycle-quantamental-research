# ML workspace instructions

This folder is the canonical home of the AI Capital Cycle Quantamental Research Engine. It must remain understandable as a standalone repository.

## Start here

1. Read `HOME.md`, then `00_CURRENT_CONTEXT.md` and `PROGRESS.md`.
2. For any learning, coding, review, or explanation session, follow `MENTOR_MODE.md`; Mentor Mode is active.
3. Read the active goal and task before changing code. Read `PHASE_00_C1W2_PLAN.md` for the current task sequence.
4. For folder structure, SQL, backend, frontend, or system design lessons, follow `ENGINEERING_LEARNING_PATH.md` and teach only the layer needed by the active phase.
5. For a learner session, use `LEARNING_MANUAL.md` as the self-contained learning and doing page. Keep its lessons cumulative, its current step and rendered diagram accurate, and its assignment solutions learner-owned. Refresh `00_CURRENT_CONTEXT.md` last.

`Visuals/*.svg` are editable diagram sources; Markdown embeds their PNG renders. When a diagram changes, run `magick -background white -density 150 Visuals/<name>.svg -resize <width>x<height> Visuals/<name>.png`, inspect the PNG, and commit source and render together. Use rendered images and tables in learner-facing Markdown so the diagrams work without Mermaid support.
4. Use the relevant design document linked from `HOME.md`; keep each rule in its canonical file.

## Learning ownership

- The learner writes, runs, explains, and defends every assignment-code line.
- The mentor owns task design, guidance, execution checks, documentation, fixtures, and progress recording. Follow the help and solution boundary in `MENTOR_MODE.md`.
- Apply the pace and difficulty ladder in `MENTOR_MODE.md`: concept, logic, Python representation, learner-written code, and a visible run. Start small, escalate help after a short stall, and grow difficulty from observed understanding.
- Course coverage and demonstrated project capability are separate states. Use `PROGRESS.md` for task, phase, and overall completion.

## Research boundaries

- The primary products are reproducible datasets, tested signals, model evidence, research reports, and paper-portfolio attribution. A dashboard is optional and never the project outcome.
- Segment companies by economic role in the AI capital cycle; do not pool them merely because they mention AI.
- A valuation residual is a signal, not proof of a bubble.
- Never claim an exact bubble burst date. Report conditional triggers, scenarios, horizons, and uncertainty.
- Preserve point-in-time data and prevent look-ahead, survivorship, revision, and target leakage.
- Deterministic finance calculations, portfolio rules, and risk limits remain in code.
- AI judgments are typed inputs to the system, not unreviewed trading decisions.
- Live means live data and a live paper portfolio by default. Real-money execution requires a separate explicit decision.

## Professional bar

- Every promoted signal needs an economic mechanism, point-in-time lineage, baseline, out-of-sample evidence, sensitivity analysis, and a written failure policy.
- Preserve negative results and rejected hypotheses.
- A conclusion must be traceable from source evidence through transformation, model, evaluation, and paper consequence.
- The learner must be able to defend every implemented step to a hedge-fund, quant, AI-finance, or MFE reviewer.

## Current implementation boundary

The learner reports completing Machine Learning Specialization Course 1 Weeks 1 and 2. C1W1 linear regression, cost, and gradient descent, plus C1W2 multiple features, vectorization, scaling, and feature engineering, are available. Later-course methods may be introduced when the project needs them: explain the prerequisite from first principles, use a bounded task, and check the learner's understanding and implementation. Do not mark a later course week complete until the learner confirms it. NumPy may perform array operations; the learner implements the first model rather than using `scikit-learn` to train it.

## Public record

- The public GitHub repository is the visible learning journey: plans, learner-authored code, session notes, evidence, failed attempts, revisions, and research outputs.
- Follow `GIT_WORKFLOW.md` for reviewed commits and pushes after meaningful milestones. Never fabricate an attempt or claim mastery from documentation alone.
- Keep local course PDFs, credentials, private provider data, and unlicensed material out of Git.
- Follow `KNOWLEDGE_GRAPH.md` when adding or changing a concept, task, evidence record, or output; update all affected links and statuses in the same commit.

## Completion standard

A task is complete only when the checks in `MENTOR_MODE.md` and its task brief pass. Update `PROGRESS.md` from observed evidence, refresh `LEARNING_MANUAL.md` and its current diagram, then refresh `00_CURRENT_CONTEXT.md` last.
