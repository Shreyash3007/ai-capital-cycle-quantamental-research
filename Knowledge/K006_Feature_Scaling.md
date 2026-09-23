# K006: Feature scaling

**Course coverage:** C1W2, learner-reported. **Project evidence:** none yet.

Feature scaling changes numeric ranges so optimization can move more evenly across parameters. It changes the coordinate system of a model, not the underlying business fact. A scaler fitted using later data would leak information into a historical test.

**Requires:** [multiple features](K004_Multiple_Features.md) and [gradient descent](K003_Gradient_Descent.md). **Used by:** [P00 T04](../PHASE_00_C1W2_PLAN.md). **Research rule:** [point-in-time evaluation](../RESEARCH_AND_EVALUATION_STANDARD.md).

**Demonstration gate:** calculate and implement a training-only scaler, compare convergence, transform changed inputs consistently, and explain leakage. Link the eventual evidence here.
