# Learning manual: AI Capital Cycle research engine

This is the one document to read and work from. It grows as you build the project. The current lesson is first; later lessons will be added here in the order you reach them. You write every assignment-code line. The mentor explains the idea, watches your runs, checks your reasoning, and keeps the checkpoint accurate.

## Where you are now

| Item | Current state |
|---|---|
| Course study | Machine Learning Specialization C1W1 and C1W2 completed, learner-reported; C1W3 not confirmed |
| Project | P00, first-principles valuation-stretch foundation |
| Active task | ML-G01-T02: cost and residuals; T01 independent transfer remains open |
| Correct so far | T01 guarded loop and vectorized functions agree on all six named company predictions; changed-input and shape-failure runs observed |
| Still to demonstrate | T01 independent explanation; T02 hand error, cost, signed residuals, changed-target run, and plot |
| Code | T01 named-output script runs; T02 learner file is empty and ready for your code |
| Evidence-backed progress | T01 0%, T02 0%, P00 0%, overall 0%; successful assisted runs are not independent mastery |

![Current learning flow from prediction to cost and residuals](Visuals/current_lesson_flow.png)

The picture is a rendered PNG, not a Mermaid code block. The table above gives the same state if an image viewer is unavailable.

# Lesson 02: Measure the prediction errors

## Why this follows prediction

T01 answered "what does this trial model predict?" T02 asks "how far are those predictions from the observed values?" This returns to the C1W1 cost function you studied. The six targets below are invented teaching values, not live market prices. We will calculate a cost, keep each signed valuation gap, and make a residual plot. Gradient descent in T03 will then use cost to decide how to change the weights.

## One worked example before your finance code

A delivery model predicts 8 and 10 minutes; the actual times are 9 and 7 minutes. Define the prediction error as `predicted - actual`:

| Delivery | Predicted | Actual | Error | Error squared | Residual: actual - predicted |
|---|---:|---:|---:|---:|---:|
| First | 8 | 9 | -1 | 1 | 1 |
| Second | 10 | 7 | 3 | 9 | -3 |

The C1W1 cost is the sum of squared errors divided by twice the number of rows: `J = (1 + 9) / (2 * 2) = 2.5`. Squaring makes both misses positive and gives a large miss more influence. The signed residual answers a different question: which side of the prediction was the actual value on? A positive valuation residual means observed valuation was above the model's estimate, not that the company is in a bubble.

## Your frozen inputs

| Company | Trial prediction | Synthetic observed log multiple |
|---|---:|---:|
| AstraCompute | 2.687 | 2.800 |
| NexaCloud | 2.376 | 2.200 |
| VertexChips | 2.955 | 3.100 |
| ModelWorks | 1.973 | 1.900 |
| DataForge | 2.004 | 2.100 |
| CobaltAI | 2.032 | 2.400 |

Use [02_cost_and_residuals.py](Projects/AI%20Capital%20Cycle%20Quantamental%20Research%20Engine/src/02_cost_and_residuals.py). It is empty so the assignment code remains yours. We supply predictions here to focus on cost before teaching imports between files. Both arrays should have shape `(6,)`, one value per company. Do not mistake these synthetic targets for measured market data.

## Do this now

First, enter the two arrays and print their shapes. Before running, calculate AstraCompute's error (`prediction - observed`), squared error, and signed residual (`observed - prediction`) by hand. Then run the file and compare. The mentor will teach every unfamiliar Python line using the delivery example first. Once this checkpoint runs, write the cost function, test a changed target and a mismatched length, then make and inspect a labeled residual plot. You do not need to reopen other documents to follow the lesson.

T01's named output is a valid assisted run. Its explanation and independent transfer remain open, but they do not stop us from learning T02. Task credit follows demonstrated understanding, not how many scripts have been typed.

## How the whole journey grows

| Stage | ML and finance | Python and engineering | Visible result |
|---|---|---|---|
| P00, now | Prediction, cost, gradient descent, multiple features, scaling, and a limited valuation-stretch signal | Values, arrays, loops, functions, `src`/`data`/`outputs`/`tests`, runs and checks | Predictions, cost curve, actual-versus-predicted plot, residual plot |
| P01 | Company fundamentals and information available at each date | File loading, SQL tables, keys, joins, and source records | Traceable company-quarter data |
| P02-P03 | Market behavior, event studies, and tested ML signals | Reusable modules, tests, repeatable model runs | Evaluation and failure reports |
| P04-P05 | AI evidence, expectations, and bubble fragility | External APIs, typed responses, versioned research records | Source-linked competing theses and fragility report |
| P06-P07 | Paper portfolio and live paper research | Read-only API, small analyst interface, reliability and system design | Evidence-linked research workflow and defended system |

