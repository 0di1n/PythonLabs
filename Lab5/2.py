#!/usr/bin/python

# Розмір матриці
n = 7
# Заповнюємо матрицю нулями
matrix = [[0] * n for _ in range(n)]

# Заповнюємо матрицю
for i in range(n):
    for j in range(n):
        matrix[i][j] = n - abs(j-i) 

# Виводимо матрицю
for row in matrix:
    print(" ".join(map(str, row)))
