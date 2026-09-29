import numpy as np

x = np.array([[0.55, 0.72,0.28,0.25,0.18]])

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
