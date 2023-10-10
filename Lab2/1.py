#!/usr/bin/python3

# Пілключаємо модулі
import module as func
import math as m

a = b = n = None

# Вводимо значення
while not isinstance(a, int) and not isinstance(b, int):
    try:
        a = int(input("Введіть значення а = "))
        b = int(input("Введіть значення b = "))
        n = int(input("Введіть значення n = "))
    except ValueError as error:
        print("Введіть числове значення")


# Перевіряемо значення а і b
if a >= 15:
    z = m.sin(2 * a) + m.cos(2 * b)
else:
    z = m.sqrt(a + (b * b))


print("z дорівнює", z)
# Викликаємо функцію з модуля
print("Ряд дорівнює", func.row(n))