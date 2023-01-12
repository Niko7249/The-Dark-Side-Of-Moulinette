# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# install make	
RUN apk add --update make

#install gcc
RUN apk add gcc
	
# install unistd.h and other C libraries
RUN apk add --no-cache musl-dev

#install emacs	
RUN apk add emacs

#install libbsd
RUN apk add --upgrade libbsd

# copy every content from the local file to the image
COPY . /app

# configure the container to run in nan executed manner
ENTRYPOINT ["python"]

CMD ["app.py"]