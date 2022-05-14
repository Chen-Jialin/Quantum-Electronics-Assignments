import numpy as np
from scipy import special
from matplotlib import pyplot as plt
Gamma_m = np.linspace(0, np.pi, 100)
I_omega_m = special.jv(1, Gamma_m)
I_3omega_m = special.jv(3, Gamma_m)
plt.plot(Gamma_m, I_3omega_m / I_omega_m)
plt.xlim([0, np.pi])
plt.ylim([0, 1.2])
plt.xlabel('$\Gamma_m$')
plt.ylabel('$I(3\omega_m)/I(\omega_m)$')
plt.show()

Gamma_m = np.linspace(0, 0.6, 100)
I_omega_m = special.jv(1, Gamma_m)
I_3omega_m = special.jv(3, Gamma_m)
plt.plot(Gamma_m, I_3omega_m / I_omega_m)
plt.xlim([0, 0.6])
plt.ylim([0, 0.012])
plt.xlabel('$\Gamma_m$')
plt.ylabel('$I(3\omega_m)/I(\omega_m)$')
plt.show()