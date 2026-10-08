import numpy as np


v0 = 22.0                 
m = 0.014                 
k = 1.3e-3                
g = 9.81                  
dt = 0.001                



def f(Y):
    x, y, vx, vy = Y
    v = np.sqrt(vx**2 + vy**2)

    ax = -(k/m) * v * vx
    ay = -(k/m) * v * vy - g

    return np.array([vx, vy, ax, ay])



def rk4_step(Y):
    k1 = f(Y)
    k2 = f(Y + 0.5 * dt * k1)
    k3 = f(Y + 0.5 * dt * k2)
    k4 = f(Y + dt * k3)

    return Y + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)

def simulate(angle_deg):
    angle = np.radians(angle_deg)

    
    x = 0.0
    y = 0.0
    vx = v0 * np.cos(angle)
    vy = v0 * np.sin(angle)

    Y = np.array([x, y, vx, vy])


    while True:
        Y = rk4_step(Y)
        x, y, vx, vy = Y

        if y <= 0 and x > 0:
            return x   



angles = np.arange(5, 86, 1)   
best_angle = None
max_range = 0.0

for angle in angles:
    R = simulate(angle)

    if R > max_range:
        max_range = R
        best_angle = angle


print("\n---")
print(f"Best angle: {best_angle} degrees")
print(f"Maximum range: {max_range:.2f} meters")
print("--")
