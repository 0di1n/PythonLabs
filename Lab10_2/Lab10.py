#!/usr/bin/python


file_path = "Answers.txt"

try:
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"Surname: \n")
except Exception as e:
    print(f"An error occurred: {e}")