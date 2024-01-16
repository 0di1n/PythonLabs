#!/usr/bin/bash


import numpy as np
import matplotlib.pyplot as plt

# Визначення функції Y(x)
def Y(x):
    return -x**np.cos(5*x)

# Генерація значень x в діапазоні від 0 до 10
x_values = np.linspace(0, 10, 1000)

# Обчислення відповідних значень Y(x)
y_values = Y(x_values)

# Побудова графіка
plt.plot(x_values, y_values, label='Y(x)=-x^cos(5x)', color='blue', linestyle='-', linewidth=2)

# Додавання осей
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Встановлення підписів осей
plt.xlabel('X')
plt.ylabel('Y')

# Додавання заголовка
plt.title('Графік функції Y(x)=-x^cos(5x)')

# Додавання легенди
plt.legend()

# Показ графіка
plt.show()