import numpy as np
from scipy.optimize import curve_fit


x = np.array([905, 910, 915, 920, 922, 924, 926, 928, 930, 935, 940, 945])
y = np.array([0, 0, 0.05, 0.2, 0.45, 0.25, 0.15, 0.40, 0.45, 0.55, 1, 1])  # Тут явно скрыта зависимость y = 2 * x

def func(x, a, b):
  return np.exp((x - a)/b) / (1 + np.exp((x - a)/b))

Init = [920, 5]
coeffs, extra = curve_fit(func, x, y, p0 = Init)
plt.scatter(
    x, y, color='blue', label='Исходные данные', zorder=5
)
x_data = np.linspace(900, 950, 100)
plt.plot(x_data, func(x_data, coeffs[0], coeffs[1]), color='red', label='Аппроксимация')
plt.legend()
plt.xlabel("Temperatures, K")
plt.ylabel("Probabilities")
plt.grid()
plt.show()
print(coeffs[0])
