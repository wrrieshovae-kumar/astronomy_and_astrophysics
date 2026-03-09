import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import kv

def integrand(x):
    return kv(5/3, x)

def P(x):
    integral, _ = quad(integrand, x, np.inf, limit=100)
    F = x * integral
    P = (np.sqrt(3) * e**3 * B * np.sin(alpha)) / (2 * np.pi * m * c**2) * F
    return P

e = 4.80320425e-10
m = 9.1093837e-28
c = 2.99792458e10
B = 1e8
alpha = np.pi / 2
v2 = 0.999 * c
gamma2 = 1.0 / np.sqrt(1 - (v2/c)**2)
omega_B2 = (e * B) / (gamma2 * m * c)
omega_c2 = (3.0 / 2.0) * (gamma2**3) * omega_B2 * np.sin(alpha)
P_vec = np.vectorize(P)
x_vals = np.logspace(-2, 1, 1000)
omega_vals = x_vals * omega_c2
power_vals = P_vec(x_vals)

plt.figure(figsize=(6,6), dpi=300)
plt.loglog(omega_vals, power_vals, color='red', label='Continuum')
plt.axvline(omega_c2, color='green', linestyle='--', label = rf'Critical: $\omega_c = {omega_c2/10**int(np.floor(np.log10(omega_c2))):.2f} \times 10^{{{int(np.floor(np.log10(omega_c2)))}}}\ rad s^{{-1}}$')
plt.xlim(np.min(omega_vals), np.max(omega_vals))
plt.xlabel(f'Frequency ($rads^{{{-1}}}$)')
plt.ylabel(f'Power ($erg s^{{{-1}}} rad^{{{-1}}} s$)')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.savefig('q5(ii).png', dpi=300)
plt.show()
plt.close()
