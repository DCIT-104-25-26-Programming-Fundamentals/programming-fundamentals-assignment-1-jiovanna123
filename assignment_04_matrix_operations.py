
def read_matrix(rows, cols, name="Matrix"):
    """Helper function to read a matrix from user input line by line."""
    print(f"\nEntering values for {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ").split()
        row = [int(val) for val in row_input]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Displays a matrix in a neat, aligned grid format."""
    for row in matrix:
        print("  ".join(f"{val:>3}" for val in row))


def transpose_matrix(matrix):
    """
    PART A: Transposes an M x N matrix into an N x M matrix.
    Rows become columns, and columns become rows.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)

    return transposed


def add_matrices(matrix1, matrix2):
    """
    PART B: Adds two matrices of the same dimensions (element-wise addition).
    """
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(matrix1[r][c] + matrix2[r][c])
        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    """
    PART C: Multiplies matrix A (M x N) by matrix B (N x P).
    Result is an M x P matrix.
    """
    m = len(matrix1)
    n = len(matrix1[0])
    p = len(matrix2[0])

   
    result = []
    for i in range(m):
        row = []
        for j in range(p):
            
            cell_sum = 0
            for k in range(n):
                cell_sum += matrix1[i][k] * matrix2[k][j]
            row.append(cell_sum)
        result.append(row)

    return result


def main():
    print("=== PART A: TRANSPOSE A MATRIX ===")
    r_a = int(input("Enter number of rows: "))
    c_a = int(input("Enter number of columns: "))
    mat_a = read_matrix(r_a, c_a, "Matrix A")

    print("\nOriginal Matrix:")
    print_matrix(mat_a)

    transposed = transpose_matrix(mat_a)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    print("\n" + "=" * 40)
    print("=== PART B: ADD TWO MATRICES ===")
    print("Enter two matrices of equal dimensions.")
    r_b = int(input("Enter number of rows: "))
    c_b = int(input("Enter number of columns: "))

    m1 = read_matrix(r_b, c_b, "Matrix 1")
    m2 = read_matrix(r_b, c_b, "Matrix 2")

    sum_mat = add_matrices(m1, m2)
    print("\nSum Matrix:")
    print_matrix(sum_mat)

    print("\n" + "=" * 40)
    print("=== PART C: MULTIPLY TWO MATRICES ===")
    m = int(input("Enter rows for Matrix A (M): "))
    n = int(input("Enter columns for Matrix A / rows for Matrix B (N): "))
    p = int(input("Enter columns for Matrix B (P): "))

    mA = read_matrix(m, n, "Matrix A")
    mB = read_matrix(n, p, "Matrix B")

    prod_mat = multiply_matrices(mA, mB)
    print("\nProduct Matrix (A x B):")
    print_matrix(prod_mat)



if __name__ == "__main__":
    main()
