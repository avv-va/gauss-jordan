from matrix_attr import *
from gauss_jordan import *

TESTCASE_DIRECTORY = 'testcases/testcase0.txt'      

if __name__ == '__main__':
    file = open(TESTCASE_DIRECTORY, 'r')
    matrix_str = file.read()
    
    get_matrix(matrix_str)

    row_size = len(matrix)
    column_size = len(matrix[0])

    perform_gauss_jordan(matrix, row_size, column_size)

    print_matrix(row_size, column_size)