import numpy as np
import matplotlib.pyplot as plt

def calc_fields(v, gamma, t, b, q):
    denom = (gamma**2 * v**2 * t**2 + b**2)**1.5
    Ex = -q * gamma * v * t / denom
    Ey = q * gamma * b / denom
    Bz = (v/c) * Ey
    return Ex, Ey, Bz

e = 4.80320425e-10
c = 2.99792458e10+
v2 = 0.999 * c
gamma2 = 1.0 / np.sqrt(1 - (v2/c)**2)
b = 1e-8
t = np.linspace(-0.2 * b/c, 0.2 * b/c, 1000)
Ex2, Ey2, Bz2 = calc_fields(v2, gamma2, t, -b, -e)

plt.figure(figsize=(6,6), dpi=300)
plt.plot(t, Ex2, label='$E_x$', color='red')
plt.plot(t, Ey2, label='$E_y$', color='blue')
plt.plot(t, Bz2, label='$B_z$', color='green')
plt.xlabel(r'Time ($s$)')
plt.ylabel(r'Field Strength ($statVcm^{-1}$ or $Gauss$)')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.savefig('q2(ii).png', dpi=300)
plt.show()
plt.close()
