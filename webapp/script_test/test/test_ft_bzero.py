import ctypes
import os
import sys
import pytest
sys.path.append('./../.')
import Moulinette

libft = ctypes.cdll.LoadLibrary(Moulinette.LIBRARY_PATH)
libc = Moulinette.LIBC

try:
  def test1_ft_bzero():
    # Test input di esempio
    input = [0, 1, 2, 3, 4]
  
    # Definisci le funzioni ft_bzero e bzero
    ft_bzero = libft.ft_bzero
    bzero = libc.bzero
    
    input_ptr = ctypes.c_void_p(id(input))

    # Verifica che l'output delle funzioni sia corretto
    assert ft_bzero(input_ptr, len(input)) == bzero(input_ptr, len(input))
except Exception as e:
  print(e)
  
  

def test2_ft_bzero():
  # Test input di esempio
  input = [0]
  
  # Definisci le funzioni ft_bzero e bzero
  ft_bzero = libft.ft_bzero
  bzero = libc.bzero

  input_ptr = ctypes.c_void_p(id(input))

  # Verifica che l'output delle funzioni sia corretto
  assert ft_bzero(input_ptr, len(input)) == bzero(input_ptr, len(input))

def test3_ft_bzero():
  # Test input di esempio
  input = [1, 1, 4, 3, 4, 1, 2, 4]
  
  # Definisci le funzioni ft_bzero e bzero
  ft_bzero = libft.ft_bzero
  bzero = libc.bzero

  input_ptr = ctypes.c_void_p(id(input))

  # Verifica che l'output delle funzioni sia corretto
  assert ft_bzero(input_ptr, len(input)) == bzero(input_ptr, len(input))

def test4_ft_bzero():
  # Test input di esempio
  input = []
  
  # Definisci le funzioni ft_bzero e bzero
  ft_bzero = libft.ft_bzero
  bzero = libc.bzero

  input_ptr = ctypes.c_void_p(id(input))

  # Verifica che l'output delle funzioni sia corretto
  assert ft_bzero(input_ptr, len(input)) == bzero(input_ptr, len(input))

def test5_ft_bzero():
  # Test input di esempio
  input = [0, 1, 2, 3, 4, 'c']
  
  # Definisci le funzioni ft_bzero e bzero
  ft_bzero = libft.ft_bzero
  bzero = libc.bzero

  input_ptr = ctypes.c_void_p(id(input))

  # Verifica che l'output delle funzioni sia corretto
  assert ft_bzero(input_ptr, len(input)) == bzero(input_ptr, len(input))
