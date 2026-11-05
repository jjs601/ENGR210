import numpy as np
import matplotlib.pyplot as plt

Lx = 1.0
Ly = 1.0

nx = 51
ny = 51

T = np.zeros((ny,nx))

# Replace these with actual BCs from the figure
T_top = 100
T_bottom = 0
T_left = 75
T_right = 50

T[-1,:] = T_top
T[0,:] = T_bottom
T[:,0] = T_left
T[:,-1] = T_right

tol = 1e-6
error = 1

while error > tol:

    error = 0

    for j in range(1,ny-1):
        for i in range(1,nx-1):

            Told = T[j,i]

            T[j,i] = 0.25*(
                T[j+1,i]
                + T[j-1,i]
                + T[j,i+1]
                + T[j,i-1]
            )

            error = max(error,abs(T[j,i]-Told))

plt.figure()
plt.imshow(T,origin='lower',cmap='hot')
plt.colorbar(label='Temperature')
plt.show()

plt.figure()
plt.contour(T,20)
plt.colorbar(label='Temperature')
plt.title('Temperature Contours')
plt.show()