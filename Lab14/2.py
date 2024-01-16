#!/usr/bin/python

import matplotlib.pyplot as plt
import csv
import numpy as np

# Reading data from a CSV file

# Lists to store data
years = list()
enrollment_Ukraine = list()
enrollment_USA = list()

# Read data from CSV file
with open('enrolment.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Skip header
    next(csv_reader)

    for row in csv_reader:
        years.append(row[4:9])  # Assuming the years are in the 4th to 8th columns
        enrollment_Ukraine.append(float(row[8]))  # Assuming enrollment values are in the 9th column
        enrollment_USA.append(float(row[8]))  # Assuming enrollment values are in the 10th column

# Line plot for the dynamics of primary education enrollment
plt.figure(figsize=(10, 6))
plt.plot(years, enrollment_Ukraine, label='Ukraine', marker='o')
plt.plot(years, enrollment_USA, label='United States', marker='o')

plt.title('Dynamics of Primary Education Enrollment')
plt.xlabel('Year')
plt.ylabel('Enrollment (number)')
plt.legend()
plt.show()

# Bar chart to compare enrollment numbers for Ukraine and the United States
plt.figure(figsize=(8, 5))
plt.bar('Ukraine', enrollment_Ukraine[-1], color='blue', label='Ukraine')
plt.bar('United States', enrollment_USA[-1], color='orange', label='United States')

plt.title('Primary Education Enrollment for Ukraine and the United States (Latest Year)')
plt.xlabel('Country')
plt.ylabel('Enrollment (number)')
plt.legend()
plt.show()