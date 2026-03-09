import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def T2(r):
    return 1e6 * np.exp(-r / r0)

def j_nu(nu, T):
    coef = (32.0 / 3.0) * np.sqrt(2.0 * np.pi / (3.0 * m * k * T)) * (Z**2 * e**6) / (m * c**3)
    return coef * n_e * n_i * np.exp(-h * nu / (k * T))

def alpha_nu(nu, T):
    coef = (4.0 / 3.0) * np.sqrt(2.0 * np.pi / (3.0 * m * k * T)) * (Z**2 * e**6) / (h * m * c)
    return coef * n_e * n_i * (1.0 - np.exp(-h * nu / (k * T))) / (nu**3)

def transfer_eq2(I, r, nu):
    T = T2(r)
    return j_nu(nu, T) - alpha_nu(nu, T) * I

k = 1.380649e-16
h = 6.62607015e-27
c = 2.99792458e10
e = 4.80320425e-10
m = 9.1093837e-28
Z = 1
n_e = 1e8
n_i = 1e8
r0 = 0.5
r_span = np.linspace(0, r0, 1000)
frequencies = [1e6, 1e7, 1e8, 1e9, 1e10, 1e11, 1e12, 1e13, 1e14, 1e15, 1e16]

plt.figure(figsize=(6,6), dpi=300)
for nu in frequencies:
    I_sol2 = odeint(transfer_eq2, 0.0, r_span, args=(nu,))
    plt.plot(r_span / r0, I_sol2, label=f'$\\nu = 10^{{{int(np.log10(nu))}}}$ Hz')

plt.xlabel(r'$r / r_0$')
plt.ylabel(r'$I_\nu / \bar{g}_{ff}\ (erg s^{-1} cm^{-2} Hz^{-1})$')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.savefig('q1(b).png', dpi=300)
plt.show()
plt.close()
