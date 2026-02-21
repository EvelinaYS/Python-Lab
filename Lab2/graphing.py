import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100) # Создаем точки на оси X
y = -np.cos(np.exp(x)) # Значения функции в этих точках

x0 = 0.5 # Выбираем точку касания

y0 = -np.cos(np.exp(x0)) # Значение функции в точке касания
k = np.sin(np.exp(x0)) * np.exp(x0) # Значение производной функции в точке касания
y_kas = y0 + k * (x - x0) # Уравнение касательной

plt.plot(x, y, 'g-', label='f(x) = -cos(e^x)') #Строим график функции (зеленая линия)
plt.plot(x, y_kas, '--', color='#A349A4', label='Касательная') # Строим касательную (фиолетовая пунктирная линия)
plt.scatter(x0, y0, color='purple', s = 50) # Отмечаем точку касания размером 50

plt.annotate(f'Точка касания\n({x0}, {y0:.3f})', # Добавляем подпись к точке касания со стрелкой
             xy=(x0, y0),
             xytext=(0.6, 0.2),
             arrowprops=dict(arrowstyle='->', color='black'))

plt.title('График функции и касательная (Вариант 10)') # Заголовок
plt.xlabel('x') # Подпись оси X
plt.ylabel('y') # Подпись оси Y
plt.grid(True) # Включаем сетку
plt.legend() # Показываем легенду

plt.show()