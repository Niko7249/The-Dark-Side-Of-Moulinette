import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC

test_strings = [99, 127, 102, 70, 0]

ids = ["input char: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_isascii(test_string):
    # Define the function ft_isascii in the library
    ft_isascii = libft.ft_isascii
    ft_isascii.restype = ctypes.c_int
    ft_isascii.argtypes = [ctypes.c_int]

    # Define the isascii function in the library
    isascii = libc.isascii
    isascii.restype = ctypes.c_int
    isascii.argtypes = [ctypes.c_int]

    # Run the test
    result = ft_isascii(test_string)
    original_result = isascii(test_string)

    # Check that the results are equal
    assert result == original_result
