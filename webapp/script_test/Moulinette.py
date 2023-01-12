import pytest
import os
import sys
import ctypes
import ctypes.util
import subprocess
from pytest_jsonreport.plugin import JSONReport


# Declaration of GLOBAL Variable, used for later.
LIBRARY_PATH = None
LIBFT = None
LIBFT_TESTER = None
LIBC = None
LIBBSD = None


def run_tests(new_filepath):
  global LIBRARY_PATH, LIBFT,  LIBFT_TESTER, LIBC, LIBBSD

  LIBRARY_PATH = os.path.join(str(new_filepath) + '/libft.so')
  LIBFT = ctypes.cdll.LoadLibrary(LIBRARY_PATH)
  LIBFT_TESTER = ctypes.cdll.LoadLibrary('./script_test/lib/libft_tester.so')
  LIBC = ctypes.cdll.LoadLibrary('libc.so.6')
  LIBBSD = ctypes.cdll.LoadLibrary('/../usr/lib/libbsd.so.0')

  path = './script_test/test/'
  tests = [
    ('FT_ISALPHA', path + 'test_ft_isalpha.py'),
    ('FT_ISDIGIT', path + 'test_ft_isdigit.py'),
    ('FT_ISALNUM', path + 'test_ft_isalnum.py'),
    ('FT_ISASCII', path + 'test_ft_isascii.py'),
    ('FT_ISPRINT', path + 'test_ft_isprint.py'),
    ('FT_MEMCHR', path + 'test_ft_memchr.py'),
    ('FT_MEMCMP', path + 'test_ft_memcmp.py'),
    ('FT_MEMCPY', path + 'test_ft_memcpy.py'),
    ('FT_MEMMOVE', path + 'test_ft_memmove.py'),
    ('FT_MEMSET', path + 'test_ft_memset.py'),
    ('FT_TOLOWER', path + 'test_ft_tolower.py'),
    ('FT_TOUPPER', path + 'test_ft_toupper.py'),
    #('FT_BZERO', path + 'test_ft_bzero.py'),
    ('FT_ATOI', path + 'test_ft_atoi.py'),
    ('FT_STRCHR', path + 'test_ft_strchr.py'),
    ('FT_STRLEN', path + 'test_ft_strlen.py'),
    ('FT_STRRCHR', path + 'test_ft_strrchr.py'),
    ('FT_STRLCPY', path + 'test_ft_strlcpy.py'),
    ('FT_STRLCAT', path + 'test_ft_strlcat.py'),
    ('FT_CALLOC', path + 'test_ft_calloc.py'),
    #('FT_STRDUP', path + 'test_ft_strdup.py'),
    #('FT_SUBSTR', path + 'test_ft_substr.py'),
    #('FT_STRJOIN', path + 'test_ft_strjoin.py'),
    #('FT_STRTRIM', path + 'test_ft_strtrim.py'),
    #('FT_ITOA', path + 'test_ft_itoa.py'),
    #('FT_STRNCMP', path + 'test_ft_strncmp.py'),
    #('FT_STRNSTR', path + 'test_ft_strnstr.py'),
    #('FT_SPLIT', path + 'test_ft_split.py'),
    ('FT_PUTCHAR_FD', path + 'test_ft_putchar_fd.py'),
    ('FT_PUTSTR_FD', path + 'test_ft_putstr_fd.py'),
    ('FT_PUTENDL_FD', path + 'test_ft_putendl_fd.py'),
    ('FT_PUTNBR_FD', path + 'test_ft_putnbr_fd.py')
   ]
  
  for test in tests:
    print(test[0])
    plugin = JSONReport()
    pytest.main(['-v', '--tb=short', '--no-header', '--json-report-file=none', test[1]], plugins=[plugin])
    plugin.save_report(new_filepath + '/tmp/' + test[0] + '.json')
