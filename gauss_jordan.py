from matrix_attr import get_leading_entry_from_row

def perform_gauss_jordan(matrix, row_size, column_size):
    for current_row_index in range(row_size): 
        row_index = find_first_non_zero_column_element_row(matrix, row_size, column_size, current_row_index)
        replace_selected_rows_in_matrix(matrix, current_row_index, row_index)
        set_appropriate_leading_entry_for_row(matrix, current_row_index)
        set_appropriate_elements_for_leading_entry_column(matrix, current_row_index, row_size, column_size, downward= True)
    # to have reduced matrix    
    for current_row_index in range(row_size-1, 0, -1):
        set_appropriate_elements_for_leading_entry_column(matrix, current_row_index, row_size, column_size, downward= False)

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

def set_appropriate_elements_for_leading_entry_column(matrix, row_start_index, row_size, column_size, downward): 
    leading_entry_ij = get_leading_entry_from_row(row_start_index)

    if downward:
        row_range = range(row_start_index+1, row_size)
    else:    
        row_range = range(row_start_index-1, -1, -1)

    for row_index in row_range:
        alpha = -1 * (float)(matrix[row_index][leading_entry_ij[1]]) / matrix[leading_entry_ij[0]][leading_entry_ij[1]]
        for column_index in range(leading_entry_ij[0], column_size):
            matrix[row_index][column_index] = alpha * matrix[row_start_index][column_index] + matrix[row_index][column_index]
