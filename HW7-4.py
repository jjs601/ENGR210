import numpy as np

A = np.array([
    [3,  1, -1,  2],
    [1, -2,  4,  3],
    [2, -1,  3,  2],
    [1,  1,  1,  1]]
             , dtype=float)

b = np.array([2, 2, 3, -7], dtype=float)

x = np.linalg.solve(A, b)

print(x)
