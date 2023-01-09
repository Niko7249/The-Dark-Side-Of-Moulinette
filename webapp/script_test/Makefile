# # Makefile

# cc = gcc

# flags = -Wall -Wextra -Werror -o

# rm = rm -f

# name_exe = libft.a

# source_files = ft_atoi.c ft_isalnum.c ft_isdigit.c ft_strchr.c ft_strlcpy.c ft_strnstr.c ft_toupper.c ft_bzero.c ft_isalpha.c ft_isprint.c ft_strdup.c ft_strlen.c ft_strrchr.c ft_calloc.c ft_isascii.c ft_memset.c ft_strlcat.c ft_strncmp.c ft_tolower.c ft_memchr.c ft_memcmp.c ft_memcpy.c ft_memmove.c

# object_files = $(source_files:%.c=.o)

# all: $(name_exe)
# 	$(cc) $(source_files) $(flags) $(name_exe)

# clean:
# 	$(rm) $(object_file) #delete all object files

# fclean: clean
# 	$(rm) $(name_exe) #calls for clean and remove even the exe.

# re: fclean all

# .PHONY: all clean fclean re #Needs for calling the options trough the terminal

NAME = libft.a

CC = gcc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f


SRCS		= 	ft_isalnum.c \
			ft_isdigit.c \
			ft_isalpha.c \
			ft_isprint.c \
			ft_isascii.c \
			ft_tolower.c \


OBJS		= ${SRCS:.c=.o}

BONUS		=	ft_lstadd_back.c ft_lstadd_front.c ft_lstclear.c\
				ft_lstdelone.c ft_lstiter.c ft_lstlast.c\
				ft_lstnew.c ft_lstsize.c ft_lstmap.c\

BONUS_OBJS	= ${BONUS:.c=.o}

CC			= gcc

RM			= rm -f

CFLAGS		= -Wall -Wextra -Werror

NAME = libft.a

all:		${NAME}

$(NAME):	${OBJS}
			ar rc ${NAME} ${OBJS}

clean:
			${RM} ${OBJS} ${BONUS_OBJS}

fclean:		clean
			${RM} ${NAME}

re:			fclean ${NAME}

bonus:		${BONUS_OBJS}
			ar rc ${NAME} ${BONUS_OBJS}
