#!/usr/bin/python

n = 7  # Size of the square matrix
matrix = [[0] * n for _ in range(n)]  # Initialize a square matrix filled with zeros

# Populate the matrix with the desired values
for i in range(n):
    for j in range(n):
        matrix[i][j] = n - abs(j-i) 

# Print the generated matrix
for row in matrix:
    print(" ".join(map(str, row)))
