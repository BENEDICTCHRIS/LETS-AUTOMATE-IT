import numpy as np

def get_matrix_order(matrix):
    # Get the number of rows and columns in the matrix
    rows, cols = matrix.shape
    return rows, cols

def calculate_determinant(matrix):
    rows, cols = get_matrix_order(matrix)

    # Check if the matrix is square
    if rows != cols:
        return f"The matrix is not square ({rows}x{cols}). Determinant undefined."

    # Base case: If the matrix is 1x1, return the single element as the determinant
    if rows == 1 and cols == 1:
        return matrix[0, 0]

    determinant = 0

    # Calculate the determinant using the cofactor expansion formula
    for j in range(cols):
        cofactor = (-1) ** j * matrix[0, j] * calculate_determinant(matrix[1:, np.arange(cols) != j])
        determinant += cofactor

    return determinant

# Input matrix as a list of lists
matrix = [
    [3, 0, 0, 3, 0],
    [-3, 0, -2, 0, 0],
    [0, -1, 0, 0, -3],
    [0, 0, 0, 3, 3],
    [0, -1, 2, 0, 1]
]

# Convert the input matrix to a NumPy array
matrix = np.array(matrix)

# Get the matrix order
rows, cols = get_matrix_order(matrix)

# Calculate the determinant
determinant = calculate_determinant(matrix)

print("Input Matrix:")
print(matrix)
print(f"Matrix Order: {rows}x{cols}")
print(f"Determinant: {determinant}")
