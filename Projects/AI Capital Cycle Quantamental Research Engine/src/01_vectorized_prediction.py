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
    pred.append(((w[0]*x[i,0]) + w[1]*x[i,1])+b)

pred = np.array(pred)

print(pred)

pred_vectorized = np.dot(x,w)+b
print(pred_vectorized)

print(np.allclose(pred, pred_vectorized))
