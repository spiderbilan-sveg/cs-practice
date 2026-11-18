import numpy as np

def make_hours():
    return np.arange(0, 21, 3, dtype=float)

def vector_report(values):
    val = np.array(values)
    return {
        "third": val[2], 
        "last": val[-1], 
        "middle": val[2:6], 
        "every_second": val[::2], 
        "reversed": val[::-1]
        }    
    
def change_vector(values):
    val = np.copy(values)
    val[1:4] = 99
    val[::2] = -1
    return val

def cap_above(values, limit):
    arr = np.asarray(values, dtype = float).copy()
    mask = arr > limit
    arr[mask] = limit
    return arr.tolist()

def celsius_to_fahrenheit(values):
    return (np.asarray(values, dtype=float) * 9 / 5 + 32).tolist()