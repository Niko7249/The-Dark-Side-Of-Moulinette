// HEADER FILE.
//ADD 42 HEADER

#ifndef LIBFT_H

#define LIBFT_H

#include<stdlib.h>    //malloc
#include<unistd.h>    //write
#include<stdio.h>     //TO DELETE
#include<ctype.h>     //TO DELETE
#include<string.h>    //TO DELETE
#include<strings.h>   //TO DELETE
#include<assert.h>    //TO DELETE -- *ft_memchr


int ft_isalpha(int c);
int ft_isdigit(int c);
int ft_isalnum(int c);
int ft_isascii(int c);
int ft_isprint(int c);
int ft_tolower(int c);

#endif
