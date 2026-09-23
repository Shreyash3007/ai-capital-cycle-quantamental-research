# Initial data dictionary

This document defines the first model variables and the finance meaning that later real-data work must preserve.

## Unit of observation

In ML-G01, one row is one fictional company at one observation date. The values are synthetic and exist only for learning.

Later, the unit will become one real company-observation date with point-in-time availability metadata.

## Feature definitions

| Feature | Initial representation | Finance meaning | Important limitation |
|---|---:|---|---|
| revenue growth | decimal, such as `0.40` for 40% | change in revenue over a declared comparable period | growth quality, acquisitions, currency, and base effects are not captured |
| gross margin | decimal | revenue remaining after cost of revenue | classification differs across companies |
| operating margin | decimal | operating income divided by revenue | stock compensation and restructuring treatment can distort comparison |
| free-cash-flow margin | decimal | free cash flow divided by revenue | free cash flow definitions and working-capital timing vary |
| R&D intensity | decimal | research and development expense divided by revenue | accounting expense is not the same as economic investment quality |

All five variables are ratios with broadly comparable numeric scale so the first prediction, cost, and gradient tasks can be understood without scaling. T04 then implements scaling, compares convergence, and explains why parameters must be fitted only on training data.

## Initial target

The planned target is the natural logarithm of a positive valuation multiple:

```text
y = ln(observed valuation multiple)
```

The exact multiple for the first frozen real-data adaptation will be chosen only after denominator quality is reviewed. A log transform can reduce skew and makes differences multiplicative, but it does not make the target automatically valid.

## Initial prediction and residual

```text
predicted_log_multiple = X @ w + b
valuation_stretch = observed_log_multiple - predicted_log_multiple
```

Positive stretch means observed valuation is above this model's estimate. It can arise from omitted quality, market power, accounting differences, speculation, bad data, or model error.

## Missing and invalid values later

- Do not replace missing values silently.
- Do not calculate a multiple with an invalid or near-zero denominator without an explicit rule.
- Preserve original units and the transformation log.
- Record whether a value was reported, calculated, estimated, or imputed.
- Fit any imputation using training data only.

## Naming and shape convention

- `m`: number of observations or rows.
- `n`: number of features or columns.
- `X`: feature matrix with shape `(m, n)`.
- `y`: target vector with shape `(m,)` unless a task explicitly teaches column vectors.
- `w`: parameter vector with shape `(n,)`.
- `b`: scalar bias.
- `y_hat`: prediction vector with shape `(m,)`.
