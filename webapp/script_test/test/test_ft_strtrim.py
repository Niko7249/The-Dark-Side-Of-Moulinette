import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libft_tester = Moulinette.LIBFT_TESTER

test_strings1 = ["   Ciao   ", " ciao Vaffanculo ciao    ", "vaffancul", "", ""]
test_toattachs = ["C ", " ciao", "_ciao", "vjdnvkjdfnvkjnksdfjdskfjsdf", ""]

test_data = [(test_strings1[0], test_toattachs[0]), 
             (test_strings1[1], test_toattachs[1]), 
             (test_strings1[2], test_toattachs[2]), 
             (test_strings1[3], test_toattachs[3]), 
             (test_strings1[4], test_toattachs[4])]

ids = ["string: '{}', to_trim: '{}'".format(t[0], t[1]) for t in test_data]
@pytest.mark.parametrize("test_string, test_toattach",test_data, ids=ids)

def test_ft_strtrim(test_string, test_toattach):

    test_string_buffer = ctypes.create_string_buffer(test_string.encode())
    test_string_buffer2 = ctypes.create_string_buffer(test_toattach.encode())
    
    # Definizione della funzione ft_strtrim nella libreria
    ft_strtrim = libft.ft_strtrim

    # Define the strtrim function in the library
    strtrim = libft_tester.strtrim

    result = ctypes.string_at(ft_strtrim(test_string_buffer, test_string_buffer2))
    
    # chiamare la funzione originale con i dati di input
    original_result = ctypes.string_at(strtrim(test_string_buffer, test_string_buffer2))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
