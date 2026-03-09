import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def case_a(r, I, theta):
    beta_nu = 1.2 * r * (np.cos(theta)**2)
    return beta_nu * I


def case_b(r, I, theta):
    beta_nu = 1.2 * r * np.exp(-r)
    return beta_nu * I


def case_c(r, I, theta):
    beta_nu = 1.2 * r * np.log(r)
    return beta_nu * I


r_span_a = (1, 0.1)
r_span_b = (1, 0)
r_span_c = (1, 0.1)

theta = np.linspace(0, 2 * np.pi, 1000)

I_obs_a, I_obs_b, I_obs_c = [], [], []

for th in theta:
    res_a = solve_ivp(case_a, r_span_a, [1.0], args=(th,))
    res_b = solve_ivp(case_b, r_span_b, [1.0], args=(th,))
    res_c = solve_ivp(case_c, r_span_c, [1.0], args=(th,))
    I_obs_a.append(res_a.y[0][-1])
    I_obs_b.append(res_b.y[0][-1])
    I_obs_c.append(res_c.y[0][-1])

plt.figure(figsize=(8, 8), dpi=300)
plt.subplot(111, projection='polar')
plt.plot(theta, I_obs_a, label='Case (a)', color='r')
plt.plot(theta, I_obs_b, label='Case (b)', color='g')
plt.plot(theta, I_obs_c, label='Case (c)', color='b')
plt.grid(True, linestyle='--')
plt.gca().set_rlabel_position(0)
plt.gca().set_theta_zero_location("E")
plt.title(r"$I_{\nu}(0,\theta)$ vs $\theta$", pad=30)
plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1))
plt.tight_layout()
plt.savefig('q3(b).png', dpi=600)
plt.show()
plt.close()