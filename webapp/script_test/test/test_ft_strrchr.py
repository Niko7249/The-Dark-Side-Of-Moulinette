import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC

test_data = [
    ["hello world", ord('w')],
    ["hello world", ord('z')],
    ["", ord('a')],
    ["\x00hello world", ord('\x00')],
    ["", ord('h')]
]

@pytest.mark.parametrize("test_src, test_char",test_data, ids=[f"string: {t[0]}, char:{chr(t[1])}" for t in test_data])
def test_ft_strrchr(test_src, test_char):
    ft_strrchr = libft.ft_strrchr
    strrchr = libc.strrchr

    test_src = bytes(test_src, 'utf-8')
    
    result = print(ft_strrchr(test_src, test_char))
    original_result = print(strrchr(test_src, test_char))

    # verificare che il risultato ottenuto sia uguale al risultato della funzione originale
    assert result == original_result 
