import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import kv

def integrand(x):
    return kv(5/3, x)

def F(x):
    integral, _ = quad(integrand, x, np.inf, limit=100)
    return x * integral

F_vec = np.vectorize(F)
x_vals = np.logspace(-2.5, 1.5, 1000)
y_brem_single = np.where(x_vals <= 1.0, 1.0, 1e-14)
y_sync_single = F_vec(x_vals)

plt.figure(figsize=(6,6), dpi=300)
plt.loglog(x_vals, y_brem_single, label=r'Bremsstrahlung: $P(\omega) \sim constant$', color='red')
plt.loglog(x_vals, y_sync_single, label=r'Synchrotron: $P(\omega) \propto F(\omega)$', color='blue')
plt.xlabel('Frequency (scaled units)')
plt.ylabel('Power (scaled Units)')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.savefig('q6(i).png', dpi=300)
plt.show()
plt.close()