These are future learning stages, not completed capabilities. We study the next layer when the current research problem needs it.

# Lesson 01: Predict before training

## 1. What you are building

You will make a small Python program that calculates a model output for each fictional company. First you will do the calculation with a loop. Then you will use NumPy to do the same calculation across rows. Both versions must agree. This prepares the inputs for the C1W1 cost function and gradient descent tasks that follow.

**Why now:** You already studied linear regression in C1W1 and vectorization in C1W2. The fastest way to make those ideas usable is to connect one hand calculation to arrays, Python execution, and a checked output. The five-feature version comes later in this same task.

**What you will get:** a learner-written, runnable prediction script and evidence that you understand the numbers and shapes. This is not a trained or investable model.

## 2. The concept and the finance meaning

For one feature, a linear model says:

```text
prediction = weight * feature + bias
```

The **feature** is an input, here revenue growth written as a decimal ratio. `0.20` means 20% growth, not 0.20%. The **weight** says how strongly that input changes the model output. The **bias** is the output when the feature is zero. These are mathematical roles; the trial weight and bias in this exercise were supplied, not learned from company data.

Later, the model output will stand for an estimated log valuation multiple. An observed value above the model's estimate will be called valuation stretch. A stretch is only a model difference; it does not by itself show mispricing, a bubble, or a future price move.

The first two companies are fictional:

| Company | Revenue growth | Trial weight | Trial bias | Your hand prediction |
|---|---:|---:|---:|---:|
| AstraCompute | 0.20 | 2.0 | 1.0 | 1.4, checked |
| NexaCloud | 0.40 | 2.0 | 1.0 | 1.8, checked |

The same weight and bias apply to both rows. You calculated both outputs correctly. The next question is how to represent this calculation for any number of rows without losing track of the dimensions.

## 3. Rows, features, weights, and shapes

A **shape** tells you how many entries an array has along each dimension. A table has rows and columns. Here one row is one company; one column is one feature. We call the table `X`. With two companies and one feature, your answer `X.shape == (2, 1)` is correct.

Use these rules to reason, not to memorize an answer:

- Each feature has a corresponding weight.
- Each company row produces one prediction.
- The bias is one number added to each row's weighted result.
- A one-dimensional NumPy array reports its shape with a trailing comma, such as `(3,)`; that is different from a three-row, one-column table `(3, 1)`.

Different example: suppose three companies each have **two** features. The input table has shape `(3, 2)`. There are two weights, so a one-dimensional weight array has shape `(2,)`. One output per company gives a prediction array of shape `(3,)`. The inner dimensions match: each two-feature row pairs with two weights.

**Current run:** with two features, `x.shape` is `(2, 2)` and `w.shape` is `(2,)`. Each row's first feature pairs with `w[0]` and second feature pairs with `w[1]`. Your saved program produced `[1.76 2.14]` by both methods. You still need to explain that pairing in your own words.

## 4. The Python ideas you will use

| Idea | Python form to recognize | Why it matters here |
|---|---|---|
| Import NumPy | `import numpy as np` | Gives you array operations. |
| Make an array | `np.array([...])` | Stores ordered numeric inputs or weights. |
| Inspect shape | `value.shape` | Checks the array you actually created. |
| Loop through values | `for item in values:` with an indented body | Makes each calculation visible before vectorizing. |
| Define a function | `def name(inputs):` and `return result` | Lets a calculation be rerun on changed input. |
| Dot product | `np.dot(matrix, weights)` | Multiplies each row's features by matching weights and sums them. |
| Compare numeric outputs | `np.allclose(first, second)` | Checks corresponding values within a small floating-point tolerance; it does not test whether the model is financially valid. |

These are building blocks, not a finished solution. You decide the variable names, array contents, functions, and control flow in the learner file. If a Python line is unfamiliar, we will explain that line on a different tiny example before you write it for this task.

`np.allclose(pred, pred_vectorized)` returned `True` in your two-feature run. This means both arrays have nearly equal values in corresponding positions. Small rounding differences can occur in decimal arithmetic, so numerical code often uses a tolerance rather than demanding identical stored bits. A `True` result only compares these two calculations on these inputs; both could still implement the same wrong finance idea.

