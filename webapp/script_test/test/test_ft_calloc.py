import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC


SIZE_MAX = sys.maxsize
SIZE_MAX = ctypes.c_size_t(-1).value

test_data = [[2, 6], [21, 63], [20, 0], [0, 0], [0, ctypes.sizeof(ctypes.c_int)], [SIZE_MAX // ctypes.sizeof(ctypes.c_int) + 1, ctypes.sizeof(ctypes.c_int)]]
ids = ["num_element: {}, element_size: {}".format(t[0], t[1]) for t in test_data]
@pytest.mark.parametrize("num_element, element_size", test_data, ids = ids)

def test_ft_calloc(num_element, element_size):
    # Define the function ft_calloc in the library
    ft_calloc = libft.ft_calloc
    ft_calloc.restype = ctypes.c_void_p

    # Define the calloc function in the library
    calloc = libc.calloc
    calloc.restype = ctypes.c_void_p

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert ctypes.string_at(ft_calloc(num_element, element_size), num_element* element_size) == ctypes.string_at(calloc(num_element, element_size), num_element * element_size)
    
