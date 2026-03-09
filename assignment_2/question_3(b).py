import numpy as np
import matplotlib.pyplot as plt

k = 1.380649e-16
h = 6.62607015e-27
c = 2.99792458e10
m = 9.1093837e-28
e = 4.80320425e-10
L = 1e17
T = 1e7
Z = 1
g = 1.2
coeff = (4.0 * Z**2 * e**6) / (3.0 * h * m * c) * np.sqrt(2.0 * np.pi / (3.0 * m * k * T))
nu = np.logspace(7, 21, 1000)
densities = [1e9, 1e11, 1e13, 1e15, 1e17, 1e19]

plt.figure(figsize=(6,6), dpi=300)
for n in densities:
    n_e = n
    n_p = n
    alpha_nu = coeff * n_e * n_p * g * (-np.expm1(-h * nu / (k * T))) / (nu**3)
    rel_diff = np.exp(-alpha_nu * L)
    plt.loglog(nu, rel_diff, label=f'$n = 10^{{{int(np.log10(n))}}}\\ cm^{{-3}}$')

plt.xlabel(r'Frequency ($Hz$)')
plt.ylabel(r'Relative difference in spectra')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.savefig('q3(b).png', dpi=300)
plt.show()
plt.close()