## 5. Why the files are separated

| Folder | Job | Use in this task |
|---|---|---|
| `src/` | Source code, the instructions that calculate a result | Your first Python script lives here. |
| `data/` | Frozen inputs, later including dated source snapshots | The two-row fixture may stay in the script for now. |
| `outputs/` | Results such as saved plots and tables | No plot is due at this first shape check. |
| `tests/` | Checks that reveal wrong behavior | We begin with hand and changed-input checks. |

`src` is a common folder name, not a special Python command. Keeping code, inputs, outputs, and checks separate makes it possible to ask: which code and data produced this result, and did a test catch a mistake? We will add SQL, an API, and a browser interface only when those layers solve a real research problem. No database or server is needed today.

## 6. Your work, in order

| Step | What you do | Evidence | State |
|---|---|---|---|
| 1 | Calculate the two outputs by hand. | `1.4` and `1.8` | Done |
| 2 | Explain the input, weight, and output shapes. | Correct sizes and one sentence on matching dimensions | In progress; sizes correct, explanation pending |
| 3 | Write a Python loop for the two rows. | Run it and compare with the hand values | General nested loop observed on two-feature data; explanation pending |
| 4 | Write the vectorized NumPy form. | Show that both versions agree | Observed on two-feature data; explain `allclose` |
| 5 | Add a second feature, then the five-feature fixture. | Explain new shapes and compare both versions | Full and changed-input runs observed; independent explanation pending |
| 6 | Change an input and intentionally create one bad shape. | Explain the changed output and the error | Runs observed; learner explanation pending |

The first complete shape-and-hand check earns the first T01 progress credit. Correct arithmetic and `X` alone are saved as partial evidence, not full credit. The mentor will update this page after each meaningful checkpoint.

## 7. When you reach the editor

Open `D:\ML-project\Projects\AI Capital Cycle Quantamental Research Engine\src\01_vectorized_prediction.py`. It contains your learner-written two-feature version with a nested loop that handles any number of matching feature columns and weights. Preserve this working baseline as you extend the fixture.

From PowerShell, after you have written the code, the file can be run from any directory with:

```powershell
python "D:\ML-project\Projects\AI Capital Cycle Quantamental Research Engine\src\01_vectorized_prediction.py"
```

Before each first run, say what you expect to see. After the run, compare the actual values and shapes. A mismatch is a useful observation to diagnose, not a reason to rush past the line.

## 8. Visual evidence still to come

Today's picture shows the task path, not model performance. When you reach gradient descent, you will plot cost against training steps to see whether learning is converging. Later you will plot actual against predicted values and the residuals, which are the differences between them. Each plot must come from your executed code and have an explanation of what it does and does not show.

## Current work block: prediction audit

**What and why:** turn your working script into two reusable prediction functions with a shape check. The four-weight experiment showed why a run that prints numbers can still be wrong: the old loop silently ignored one feature. The output is a named prediction table plus original, changed-input, and invalid-shape runs that you can explain in a research review.

### First teaching pass: a function

A function gives a calculation a name. You put inputs in its parentheses; `return` sends the result back to the caller. Start with this different example:

```python
def double_with_fee(value, fee):
    result = value * 2 + fee
    return result

print(double_with_fee(3, 1))  # 7
```

Line 1 defines a reusable calculation and names two inputs. Line 2 calculates from those inputs. Line 3 sends the result back. The last line calls the function with `3` and `1`, then prints `7`. The indented lines belong to the function; the unindented `print` runs after the definition.

For the assisted first pass, you completed and called the function with these lines:

```python
def vector_pred(x, w, b):
    return np.dot(x, w) + b

print(vector_pred(x, w, b))
```

The indented `return` belongs to the function; the unindented `print` calls it. `x`, `w`, and `b` inside the function are inputs supplied by that call. `np.dot(x, w) + b` is the calculation you had already run outside a function. `return` hands its six-number array back to `print`. The run repeated the original six predictions. This was assisted teaching, not independent mastery.

**Current result:** that teaching pass is done. You added a shape guard to `vector_pred`, tested its own error, and wrote `loop_pred` with the same guard. Both functions return the same six predictions. The earlier top-level loop and dot calculation still run too, so the script prints repeated outputs; later cleanup will keep one clear path through the functions.

