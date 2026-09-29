import numpy as np

x = np.array([
    [0.55, 0.72, 0.28, 0.25, 0.18],
    [0.40, 0.68, 0.22, 0.20, 0.16],
    [0.65, 0.75, 0.35, 0.32, 0.21],
    [0.30, 0.62, 0.12, 0.08, 0.25],
    [0.25, 0.58, 0.15, 0.14, 0.12],
    [0.50, 0.65, 0.05, -0.02, 0.40]
])

w = np.array([1.2, 0.8, 1.0, 0.9, -0.3])
b = 1.0

print(x.shape)
print(w.shape)
print(b)

pred = []
for i in range(len(x)):
    subtotal = 0
    for j in range(len(w)):
        subtotal += x[i,j]*w[j]
    subtotal +=b
    pred.append(subtotal)

pred = np.array(pred)

print(pred)

pred_vectorized = np.dot(x,w)+b
print(pred_vectorized)

print(np.allclose(pred, pred_vectorized))
