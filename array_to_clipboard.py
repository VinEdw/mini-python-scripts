# Array to clipboard

import pyperclip as pc

def array_to_string(arr):
    return_str = ''
    for row in arr:
        row_str = ''
        for cell in row:
            row_str += str(cell) + '\t'
        return_str += row_str[:-1] + '\n'
    return return_str

def copy_array(arr):
    arr_str = array_to_string(arr)
    pc.copy(arr_str)