def characteristic(row):
    return sum(x for x in row if x < 0)

def transform_matrix(matrix):
    characteristics = [characteristic(row) for row in matrix]
    sorted_indices = sorted(range(len(characteristics)), key=lambda k: characteristics[k])

    transformed_matrix = [matrix[i] for i in sorted_indices]

    return transformed_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

n = 5
matrix_A = [[-1, 2, 3], [4, -5, 6], [-7, 8, -9]]

transformed_matrix_A = transform_matrix(matrix_A)
print_matrix(transformed_matrix_A)
