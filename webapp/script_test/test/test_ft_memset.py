import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC

test_dests = ["ucococsdicja989 9888     \n\n\n\n\t\t\t\n\t\n ", "wouihdosijdaIUHSiuha9889a8YA9ha98", "ciao", "ciao  ", ""]
test_int = [ord('\t'), 66, 99, 66, 0]
test_sizes = [len(test_dests[0]), len(test_dests[1]), len(test_dests[2]), len(test_dests[3]), len(test_dests[4])]

test_data = [(test_dests[0], test_int[0], test_sizes[0]), 
             (test_dests[1], test_int[1], test_sizes[1]), 
             (test_dests[2], test_int[2], test_sizes[2]), 
             (test_dests[3], test_int[3], test_sizes[3]), 
             (test_dests[4], test_int[4], test_sizes[4])]

ids = ["string: {}, char (in int):{}".format(t[0], t[1]) for t in test_data]
@pytest.mark.parametrize("test_dest, test_string2, test_size",test_data, ids=ids)

def test_ft_memset(test_dest, test_string2, test_size):

    # Definizione della funzione ft_memset nella libreria
    ft_memset = libft.ft_memset

    # Define the memset function in the library
    memset = libc.memset

    result = print(ft_memset(test_dest, test_string2, test_size))
    
    # chiamare la funzione originale con i dati di input
    original_result = print(memset(test_dest, test_string2, test_size))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result
