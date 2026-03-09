import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

sigma_s = 5.670374419e-8

T_vals = np.arange(300, 1001, 100)
r_vals = np.linspace(0.1, 0.9, 1000)

plt.figure(figsize=(8, 8), dpi=300)

for T in T_vals:
    flux_coeff = (-16 * sigma_s / 3) * (T**3)
    flux_b = flux_coeff / r_vals
    plt.plot(r_vals, flux_b, label=f'T = {T} K')

plt.xlim(0, 1)
plt.xlabel('Length r')
plt.ylabel('Flux F(r)')
plt.grid(True, which='both', linestyle='--')
plt.legend()
plt.tight_layout()
plt.savefig('q6(b).png', dpi=600)
plt.show()
plt.close()