#!/usr/bin/python

import csv

# Функція для отримання даних за рік з CSV-файлу
def get_exports_data_from_csv(filename):
    exports_data = {}
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            country = row['Country Name']
            exports_data[country] = {'2018': row['2018 [YR2018]'], '2019': row['2019 [YR2019]']}
    return exports_data

# Функція для виведення даних на екран та запису у CSV-файл
def print_csv(data):
    fieldnames = ['Country Name', 'Exports (% of GDP) 2018', 'Exports (% of GDP) 2019']
    for country, values in data.items():
        print(f'{country}: {values["2018"]}, {values["2019"]}')



# Отримання даних з CSV-файлу
combined_data = get_exports_data_from_csv('GDP.csv')

# Виведення на екран CSV-файлу
print_csv(combined_data)

# Пошук даних для введених користувачем країн
user_input_countries = input("Введіть назви країн через кому: ").split(', ')
user_input_data = {country: combined_data[country] for country in user_input_countries if country in combined_data}

# Запис результату пошуку у новий CSV-файл
print_and_save_to_csv(user_input_data, 'user_input_exports_data.csv')