#!/usr/bin/python

# Ініціалізуємо списки
List = list()
List2 = []

# Функція яка формує новий список, у який входить кожен другий елемент поточного списку
def task(List: list):
    tmpList = List[1::2]
    return tmpList

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

List2 = task(List)
printList(List2)