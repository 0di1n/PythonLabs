#!/usr/bin/python

size = None
a = 0

while not isinstance(size, int):
    try:
        size = int(input("Введіть розмір масиву "))
    except ValueError as error:
        print("Введіть числове значення")

array = [0] * size

for i in range(0, size):
    number = None
    while not isinstance(number, int):
        try:
            number = (int(input("Введіть число ")))
        except ValueError as error:
            print("Введіть числове значення")
    array[i] = number

count = 0

for i in range(0, size):
    if array[i] >= 0:
        a += array[i]
        count += 1

print("Середнє арифметичне ", a / count)