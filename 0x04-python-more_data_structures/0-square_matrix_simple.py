#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes square value of all integer of a matrix and returns new matrix."""
    new_matrix = matrix.copy()
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i].append(j**2)
    
    return (new_matrix)

