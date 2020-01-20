matrix = []

def get_matrix(matrix_str):
    _matrix_rows = matrix_str.split('\n')
    for _row in _matrix_rows:
        row = _row.split(' ')
        matrix.append([int(element) for element in row])  

def get_leading_entry_from_row(row):
    leading_entry_ij = []
    for column_index in range(len(matrix[row])):
        if matrix[row][column_index] == 1:
            leading_entry_ij.append(row)
            leading_entry_ij.append(column_index)
            return leading_entry_ij


def print_matrix(row_size, column_size):
    print('reduced row echelon form is:')
    for i in range(row_size):
        for j in range(column_size):
            print("%.2f\t" % matrix[i][j]),
        print('')        