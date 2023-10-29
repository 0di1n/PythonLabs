#!/usr/bin/python3

a = b = x = None

# Считуємо значення з терміналу
while not isinstance(a, int) and not isinstance(b, int):
    try:
        a = int(input("Введіть значення а = "))
        b = int(input("Введіть значення b = "))
    except ValueError as error:
        print("Введіть числове значення")

# Перевіряемо значення а і b
if a > b:
    x = a / b + 1
if a == b:
    x = -2
if a < b:
    x = (a - b) / a
print("Значення x = ", x)