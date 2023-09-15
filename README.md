# LETS-AUTOMATE-IT
Certainly, adding a README file to your project is a good practice to help others understand how to use and navigate your code. Here's an example of a README file that you can include with your matrix determinant calculation project:

```markdown
# Matrix Determinant Calculator

This Python program calculates the determinant of a square matrix of any order. It takes a matrix as input, determines its order, and calculates the determinant using the cofactor expansion method.

## Usage

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/BENEDICTCHRIS/matrix-determinant-calculator.git
   ```

2. Navigate to the project directory:

   ```
   cd matrix-determinant-calculator
   ```

3. Open the `determinant_calculator.py` file in your preferred Python environment.

4. Modify the `matrix` variable with your desired square matrix.

5. Run the program:

   ```
   python determinant_calculator.py
   ```

6. The program will display the input matrix, its order (number of rows and columns), and the calculated determinant.

## Example

Here's an example of how to use this program:

```python
# Input matrix as a list of lists
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
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
```

## Requirements

- Python 3.x
- NumPy library (install it using `pip install numpy`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
