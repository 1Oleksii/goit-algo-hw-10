import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Функція, яку інтегруємо
def f(x):
    return x**2

# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок
n = 100000

# Генеруємо випадкові точки
x_rand = np.random.uniform(a, b, n)
y_rand = np.random.uniform(0, b**2, n)  # f(x)=x^2 досягає максимуму в x=2 → f(2)=4

# Обчислюємо кількість точок під кривою
under_curve = y_rand < f(x_rand)
area_rect = (b - a) * (b**2)  # площа прямокутника, що охоплює криву

# Метод Монте-Карло для обчислення інтеграла
integral_mc = area_rect * np.sum(under_curve) / n

# Точне значення за допомогою quad
integral_exact, error = quad(f, a, b)

# Виводимо результати
print("Monte Carlo integral:", integral_mc)
print("Exact integral (quad):", integral_exact)
print("Absolute error:", abs(integral_exact - integral_mc))

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)
fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
