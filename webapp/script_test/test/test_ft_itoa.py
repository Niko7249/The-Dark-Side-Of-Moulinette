import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libft_tester = Moulinette.LIBFT_TESTER

test_ints = [4359, 43595, -4385309, -34658342, 0, -2147483648]

ids = ["input: '{}'".format(t) for t in test_ints]
@pytest.mark.parametrize("test_int", test_ints, ids = ids)

def test_ft_itoa(test_int):
    # Define the function ft_itoa in the library
    ft_itoa = libft.ft_itoa

    # Define the itoa function in the library
    itoa = libft_tester.itoa

    test_string_buffer = ctypes.create_string_buffer(ft_itoa(test_int))
    test_string_buffer2 = ctypes.create_string_buffer(itoa(test_int))

    # chiamare la funzione custom con i dati di input    
    result = ctypes.string_at(ft_itoa(test_int))
 
    # chiamare la funzione originale con i dati di input   
    original_result = ctypes.string_at(itoa(test_int))
    
    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
