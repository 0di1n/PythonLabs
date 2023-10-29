#!/usr/bin/python



# Функція яка визначає множину з  літерами, які входять в текст один раз
def task(String: str):
    uniqueElements = set()
    seenElements = set()
    List = list(String)
    for Item in List:
        if Item not in seenElements:
            uniqueElements.add(Item)
        else:
            uniqueElements.discard(Item)
        seenElements.add(Item)
    return uniqueElements

# Функція для виводу множини
def printSet(Set: set):
    for i in Set:
        print(i)

text = input("Введіть текст: ")

Set = task(text)
printSet(Set)