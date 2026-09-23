# Knowledge graph

## Purpose

This is the map from course knowledge to code, research outputs, and proof. The graph is complete for the **planned project structure**; a future concept has a planned node until the learner studies or demonstrates it. The graph does not claim that a linked topic is mastered.

Open [Knowledge/INDEX.md](Knowledge/INDEX.md) for the current concept nodes. Open [PROGRESS.md](PROGRESS.md) for task, phase, and overall completion. Open [JOURNEY.md](JOURNEY.md) for the chronological record.

## Relationship types

| Edge | Meaning |
|---|---|
| `requires` | The first node needs the second idea or artifact. |
| `practised_in` | A concept is used in a learner task. |
| `produces` | A task or phase creates an output. |
| `evidenced_by` | A claim is supported by an observed run, explanation, or review. |
| `extends_to` | A current capability becomes a later research capability. |

## Current concept chain

```mermaid
flowchart LR
  W1[Course 1 Week 1 covered]
  W2[Course 1 Week 2 covered]
  LR[Linear regression]
  CF[Cost function]
  GD[Gradient descent]
  MF[Multiple features]
  V[Vectorization]
  SC[Feature scaling]
  FE[Feature engineering]
  T01[T01 prediction]
  T02[T02 cost]
  T03[T03 training]
  T04[T04 scaling]
  T05[T05 engineering]
  T06[T06 research defense]
  VS[Valuation stretch]
  W1 --> LR --> CF --> GD
  W2 --> MF --> V --> SC --> FE
  MF --> T01
  V --> T01
  CF --> T02
  GD --> T03
  SC --> T04
  FE --> T05
  T01 --> T02 --> T03 --> T04 --> T05 --> T06
  T06 --> VS
```

Course completion in this diagram is learner-reported coverage. Every current task remains at 0% until its checks pass.

## Research chain

| Starting node | Edge | Destination | Current state |
|---|---|---|---|
| [C1W1-C1W2 concept set](Knowledge/INDEX.md) | `practised_in` | [P00 goal](Goals/ML-G01%20-%20C1W2%20Valuation%20Stretch%20Foundation/GOAL.md) | ready, no implementation evidence |
| [Project structure](Knowledge/K009_Project_Structure.md) | `practised_in` | [P00 scripts and checks](PHASE_00_C1W2_PLAN.md) | planned, no structure explanation observed |
| [Engineering path](ENGINEERING_LEARNING_PATH.md) | `extends_to` | [P01 SQL and P07 analyst workbench](ROADMAP.md) | planned, no full-stack evidence |
| [P00 goal](Goals/ML-G01%20-%20C1W2%20Valuation%20Stretch%20Foundation/GOAL.md) | `produces` | [valuation-stretch research output](RESEARCH_OUTPUTS.md) | planned |
| [Valuation stretch](Knowledge/K008_Valuation_Stretch.md) | `extends_to` | [expectations gap and bubble dimensions](BUBBLE_MONITOR.md) | planned |
| [Finance model](FINANCE_RESEARCH_MODEL.md) | `requires` | [point-in-time data](DATA_AND_LIVE_SYSTEM.md) | planned |
| [Point-in-time data](DATA_AND_LIVE_SYSTEM.md) | `produces` | [versioned research signals](SIGNAL_RESEARCH_PROGRAM.md) | planned |
| [AI evidence](TYPESAFE_AND_AI.md) | `extends_to` | [narrative-evidence gap](BUBBLE_MONITOR.md) | planned |
| [Signal research](SIGNAL_RESEARCH_PROGRAM.md) | `produces` | [paper portfolio and attribution](RESEARCH_OUTPUTS.md) | planned |
| [Research outputs](RESEARCH_OUTPUTS.md) | `evidenced_by` | [journey and evidence records](JOURNEY.md) | planned |

## Phase graph

```mermaid
flowchart LR
  P00[P00 first-principles model] --> P01[P01 point-in-time finance data]
  P01 --> P02[P02 market and econometrics]
  P02 --> P03[P03 supervised ML signals]
  P01 --> P04[P04 AI evidence and deep learning]
  P03 --> P05[P05 bubble and fragility]
  P04 --> P05
  P05 --> P06[P06 portfolio and signal book]
  P06 --> P07[P07 live paper research and defense]
```

The sequence and every planned task are defined in [ROADMAP.md](ROADMAP.md). A later-course concept can be taught early under [MENTOR_MODE.md](MENTOR_MODE.md); its course week remains unconfirmed until the learner says it is complete.

Software engineering grows through [folder roles](Knowledge/K009_Project_Structure.md), [the engineering path](ENGINEERING_LEARNING_PATH.md), and the phase tasks in [ROADMAP.md](ROADMAP.md): Python execution -> SQL and data contracts -> APIs -> analyst interface and system design. These are planned links until the learner writes, runs, and explains the relevant code.

```mermaid
flowchart LR
  FS[Folder roles P00] --> PY[Python scripts and tests P00-P03]
  PY --> SQL[SQL and data contracts P01-P02]
  SQL --> EXT[External API clients P04]
  EXT --> ART[Versioned research artifacts P05]
  ART --> API[Read-only research API P06]
  API --> UI[Analyst workbench P07]
  UI --> SD[System design defense P07]
```

## Update contract

When a concept, task, source, model, or output changes:

1. Update its canonical document and status.
2. Update incoming and outgoing graph links here and in [Knowledge/INDEX.md](Knowledge/INDEX.md) where relevant.
3. Link the observed evidence from [JOURNEY.md](JOURNEY.md) and update [PROGRESS.md](PROGRESS.md).
4. Check that every internal Markdown link resolves and each graph claim matches its linked record.
5. Commit those changes together under the workflow in [GIT_WORKFLOW.md](GIT_WORKFLOW.md).

A planned link is a design relationship. An `evidenced_by` link must point to an actual saved observation, not a promise.
