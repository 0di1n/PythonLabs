#!/usr/bin/python

students = {}


# Функція для додавання студента до словнику
def addStudent(Name: str, Grades: []):
    try:
        if name in students:
            raise ValueError("Учень з таким ім'ям вже існує.")
        students[name] = grades
    except ValueError as e:
        print(e)

# Функція для видалення студента зі словника
def removeStudent(Name: str):
    try:
        if name not in students:
            raise ValueError("Учень з таким ім'ям не існує.")
        del students[name]
    except ValueError as e:
        print(e)

# Функція для знаходження середньої оцінки
def calculateAverage():
    classAverage = sum(sum(grades) for grades in students.values()) / len(students)
    return classAverage

# Функція для знаходження студентів з середньою оцінкою вище чим середня класу
def aboveClassAverage():
    classAverage = calculateAverage()
    aboveAverageStudents = [name for name, grades in students.items() if sum(grades) / len(grades) > classAverage]
    return aboveAverageStudents

# Функція для виводу імен та оцінок
def displayStudents():
    for name, grades in students.items():
        print(f"{name}: {grades}")

# Функція для виводу відсортованих імен та оцінок
def displaySortedKeys():
    sortedKeys = sorted(students.keys())
    for name in sortedKeys:
        print(f"{name}: {grades}")


while True:
    print("\nОберіть опцію:")
    print("1. Додати учня")
    print("2. Видалити учня")
    print("3. Порахувати середню оцінку")
    print("4. Показати учнів з вищою середньою")
    print("5. Показати всіх учнів")
    print("6. Показати відсортовані імена учнів")
    print("7. Вийти")
    choice = input("Ваш вибір: ")
    if choice == "1":
        name = input("Введіть ім'я учня: ")
        grades = [int(grade) for grade in input("Введіть оцінки через пробіл: ").split()]
        addStudent(name, grades)
    elif choice == "2":
        name = input("Введіть ім'я учня, якого потрібно видалити: ")
        removeStudent(name)
    elif choice == "3":
        classAverage = calculateAverage()
        print(f"Середня оцінка по класу: {classAverage:.2f}")
    elif choice == "4":
        aboveAverageStudents = aboveClassAverage()
        print("Учні з вищою середньою оцінкою в класі:")
        for student in aboveAverageStudents:
            print(student)
    elif choice == "5":
        print("Учні у класі:")
        displayStudents()
    elif choice == "6":
        print("Всі імена учнів відсортовані:")
        displaySortedKeys()
    elif choice == "7":
        break