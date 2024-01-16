#!/usr/bin/python

import json

# Функція для завантаження даних з JSON-файлу
def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

# Функція для виведення на екран вмісту JSON-файлу
def display_data(data):
    print(json.dumps(data, indent=2))

# Функція для додавання нового запису у JSON-файл
def add_record(data, student_name, grades):
    record = {'Name': student_name, 'Grades': grades}
    data.append(record)

# Функція для видалення запису з JSON-файлу
def remove_record(data, student_name):
    data[:] = [record for record in data if record['Name'] != student_name]

# Функція для пошуку даних за одним із полів на вибір
def search_by_field(data, field, value):
    return [record for record in data if record.get(field) == value]

# Функція для визначення середньої оцінки кожного учня і всього класу
def calculate_averages(data):
    averages = []
    class_average = 0

    for record in data:
        grades = record['Grades']
        average = sum(grades) / len(grades)
        record['Average'] = average
        averages.append({'Name': record['Name'], 'Average': average})

    if averages:
        class_average = sum(entry['Average'] for entry in averages) / len(averages)

    return averages, class_average

# Функція для виведення прізвищ учнів, у яких середня оцінка вище середньої в класі
def display_above_class_average(data, class_average):
    above_average_students = [record['Name'] for record in data if record['Average'] > class_average]
    print("Прізвища учнів, у яких середня оцінка вище середньої в класі:", above_average_students)

# Головна функція
def main():
    json_file = 'grades.json'
    data = load_data(json_file)

    while True:
        print("\nОберіть опцію:")
        print("1. Вивести на екран вміст JSON файлу")
        print("2. Додати новий запис у JSON файл")
        print("3. Видалити запис з JSON файлу")
        print("4. Пошук даних за одним із полів")
        print("5. Розрахувати середні оцінки")
        print("6. Вивести прізвища учнів з оцінками вище середньої в класі")
        print("0. Завершити програму")

        choice = input("Ваш вибір: ")

        if choice == '1':
            display_data(data)
        elif choice == '2':
            student_name = input("Введіть прізвище учня: ")
            grades = [float(grade) for grade in input("Введіть оцінки через кому: ").split(',')]
            add_record(data, student_name, grades)
            with open(json_file, 'w') as file:
                json.dump(data, file, indent=2)
            print("Запис додано успішно.")
        elif choice == '3':
            student_name = input("Введіть прізвище учня для видалення: ")
            remove_record(data, student_name)
            with open(json_file, 'w') as file:
                json.dump(data, file, indent=2)
            print("Запис видалено успішно.")
        elif choice == '4':
            field = input("Введіть поле для пошуку: ")
            value = input("Введіть значення для пошуку: ")
            result = search_by_field(data, field, value)
            display_data(result)
        elif choice == '5':
            averages, class_average = calculate_averages(data)
            print("Середні оцінки учнів:")
            display_data(averages)
            print("Середня оцінка в класі:", class_average)
        elif choice == '6':
            averages, class_average = calculate_averages(data)
            display_above_class_average(averages, class_average)
        elif choice == '0':
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()