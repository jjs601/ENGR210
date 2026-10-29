import numpy as np
import matplotlib.pyplot as plt

hpr = 0.01
L = 10.0
Tleft = 200.0
Tamb = 20.0

n = 101
dx = L/(n-1)

A = np.zeros((n,n),dtype=float)
b = np.zeros(n,dtype=float)


np.fill_diagonal(A[1:-1,1:-1], -(2 + hpr*dx**2))
np.fill_diagonal(A[1:-1,0:-2], 1)
np.fill_diagonal(A[1:-1,2:], 1)
b[1:-1] = -hpr*Tamb*dx**2

A[0,0] = 1
b[0] = Tleft


A[-1,-2] = 2
A[-1,-1] = -(2 + hpr*dx**2)
b[-1] = -hpr*Tamb*dx**2


T = np.linalg.solve(A, b)

k = np.sqrt(hpr)
def T_anal(x):
    return Tamb + (Tleft - Tamb)*np.cosh(k*(L-x))/np.cosh(k*L)

x_arr = np.linspace(0,L,n)
T_exact = T_anal(x_arr)

plt.figure(figsize=(6,5))
plt.plot(x_arr, T, 'o-')
plt.plot(x_arr, T_exact, '--')
plt.xlabel('x')
plt.ylabel('T')
plt.legend()
plt.grid(True)
plt.show()
