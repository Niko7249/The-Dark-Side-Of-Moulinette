import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC

test_strings = ["ciao mondo", "", "    +-18329jchdbckjdhb", "ciao mondo               ", "ciao    \n mondo", "    -+18329234987298472904802498", "    + 18329234987298472904802498", "c"]
ids = ["input: '{}'".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string", test_strings, ids = ids)
def test_ft_strlen(test_string):
    # Define the function ft_strlen in the library
    ft_strlen = libft.ft_strlen

    # Define the strlen function in the library
    strlen = libc.strlen

    # Run the test
    result = ft_strlen(test_string)
    original_result = strlen(test_string)

    # Check that the results are equal
    assert result == original_result