### Why this task exists

This is the **prediction** part of linear regression, not training yet. Each company row contains five financial ratios. Each ratio pairs with one supplied weight; their products are summed and the bias is added once. A loop makes every step inspectable. `np.dot` performs the same row-wise calculation compactly. The function names let later cost and training code call the calculation with new inputs and weights instead of duplicating it. The guards stop a misleading run when the number of feature columns and weights differs.

The numbers are a toy estimated log valuation multiple from synthetic data and trial parameters. Their agreement shows the two implementations match, not that the model fits real valuations or predicts market returns.

### What comes next

| Project task | What you will build | Why it follows |
|---|---|---|
| Finish T01 | Remove duplicate top-level calculations, show named company predictions, rerun original/changed/error cases, and explain limits | Leaves one clean, reusable prediction tool |
| T02: cost and residuals | Compare predictions with synthetic observed targets, calculate errors and squared-error cost | Measures how far the model is from known values |
| T03: gradients and gradient descent | Calculate how weights and bias should change, update them repeatedly, and plot cost over steps | Trains the model instead of using trial weights |
| T04-T06 | Scaling, feature experiments, and a limited valuation-stretch research output | Tests whether the training and finance interpretation hold up |

Your course coverage is C1W1 and C1W2, learner-reported. T01 applies C1W1 prediction and C1W2 multiple features/vectorization. T02 and T03 deliberately return to the C1W1 cost and gradient-descent ideas you already studied. C1W3 is not marked complete until you confirm it.

### Later in this work block

Here is a worked example of the same *type* from delivery planning, not the finance assignment. Each route has two measurements, distance and delay; the function checks that each measurement has a matching penalty before calculating a score:

```python
import numpy as np

def delivery_scores(routes, penalties):
    if routes.ndim != 2 or penalties.ndim != 1:
        raise ValueError("Expected a route table and a weight list")
    if routes.shape[1] != penalties.shape[0]:
        raise ValueError("One penalty is required per route measurement")
    return np.dot(routes, penalties)

routes = np.array([[2, 3], [4, 1]])
penalties = np.array([10, 1])
for name, score in zip(["North", "South"], delivery_scores(routes, penalties)):
    print(name, score)
# North 23; South 41
```

Your larger assignment, after the first teaching passes:

1. In your existing Python file, make separate learner-written loop and vectorized prediction functions accepting `x`, `w`, and `b`; each returns a one-dimensional prediction array. Add a feature/weight shape check before both calculations.
2. Print company names beside the six predictions from the frozen table below. Show the shapes and `np.allclose` result. Check equal output shapes as well as close values.
3. Run the frozen table, one changed input, and one four-weight failure. Restore the frozen data and five weights afterward. Send the three outputs or error together.
4. Write four short sentences: why the old loop omitted a feature, what `np.allclose` proves, what one prediction represents, and why these supplied weights cannot establish real valuation accuracy.

Use this full frozen synthetic table for your original run:

| Company | Revenue growth | Gross margin | Operating margin | FCF margin | R&D intensity |
|---|---:|---:|---:|---:|---:|
| AstraCompute | 0.55 | 0.72 | 0.28 | 0.25 | 0.18 |
| NexaCloud | 0.40 | 0.68 | 0.22 | 0.20 | 0.16 |
| VertexChips | 0.65 | 0.75 | 0.35 | 0.32 | 0.21 |
| ModelWorks | 0.30 | 0.62 | 0.12 | 0.08 | 0.25 |
| DataForge | 0.25 | 0.58 | 0.15 | 0.14 | 0.12 |
| CobaltAI | 0.50 | 0.65 | 0.05 | -0.02 | 0.40 |

The weights are in the same column order: `[1.2, 0.8, 1.0, 0.9, -0.3]`, with bias `1.0`. The original run produced `[2.687 2.376 2.955 1.973 2.004 2.032]`; the changed NexaCloud row produced `[2.687 2.496 2.955 1.973 2.004 2.032]`. These are supplied trial weights on synthetic companies, not a validated valuation model.

## How this manual is maintained

The mentor updates the current state and rendered picture only after observing your answer or run. New lessons are added here in sequence so this remains your one learning and doing document. Detailed task, evidence, and progress records still exist in the repository for audit, but you do not need to open them to do the current exercise. No course week or project task is marked complete merely because it appears here.
