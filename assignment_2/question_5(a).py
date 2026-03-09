import numpy as np
import matplotlib.pyplot as plt

e = 4.80320425e-10
m = 9.1093837e-28
c = 2.99792458e10
B = 1e8
v1 = 0.01 * c
gamma1 = 1.0 / np.sqrt(1 - (v1/c)**2)
omega_B1 = (e * B) / (gamma1 * m * c)

plt.figure(figsize=(6,6), dpi=300)
plt.axvline(omega_B1, color='blue', label=rf'Fundamental: $\omega_B = {omega_B1/10**int(np.floor(np.log10(omega_B1))):.2f} \times 10^{{{int(np.floor(np.log10(omega_B1)))}}}\ rad s^{{-1}}$')
plt.xlim(0, 3 * omega_B1)
plt.xlabel(f'Frequency ($rad s^{{{-1}}}$)')
plt.ylabel(f'Power ($erg s^{{{-1}}} rad^{{{-1}}} s$)')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.savefig('q5(i).png', dpi=300)
plt.show()
plt.close()
