from matrix_attr import *
from gauss_jordan import *

TESTCASE_DIRECTORY = 'testcase0.txt'      

if __name__ == '__main__':
    file = open(TESTCASE_DIRECTORY, 'r')
    matrix_str = file.read()
    
    setMatrix(matrix_str)
    setRows(matrix_str)
    setColumns(matrix_str)

    perform_gauss_jordan(matrix, len(rows), len(columns))
