A = [[4.0, -1.0,  1.0, 0.0],
    [2.0,  5.0,  2.0, 0.0],
    [1.0,  2.0,  4.0, 0.0],
    [1.0, -1.0,  2.0, -1.0]]

b = [8.0, 3.0, 11.0, -8.0]
n = len(b)

for k in range(n-1):
    for i in range(k+1, n):
        factor = A[i][k] / A[k][k]
        for j in range(k, n):
            A[i][j] -= factor * A[k][j]
        b[i] -= factor * b[k]
x = [0.0]*n
x[n-1] = b[n-1] / A[n-1][n-1]

for i in range(n-2, -1, -1):
    s = b[i]
    for j in range(i+1, n):
        s -= A[i][j] * x[j]
    x[i] = s / A[i][i]

print(x)
