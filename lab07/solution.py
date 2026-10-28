from numpy import *
def reshape_rows(values, width):
    if len(values)%width == 0:
        return array(values).reshape(len(values)//width, width).tolist()
    else:
        return []
    
def block(matrix, rows, columns):
    return matrix[ix_(rows, columns)].tolist()

def column_means(matrix):
    if len(matrix) == 0:
        return []
    else:
        return round(mean(matrix, axis=0), 6).tolist()
    
def column_range(matrix, column):
    if len(matrix) == 0:
        return []
    else:
        return ptp(matrix[:, column]).tolist()