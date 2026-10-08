import numpy as np
import matplotlib.pyplot as plt

k_growth = 0.3
k_predation = 0.01
k_death = 0.2
k_hunt = 0.0003

dt = 1/12
T = 10
steps = int(T/dt)

prey0 = 700
pred0 = 22

t = np.linspace(0, T, steps+1)
prey = np.zeros(steps+1)
pred = np.zeros(steps+1)
prey_hunt = np.zeros(steps+1)
pred_hunt = np.zeros(steps+1)

prey[0] = prey0
pred_euler[0] = pred0
prey_hunt[0] = prey0
pred_hunt[0] = pred0

def f_prey(prey, pred):
    return k_growth*prey - k_predation*prey*pred

def f_pred(prey, pred):
    return -k_death*pred + k_hunt*prey*pred

for i in range(steps):
    p = prey[i]
    q = pred[i]
    prey[i+1] = p + dt * f_prey(p, q)
    pred[i+1] = q + dt * f_pred(p, q)

    p = prey[i]
    q = pred[i]
    p_pred = p + dt * f_prey(p, q)
    q_pred = q + dt * f_pred(p, q)
    prey[i+1] = p + 0.5 * dt * (f_prey(p, q) + f_prey(p_pred, q_pred))
    pred[i+1] = q + 0.5 * dt * (f_pred(p, q) + f_pred(p_pred, q_pred))

plt.figure(figsize=(12,8))
