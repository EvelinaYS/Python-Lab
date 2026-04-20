import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
y = -np.cos(np.exp(x))

x0 = 0.5

y0 = -np.cos(np.exp(x0))
k = np.sin(np.exp(x0)) * np.exp(x0)
y_kas = y0 + k * (x - x0)

plt.plot(x, y, 'g-', label='f(x) = -cos(e^x)')
plt.plot(x, y_kas, '--', color='#A349A4', label='Касательная')
plt.scatter(x0, y0, color='purple', s = 50)

plt.annotate(f'Точка касания\n({x0}, {y0:.3f})',
             xy=(x0, y0),
             xytext=(0.6, 0.2),
             arrowprops=dict(arrowstyle='->', color='black'))

plt.title('График функции и касательная (Вариант 10)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.show()