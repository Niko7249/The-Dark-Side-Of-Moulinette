import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC

test_strings = [90, 68, 48, 32, 102]

ids = ["input char: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_tolower(test_string):
    # Define the function ft_tolower in the library
    ft_tolower = libft.ft_tolower
    ft_tolower.restype = ctypes.c_int
    ft_tolower.argtypes = [ctypes.c_int]

    # Define the tolower function in the library
    tolower = libc.tolower
    tolower.restype = ctypes.c_int
    tolower.argtypes = [ctypes.c_int]

    # Run the test
    result = ft_tolower(test_string)
    original_result = tolower(test_string)

    # Check that the results are equal
    assert result == original_result
