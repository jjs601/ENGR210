import numpy as np
import matplotlib.pyplot as plt

# properties
k = 25.0
ho = 1000.0
hi = 200.0
Tho = 1700.0
Thi = 400.0

# quarter-cell dimensions (m)
Lx = 0.005
Ly = 0.003

dx = dy = 0.0001

nx = int(Lx/dx)+1
ny = int(Ly/dy)+1

Bi_o = ho*dy/k
Bi_i = hi*dx/k

T = np.ones((ny,nx))*800

channel_depth = int(0.001/dy)
channel_halfwidth = int(0.003/dx)

tol = 1e-6
err = 1.0

while err > tol:

    Told = T.copy()

    # symmetry boundaries
    T[:,0] = T[:,1]
    T[0,:] = T[1,:]

    # hot outer surface
    for i in range(nx):
        T[-1,i] = (T[-2,i] + Bi_o*Tho)/(1+Bi_o)

    # channel roof
    for i in range(channel_halfwidth):
        T[channel_depth,i] = (
            T[channel_depth+1,i]
            + Bi_i*Thi
        )/(1+Bi_i)

    # channel side wall
    for j in range(channel_depth):
        T[j,channel_halfwidth] = (
            T[j,channel_halfwidth+1]
            + Bi_i*Thi
        )/(1+Bi_i)

    # Gauss-Seidel update
    for j in range(1,ny-1):
        for i in range(1,nx-1):

            if j <= channel_depth and i <= channel_halfwidth:
                continue

            T[j,i] = 0.25*(
                T[j+1,i]
                + T[j-1,i]
                + T[j,i+1]
                + T[j,i-1]
            )

    err = np.max(np.abs(T-Told))

print("Maximum temperature =", np.max(T), "K")

plt.figure(figsize=(7,5))
plt.imshow(
    T,
    origin='lower',
    extent=[0,Lx*1000,0,Ly*1000],
    aspect='auto'
)
plt.colorbar(label='Temperature (K)')
plt.xlabel('x (mm)')
plt.ylabel('y (mm)')
plt.title('Quarter-Symmetry Temperature Field')
plt.show()