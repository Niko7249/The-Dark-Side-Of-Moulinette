# start by pulling the python image
FROM python:3.10-alpine

# copy the requirements file into the image
COPY ./requirements..txt /app/requirements.txt

# switch working directory
WORDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content ffrom the local file to the image
COPY . /app

# configure the container to run in nan executed manner
ENTRYPOINT ["python"]

CMD["app.y"]