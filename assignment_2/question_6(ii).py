import numpy as np
import matplotlib.pyplot as plt

x_vals = np.logspace(-2.5, 1.5, 1000)
y_brem_multi = np.exp(-x_vals)
y_sync_multi = x_vals**(-0.75)

plt.figure(figsize=(6,6), dpi=300)
plt.loglog(x_vals, y_brem_multi, label=r'Bremsstrahlung: $P(\omega) \propto e^{-\omega}$', color='red')
plt.loglog(x_vals, y_sync_multi, label=r'Synchrotron: $P(\omega) \propto \omega^{-s}$', color='blue')
plt.xlabel('Frequency (scaled units)')
plt.ylabel('Power (scaled Units)')
plt.legend()
plt.grid(True, which='both', linestyle='--')
plt.tight_layout()
plt.savefig('q6(ii).png', dpi=300)
plt.show()
plt.close()
