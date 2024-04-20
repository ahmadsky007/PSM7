import numpy as np
import matplotlib.pyplot as plt


n = 41
T_top = 100
T_other = 0


T = np.zeros((n, n))
T[0, :] = T_top



max_iter = 1000
tol = 1e-5
omega = 1.5


for iteration in range(max_iter):
    T_old = T.copy()
    for i in range(1, n-1):
        for j in range(1, n-1):
            T[i, j] = (1-omega) * T[i, j] + omega * 0.25 * (T_old[i+1, j] + T[i-1, j] + T_old[i, j+1] + T[i, j-1])

    if np.max(np.abs(T - T_old)) < tol:
        break

# Plotting the result
plt.figure(figsize=(8, 8))
plt.imshow(T, cmap='hot', interpolation='nearest')
plt.colorbar(label='Temperature (°C)')
plt.title('Temperature Distribution on a Square Plate')
plt.show()
