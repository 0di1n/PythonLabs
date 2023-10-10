#!/usr/bin/python3

n = int(input("Введіть кількість рядків: "))
 # Генеруємо трикутник з чисел 
for i in range(n, 0, -1): 
    # Додаємо пробіли перед числами
    for j in range(n - i):
        print(" ", end=" ")
    # Пишемо числа
    for k in range(i, 0, -1):
        print(n - k + 1, end=" ")
    print()