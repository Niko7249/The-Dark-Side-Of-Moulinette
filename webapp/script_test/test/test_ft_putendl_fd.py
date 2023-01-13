import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette


libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
        
ft_putendl_fd = libft.ft_putendl_fd

test_path = os.path.join(Moulinette.TEST_FILEPATH + "/test1001.txt")

test_strings = ["02987549238573405934753408573409573409573405973405983", "983iubfd0q987f4u3bf03f87b2306t234ubf032hg730cv2304f23460fg\t\n\t", "C", "      C/niao come/n stai/n", ""]

ids = ["string: {}".format(t) for t in test_strings]
@pytest.mark.parametrize("test_string",test_strings, ids=ids)

def test_ft_putendl_fd(test_string):
    # Apri un file di test in scrittura
#    with open(str(test_path) + 'test2001.txt', 'wb') as f:
    with open(test_path, 'wb') as f:
        # Verifica che il file descriptor sia valido
        assert f.fileno() > 0

        s = test_string

        # Usa ft_putendl_fd per scrivere un carattere nel file
        result = ft_putendl_fd(s.encode('utf-8'), f.fileno())

    # Apri il file di test in lettura
    with open(test_path, 'rb') as f:
            # Verifica che il file contenga solo il carattere scritto
            assert f.read() == (s + '\n').encode('utf-8')
    if os.path.exists(test_path):
        os.remove(test_path)
    else:
        print("the file from test_ft_putendl_fd.py was NOT CREATED")
