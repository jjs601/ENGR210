import numpy as np
import matplotlib.pyplot as plt
def trapz(f, x0, xN, N):
    h = (xN - x0) / N
    s = 0.5 * f(x0) + 0.5 * f(xN)
    for i in range(1, N):
        s += f(x0 + i*h)
    return h * s

if __name__ == "__main__":

    xs = np.linspace(0, 2*np.pi, 200)
    vals = [trapz(np.sin, 0, x, 200) for x in xs]

    plt.plot(xs, vals)
    plt.title("Integral of sin(x) from 0 to x")
    plt.xlabel("x")
    plt.ylabel("Integral")
    plt.grid(True)
    plt.show()
    exact = 2  
    Ns = np.array([1, 10, 100, 1000, 10000, 10000, 100000])
    hs = (np.pi - 0) / Ns
    errors = [abs(trapz(np.sin, 0, np.pi, N) - exact) for N in Ns]

    plt.loglog(hs, errors, 'o-')
    plt.title("Trapezoidal Rule Error Convergence")
    plt.xlabel("h")
    plt.ylabel("Error")
    plt.grid(True)
    plt.show()