# Makefile

NAME = libft.a

CC = gcc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f


SRCS		= 	*.c \


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
