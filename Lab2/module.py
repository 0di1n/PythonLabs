
# Вирішуємо ряд
def row(n):
    row = 0
    for i in range(1, n):
        row = row + ((n+1)/n)
    return row