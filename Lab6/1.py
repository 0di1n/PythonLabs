#!/usr/bin/python


# Ініціалізуємо список
List = list()
size = 0

# Функція для записування списка у зворотньому порядку
def task(List: list, size: int):
    List.sort(reverse=True)
    size = len(List)

# Функція для виводу сиску
def printList(List: list):
    for i in List:
        print(i)

# Вводимо елементи в список
while(True):
    List.append(input("Введіть елемент в список (quit для виходу) "))
    if List[-1] == "quit":
        List.pop()
        break

task(List, size)
printList(List)
print(size)