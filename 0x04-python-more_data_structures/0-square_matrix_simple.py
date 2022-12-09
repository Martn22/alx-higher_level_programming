#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes square value of all integer of a matrix and returns new matrix."""
    matrix = []
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(j**2)
    return new_matrix
