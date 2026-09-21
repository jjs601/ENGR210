import numpy as np
import matplotlib.pyplot as plt

amplitude = 2
period = 24
t_max = 2 * period
t = np.linspace(0, t_max, 1000)

omega = 2 * np.pi / period

sine_wave = amplitude * np.sin(omega * t)
cosine_wave = amplitude * np.cos(omega * t)

plt.figure(figsize=(10, 6))
plt.plot(t, sine_wave, color='green', linestyle='--', label='Sine')
plt.plot(t, cosine_wave, color='red', linestyle='-.', label='Cosine')

plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.grid(True)
plt.savefig('wave_oscillation.png')
plt.show()