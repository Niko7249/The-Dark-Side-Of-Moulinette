import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libbsd = Moulinette.LIBBSD

test_dests = [ctypes.create_string_buffer(b'\0' * 20)]
test_strings2 = [b"1234567890", b"ciaocomeva", b"", b"         \n"]
test_sizes = [20, 5, 15, 1]

test_data = [(test_dests[0], test_strings2[0], test_sizes[0]), 
             (test_dests[0], test_strings2[1], test_sizes[1]), 
             (test_dests[0], test_strings2[2], test_sizes[2]), 
             (test_dests[0], test_strings2[3], test_sizes[3])]

ids = ["string: {}, size:{}".format(t[1], t[2]) for t in test_data]
@pytest.mark.parametrize("test_dest, test_string2, test_size",test_data, ids=ids)

def test_ft_strlcpy(test_dest, test_string2, test_size):

    # Definizione della funzione ft_strlcpy nella libreria
    ft_strlcpy = libft.ft_strlcpy

    # Define the strlcpy function in the library
    strlcpy = libbsd.strlcpy

    result = ft_strlcpy(test_dest, test_string2, test_size)
    
    # chiamare la funzione originale con i dati di input
    original_result = strlcpy(test_dest, test_string2, test_size)

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
