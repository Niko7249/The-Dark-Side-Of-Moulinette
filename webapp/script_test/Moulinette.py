from pytest_jsonreport.plugin import JSONReport
import pytest
import os
import sys
import ctypes
import ctypes.util

"""
library_path = os.path.join(str(app.new_filepath) + 'libft.so')
libft = ctypes.cdll.LoadLibrary('library_path')
libft_tester = ctypes.cdll.LoadLibrary('./lib/libft_tester.so')
libc = ctypes.cdll.LoadLibrary('./lib/libc.so.6')
libbsd = ctypes.cdll.LoadLibrary('./lib/libbsd.so.0.11.5')
"""
# Declaration of GLOBAL Variable, used for later.
LIBRARY_PATH = None
LIBFT = None
LIBFT_TESTER = None
libc = None
libbsd = None

def run_tests(new_filepath):
  global LIBRARY_PATH, libft,  libft_tester, libc, libbsd

  LIBRARY_PATH = os.path.join(str(new_filepath) + '/libft.so')
  LIBFT = ctypes.cdll.LoadLibrary(LIBRARY_PATH)
  LIBFT_TESTER = ctypes.cdll.LoadLibrary('./script_test/lib/libft_tester.so')
  lbc = ctypes.cdll.LoadLibrary('libc.so.6')
#  libbsd = ctypes.cdll.LoadLibrary('./script_test/lib/libbsd.so.0.11.5')
'''
path = './scriptsda_test/test/'
['FT_ISALPHA', path + 'test_ft_isalpha.py']
['FT_ISDIGIT', path + 'test_ft_isdigit.py']
['FT_ISALNUM', path + 'test_ft_isalnum.py']
['FT_ISASCII', path + 'test_ft_isascii.py']
['FT_ISPRINT', path + 'test_ft_isprint.py']
['FT_MEMCHR', path + 'test_ft_memchr.py']
['FT_MEMCMP', path + 'test_ft_memcmp.py']
['FT_MEMCPY', path + 'test_ft_memcpy.py']
['FT_MEMMOVE', path + 'test_ft_memmove.py']
['FT_MEMSET', path + 'test_ft_memset.py']
['FT_TOLOWER', path + 'test_ft_tolower.py']
['FT_TOUPPER', path + 'test_ft_toupper.py']
['FT_BZERO', path + 'test_ft_bzero.py']
['FT_ATOI', path + 'test_ft_atoi.py']
['FT_STRCHR', path + 'test_ft_strchr.py']
['FT_STRLEN', path + 'test_ft_strlen.py']
['FT_STRRCHR', path + 'test_ft_strrchr.py']
['FT_STRLCPY', path + 'test_ft_strlcpy.py']
['FT_STRLCAT', path + 'test_ft_strlcat.py']
['FT_CALLOC', path + 'test_ft_calloc.py']
['FT_STRDUP', path + 'test_ft_strdup.py']
['FT_SUBSTR', path + 'test_ft_substr.py']
['FT_STRJOIN', path + 'test_ft_strjoin.py']
['FT_STRTRIM', path + 'test_ft_strtrim.py']
['FT_ITOA', , path + 'test_ft_itoa.py']
['FT_STRNCMP', , path + 'test_ft_strncmp.py']
['FT_STRNSTR', , path + 'test_ft_strnstr.py']
['FT_SPLIT', , path + 'test_ft_split.py']
['FT_PUTCHAR_FD' , path + 'test_ft_putchar_fd.py']
['FT_PUTSTR_FD', , path + 'test_ft_putstr_fd.py']
['FT_PUTENDL_FD', , path + 'test_ft_putendl_fd.py']
['FT_PUTNBR_FD', , path + 'test_ft_putnbr_fd.py']
'''  
  # tests = [
  #   ('FT_ISALNUM', './script_test/test/test_ft_isalnum.py'),
  #   ('FT_ISALPHA', './script_test/test/test_ft_isalpha.py'),
  #   ('FT_ISDIGIT', './script_test/test/test_ft_isdigit.py'),
  #   ('FT_ISASCII', './script_test/test/test_ft_isascii.py'),
  #   ('FT_ISPRINT', './script_test/test/test_ft_isprint.py'),
  #   ('FT_TOLOWER', './script_test/test/test_ft_tolower.py') 
  # ]
  
  # for test in tests:
  #   print(test[0])
  #   plugin = JSONReport()
  #   pytest.main(['-v', '--tb=short', '--no-header', '--json-report-file=none', test[1]], plugins=[plugin])
  #   plugin.save_report(new_filepath + '/tmp/' + test[0] + '.json')

  plugin = JSONReport()
  print('FT_ISALNUM')
  pytest.main(['-v', '--tb=short', '--no-header', '--json-report-file=none', './script_test/test/test_ft_isalnum.py'], plugins = [plugin])
  plugin.save_report(new_filepath + '/tmp/' + 'FT_ISALPHA' + '.json')
  # print('FT_ISALPHA')
  # pytest.main(['-v', '--tb=short', '--no-header', '--json-report-file=none', './scrip_test/test/test_ft_isalpha.py'], plugins = [plugin])
  # plugin.save_report(new_filepath + '/tmp/' + 'FT_ISALPHA' + '.json')
  # print('FT_ISDIGIT')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_isdigit.py'])
  # print('FT_ISALNUM')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_isalnum.py'])
  # print('FT_ISASCII')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_isascii.py'])
  # print('FT_ISPRINT')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_isprint.py'])
  # # print('FT_MEMCHR')
  # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_memchr.py'])
  # # print('FT_MEMCMP')
  # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_memcmp.py'])
  # # print('FT_MEMCPY')
  # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_memcpy.py'])

  # # #LE FUNZIONI MEMMOVE VANNO IN SEGMANTTION FAULT ----> DA FIXARE

  # # # print('FT_MEMMOVE')
  # # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_memmove.py'])
  # # # print('FT_MEMSET')
  # # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_memset.py'])

  # # #LA FUNZIONE BZERO RESTITUISCE UN VALORE TOTALMENTE DIFFERENTE ---> DA FIXARE

  # # # print('FT_BZERO')
  # # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_bzero.py'])


  # # print('FT_ATOI')
  # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_atoi.py'])
  # # print('FT_STRCHR')
  # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_strchr.py'])
  # # print('FT_STRLEN')
  # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_strlen.py'])
  # # print('FT_STRRCHR')
  # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_strrchr.py'])
  # print('FT_TOLOWER')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_tolower.py'])
  # # print('FT_TOUPPER')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_toupper.py'])

  # #LE FUNZIONI CALLOC E STRDUP RESTITUISCO GLI INDIRIZZI DI MEMORIA ---> FIXARE UTILIZZANDO PRINTF PER VEDERE IL RISULTATO

  # # print('FT_CALLOC')
  # # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_calloc.py'])
  # print('FT_STRDUP')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_strdup.py'])
  # print('FT_SUBSTR')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_substr.py'])
  # print('FT_STRJOIN')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_strjoin.py'])
  # print('FT_STRTRIM')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_strtrim.py'])
  # print('FT_ITOA')
  # pytest.main(['-v', '--tb=short', '--no-header', './script_test/test/test_ft_itoa.py'])


# gcc -shared -o libft.so *.o


if __name__ == '__main__':
  run_tests()
