import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style = "darkgrid")

x1 = np.linspace(0, 1, 200)
y1 = -np.cos(np.exp(x1))

x2 = np.linspace(1.001, 2, 200)
y2 = np.log(2 * x2 + np.sin(x2 ** 2))

df1 = pd.DataFrame({"x": x1, "y": y1})
df2 = pd.DataFrame({"x": x2, "y": y2})

plt.figure(figsize = (10, 6))

sns.lineplot(data = df1, x = "x", y = "y", color = 'g', label = "f(x) = -cos(e^x)")

sns.lineplot(data = df2, x = "x", y = "y", color = '#A349A4', label = "f(x) = ln(2x + sin(x²))")

y_left = -np.cos(np.exp(1))
y_right = np.log(2 * 1 + np.sin(1))

plt.scatter(1, y_left, color = 'g', s = 50)
plt.scatter(1, y_right, color = '#A349A4', s = 50)

plt.title('График кусочной функции (Seaborn)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(0, 2)
plt.legend()

plt.show()