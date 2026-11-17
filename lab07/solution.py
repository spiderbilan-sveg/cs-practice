from numpy import *


def reshape_rows(values, width):
    if len(values) % width == 0:
        return array(values).reshape(len(values) // width, width).tolist()
    else:
        return []


def block(matrix, rows, columns):
    if not matrix:
        return []
    
    arr = asarray(matrix, dtype=float)
    
    selected = arr[ix_(rows, columns)]
    return selected.tolist()


def column_means(matrix):
    if not matrix:
        return []
    
    return round(mean(matrix, axis=0), 6).tolist()

def column_range(matrix, column):
    if not matrix:
        return 0.0
    
    arr = asarray(matrix, dtype=float)
    col_data = arr[:, column]
    rng = max(col_data) - min(col_data)
    return round(float(rng), 6)
