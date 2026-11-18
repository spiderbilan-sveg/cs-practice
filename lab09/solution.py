import numpy as np

def make_hours():
    return np.arange(0, 22, 3).tolist()

def vector_report(values):
    return {
        "third": values[2], 
        "last": values[-1], 
        "middle": values[2:6], 
        "every_second": values[::2], 
        "reversed": values[::-1]
        }    
    
def change_vector(values):
    val = np.copy(values)
    val[2:4] = 99
    val[::2] = -1
    return [float(i) for i in val]

def cap_above(values, limit):
    arr = np.asarray(values, dtype = float).copy()
    mask = arr > limit
    arr[mask] = limit
    return arr.tolist()

def celsius_to_fahrenheit(values):
    return (np.asarray(values, dtype=float) * 9 / 5 + 32).tolist()
