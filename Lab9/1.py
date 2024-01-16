#!/usr/bin/python

import random
import string

# Генератор строк
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Перевіряє на цифри в строці
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


# Записує строки в файл
def write_to_file(filename, lines):
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')

# Cтворюємо файл TF17_1 із символьних рядків різної довжини
lines = [generate_random_string(random.randint(5, 15)) for _ in range(20)]
write_to_file('TF17_1.txt', lines)

# Переписуємо вміст файла TF17_1 у файл TF17_2 (використовуючи при цьому допоміжний файл TF17_3)
with open('TF17_1.txt', 'r') as input_file, open('TF17_2.txt', 'w') as output_file, open('TF17_3.txt', 'w') as helper_file:
    for line in input_file:
        if has_numbers(line):
            helper_file.write(line)
        else:
            output_file.write(line)

# Читаємо вміст файла TF17_2 і друкуємо його по рядках
with open('TF17_2.txt', 'r') as output_file:
    for line in output_file:
        print(line.strip())