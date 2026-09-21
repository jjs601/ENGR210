import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt(r"C:\Users\farma\ENGR210\ENGR210 Fa2026 HW04 Prob2 Data.csv",
                      delimiter=",", skiprows=1)

def trapz_data(x, y):
    total = 0.0
    for i in range(len(x) - 1):
        total += ((y[i+1] + y[i]) * 0.5) * (x[i+1] - x[i])
    return total


if __name__ == "__main__":
   
    strain = data[:, 1]
    stress = data[:, 0]

    tuf = trapz_data(strain, stress)
    print("Modulus of Toughness =", tuf)
print(data)
data = np.array(data)
data[data==-999]=np.nan
plt.plot(data[:,1], data[:,0], 'o', label='strain')
plt.show()
plt.figure(figsize=(5,5))
plt.plot(data[:,2], data[:,1], 'o')
plt.show()

