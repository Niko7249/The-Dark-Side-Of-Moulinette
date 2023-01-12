import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC

test_strings = [99, 48, 56, 127, 0]

ids = ["input char: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_isdigit(test_string):
    # Define the function ft_isdigit in the library
    ft_isdigit = libft.ft_isdigit
    ft_isdigit.restype = ctypes.c_int
    ft_isdigit.argtypes = [ctypes.c_int]

    # Define the isdigit function in the library
    isdigit = libc.isdigit
    isdigit.restype = ctypes.c_int
    isdigit.argtypes = [ctypes.c_int]

    # Run the test
    result = ft_isdigit(test_string)
    original_result = isdigit(test_string)

    # Check that the results are equal
    assert result == original_result
