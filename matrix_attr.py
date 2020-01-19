rows = []
columns = []
matrix = []

def setRows(matrix_str): 
    _matrix_rows = matrix_str.split('\n')
    for _row in _matrix_rows:
        row = _row.split(' ')
        rows.append([int(element) for element in row])    

def setColumns(matrix_str):
    for column in range(len(rows[0])):
        col = []
        for row in rows:
            col.append(row[column])
        columns.append(col)

def setMatrix(matrix_str):
    _matrix_rows = matrix_str.split('\n')
    for _row in _matrix_rows:
        row = _row.split(' ')
        matrix.append([int(element) for element in row])  