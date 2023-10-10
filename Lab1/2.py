#!/usr/bin/python3

N = 30
S = 0

# В циклі вирішуємо ряд
for i in range(1, N):
    S += 1/i

print("S дорівнює", S, "при N =", N)
