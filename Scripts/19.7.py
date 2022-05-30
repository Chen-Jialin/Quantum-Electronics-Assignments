import numpy as np
from matplotlib import pyplot as plt
n_1 = 1
n_2 = 3.5
n_3 = 3.4
t = 3e-6
a = 500e-10
lambda_0 = 0.85e-6
Lambda = 0.11e-6
s = 1
l = 1

varkappa = 2 * np.pi**2 * s**2 / (3 * l * lambda_0) * (n_2**2 - n_1**2) / n_2 * (a / t)**3 * (1 + 3 / (2 * np.pi) * lambda_0 / a / np.sqrt(n_2**2 - n_1**2) + 3 / (4 * np.pi**2) * (lambda_0 / a)**2 / (n_2**2 - n_1**2))
print('\\varkappa = ', varkappa)
Deltabeta = 2 * np.pi * 3.5 / lambda_0 - np.pi / Lambda
print('\\Delta\\beta = ', Deltabeta)

gamma_list = np.arange(1e3, 1e5, 1)
L_list = []
for gamma in gamma_list:
    L = np.log((4 / varkappa**2) * (gamma**2 + Deltabeta**2)) / (2 * gamma)
    L_list.append(L)
L_list = np.array(L_list)

plt.axes(yscale = "log")
plt.plot(L_list * 1000, gamma_list / 100)
plt.xlim([0, 2])
plt.ylim([1e1, 1e3])
plt.xlabel('Length $L$ / mm')
plt.ylabel('Threshold gain $\gamma$ / cm$^{-1}$')
plt.show()