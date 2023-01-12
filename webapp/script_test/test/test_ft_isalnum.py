import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC

test_strings = [99, 1, 999, 127, 50]

ids = ["input char: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_isalnum(test_string):
    # Define the function ft_isalnum in the library
    ft_isalnum = libft.ft_isalnum
    ft_isalnum.restype = ctypes.c_int
    ft_isalnum.argtypes = [ctypes.c_int]

    # Define the isalnum function in the library
    isalnum = libc.isalnum
    isalnum.restype = ctypes.c_int
    isalnum.argtypes = [ctypes.c_int]

    # Run the test
    result = ft_isalnum(test_string)
    original_result = isalnum(test_string)

    # Check that the results are equal
    assert result == original_result
