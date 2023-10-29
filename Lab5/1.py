#!/usr/bin/python

size = None
a = 0

# Вводимо розмір
while not isinstance(size, int):
    try:
        size = int(input("Введіть розмір масиву "))
    except ValueError as error:
        print("Введіть числове значення")

# Массив
array = [0] * size

# Вводимо числа в масив
for i in range(0, size):
    number = None
    while not isinstance(number, int):
        try:
            number = (int(input("Введіть число ")))
        except ValueError as error:
            print("Введіть числове значення")
    array[i] = number


# Перевіряємо на додатні елементи та додаємо
for i in range(0, size):
    if array[i] >= 0:
        a += array[i]

print("Середнє арифметичне ", a / len(array))