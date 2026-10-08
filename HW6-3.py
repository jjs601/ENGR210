import numpy as np
import matplotlib.pyplot as plt

m = 2
k = 20
x0 = 0.5
v0 = 0.0
dt = 0.1
T = 200
steps = int(T/dt)
omega = np.sqrt(k/m)

t = np.linspace(0, T, steps+1)
x_exact = x0 * np.cos(omega * t)

x_euler = np.zeros(steps+1)
v_euler = np.zeros(steps+1)
x_euler[0] = x0
v_euler[0] = v0

x_rk = np.zeros(steps+1)
v_rk = np.zeros(steps+1)
x_rk[0] = x0
v_rk[0] = v0

def a(x):
    return -(k/m)*x

for i in range(steps):
    x_euler[i+1] = x_euler[i] + dt*v_euler[i]
    v_euler[i+1] = v_euler[i] + dt*a(x_euler[i])

    k1x = v_rk[i]
    k1v = a(x_rk[i])
    k2x = v_rk[i] + 0.5*dt*k1v
    k2v = a(x_rk[i] + 0.5*dt*k1x)
    k3x = v_rk[i] +