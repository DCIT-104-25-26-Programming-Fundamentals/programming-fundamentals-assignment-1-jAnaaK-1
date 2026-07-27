# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# ============================================

# Matrix Operations Program
# Performs transpose, addition, and multiplication on matrices

def read_matrix(rows, cols):
    """Read a matrix of size rows x cols from user input."""
    matrix = []
    for i in range(1, rows + 1):
        while True:
            try:
                row_input = input(f"Enter row {i}: ").strip().split()
                if len(row_input) != cols:
                    print(f"Error: Please enter exactly {cols} values.")
                    continue
                row = [float(val) for val in row_input]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter valid numbers separated by spaces.")
    return matrix


def display_matrix(matrix, label="Matrix"):
    """Display a matrix in a neat, aligned grid format."""
    print(f"\n{label}:")
    if not matrix:
        print("(empty)")
        return
    
    # Calculate column widths for alignment
    col_widths = []
    for col in range(len(matrix[0])):
        max_width = max(len(str(int(matrix[row][col]) if matrix[row][col] == int(matrix[row][col]) else matrix[row][col])) 
                       for row in range(len(matrix)))
        col_widths.append(max_width)
    
    # Print each row with alignment
    for row in matrix:
        row_str = "  ".join(
            str(int(val) if val == int(val) else round(val, 2)).rjust(col_widths[i])
            for i, val in enumerate(row)
        )
        print(row_str)


def transpose_matrix(matrix):
    """
    Transpose a matrix (rows become columns, columns become rows).
    Input: M x N matrix
    Output: N x M matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = []
    for col in range(cols):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transposed.append(new_row)
    
    return transposed


def add_matrices(matrix_a, matrix_b):
    """
    Add two matrices of the same size (M x N).
    Returns a new matrix where each element is the sum of corresponding elements.
    """
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    
    result = []
    for row in range(rows):
        new_row = []
        for col in range(cols):
            new_row.append(matrix_a[row][col] + matrix_b[row][col])
        result.append(new_row)
    
    return result


def multiply_matrices(matrix_a, matrix_b):
    """
    Multiply two matrices: A (M x N) × B (N x P) = Result (M x P).
    The number of columns in A must equal the number of rows in B.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])
    
    # Check if multiplication is possible
    if cols_a != rows_b:
        print(f"Error: Cannot multiply matrices. Matrix A has {cols_a} columns "
              f"but Matrix B has {rows_b} rows.")
        return None
    
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            # Calculate dot product of row i from A and column j from B
            sum_val = 0
            for k in range(cols_a):
                sum_val += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(sum_val)
        result.append(new_row)
    
    return result


def part_a_transpose():
    """Part A: Transpose a matrix."""
    print("\n" + "="*40)
    print("PART A: TRANSPOSE A MATRIX")
    print("="*40)
    
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        if rows < 1 or cols < 1:
            print("Error: Rows and columns must be positive integers.")
            return
        
        print("Enter the matrix:")
        matrix = read_matrix(rows, cols)
        
        transposed = transpose_matrix(matrix)
        
        display_matrix(matrix, "Original Matrix")
        display_matrix(transposed, "Transposed Matrix")
    
    except ValueError:
        print("Error: Please enter valid integers.")


def part_b_add():
    """Part B: Add two matrices."""
    print("\n" + "="*40)
    print("PART B: ADD TWO MATRICES")
    print("="*40)
    
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        if rows < 1 or cols < 1:
            print("Error: Rows and columns must be positive integers.")
            return
        
        print("\nEnter Matrix A:")
        matrix_a = read_matrix(rows, cols)
        
        print("\nEnter Matrix B:")
        matrix_b = read_matrix(rows, cols)
        
        result = add_matrices(matrix_a, matrix_b)
        
        display_matrix(matrix_a, "Matrix A")
        display_matrix(matrix_b, "Matrix B")
        display_matrix(result, "Sum (A + B)")
    
    except ValueError:
        print("Error: Please enter valid integers.")


def part_c_multiply():
    """Part C: Multiply two matrices."""
    print("\n" + "="*40)
    print("PART C: MULTIPLY TWO MATRICES")
    print("="*40)
    
    try:
        print("\nMatrix A dimensions:")
        rows_a = int(input("Enter number of rows: "))
        cols_a = int(input("Enter number of columns: "))
        
        print("\nMatrix B dimensions:")
        rows_b = int(input("Enter number of rows: "))
        cols_b = int(input("Enter number of columns: "))
        
        if rows_a < 1 or cols_a < 1 or rows_b < 1 or cols_b < 1:
            print("Error: All dimensions must be positive integers.")
            return
        
        if cols_a != rows_b:
            print(f"Error: Cannot multiply. Matrix A has {cols_a} columns "
                  f"but Matrix B has {rows_b} rows. They must be equal.")
            return
        
        print("\nEnter Matrix A:")
        matrix_a = read_matrix(rows_a, cols_a)
        
        print("\nEnter Matrix B:")
        matrix_b = read_matrix(rows_b, cols_b)
        
        result = multiply_matrices(matrix_a, matrix_b)
        
        if result:
            display_matrix(matrix_a, "Matrix A")
            display_matrix(matrix_b, "Matrix B")
            display_matrix(result, "Product (A × B)")
    
    except ValueError:
        print("Error: Please enter valid integers.")


def main():
    """Main program to choose which matrix operation to perform."""
    while True:
        print("\n" + "="*40)
        print("    MATRIX OPERATIONS PROGRAM")
        print("="*40)
        print("1. Transpose a Matrix (Part A)")
        print("2. Add Two Matrices (Part B)")
        print("3. Multiply Two Matrices (Part C)")
        print("4. Quit")
        print()
        
        choice = input("Select an operation (1-4): ").strip()
        
        if choice == "1":
            part_a_transpose()
        elif choice == "2":
            part_b_add()
        elif choice == "3":
            part_c_multiply()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()


# =============================================================================

