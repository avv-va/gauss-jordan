def find_first_non_zero_column_element_row(matrix, row_size, column_size, row_start_index): 
    for column_index in range(column_size):
        for row_index in range(row_start_index, row_size):
            if matrix[row_index][column_index] != 0:
                return row_index

def replace_selected_rows_in_matrix(matrix, row_index1, row_index2):
    matrix[row_index1], matrix[row_index2] = matrix[row_index2], matrix[row_index1]

def set_appropriate_leading_entry_for_row(matrix, row_index):
    first_element = 0
    for column_index in range(len(matrix[row_index])):
        if matrix[row_index][column_index] !=0:
            if first_element == 0: 
                first_element = matrix[row_index][column_index]
            if first_element != 0:
                matrix[row_index][column_index] =  (float)(matrix[row_index][column_index])/first_element

def set_appropriate_elements_for_leading_entry_column(matrix, row_start_index, row_size, column_size): 
    # get leading entry
    leading_entry_ij = []
    for column_index in range(len(matrix[row_start_index])):
        if matrix[row_start_index][column_index] == 1:
            leading_entry_ij.append(row_start_index)
            leading_entry_ij.append(column_index)
            break
            
    for row_index in range(row_start_index+1, row_size):
        alpha = -1 * (float)(matrix[row_index][leading_entry_ij[1]]) / matrix[leading_entry_ij[0]][leading_entry_ij[1]]
        for column_index in range(leading_entry_ij[0], column_size):
            matrix[row_index][column_index] = alpha * matrix[row_start_index][column_index] + matrix[row_index][column_index]



def perform_gauss_jordan(matrix, row_size, column_size):
    for rowNum in range(len(matrix)): 
        row_index = find_first_non_zero_column_element_row(matrix, row_size, column_size, rowNum)
        replace_selected_rows_in_matrix(matrix, row_index, rowNum)
        set_appropriate_leading_entry_for_row(matrix, rowNum)
        set_appropriate_elements_for_leading_entry_column(matrix, rowNum, row_size, column_size)
    
    for i in range(row_size):
        for j in range(column_size):
            print(matrix[i][j]),
        print('')            