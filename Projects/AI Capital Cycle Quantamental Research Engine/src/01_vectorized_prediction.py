import numpy as np

x = np.array([[0.20, 0.72],
             [0.40,0.68]])

w = np.array([2.0,0.5])
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
