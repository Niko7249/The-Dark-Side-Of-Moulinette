import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
        
ft_putnbr_fd = libft.ft_putnbr_fd

test_ints = [123456789, -127849, 0, -2147483648, -21474836]

ids = ["int: {}".format(t) for t in test_ints]
@pytest.mark.parametrize("test_int",test_ints, ids=ids)

def test_ft_putnbr_fd(test_int):
    # Apri un file di test in scrittura
    with open('test3001.txt', 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        nb = test_int

        # Usa ft_putnbr_fd per scrivere un carattere nel file
        result = ft_putnbr_fd(nb, f.fileno())

    # Apri il file di test in lettura
    with open('test3001.txt', 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == str(nb).encode('utf-8')
