import ctypes
import os
import sys
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC

test_strings = ["    +18329jchdbckjdhb", "    -18329jchdbckjdhb", "    +-18329jchdbckjdhb", "    +18329234987298472904802498", "    -18329234987298472904802498", "    -+18329234987298472904802498", ""]
ids = ["input: '{}'".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string", test_strings, ids = ids)
def test_ft_atoi(test_string):
    # Define the function ft_atoi in the library
    ft_atoi = libft.ft_atoi

    # Define the atoi function in the library
    atoi = libc.atoi

    # Run the test
    result = ft_atoi(test_string)
    original_result = atoi(test_string)

    # Check that the results are equal
    assert result == original_result
