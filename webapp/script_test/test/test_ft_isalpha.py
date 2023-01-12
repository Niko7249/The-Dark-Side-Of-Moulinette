import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC

test_strings = [67, 12, 102, 70, 0]

ids = ["input char: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_isalpha(test_string):
    # Define the function ft_isalpha in the library
    ft_isalpha = libft.ft_isalpha
    ft_isalpha.restype = ctypes.c_int
    ft_isalpha.argtypes = [ctypes.c_int]

    # Define the isalpha function in the library
    isalpha = libc.isalpha
    isalpha.restype = ctypes.c_int
    isalpha.argtypes = [ctypes.c_int]

    # Run the test
    result = ft_isalpha(test_string)
    original_result = isalpha(test_string)

    # Check that the results are equal
    assert result == original_result
