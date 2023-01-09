# The Dark Side of Moulinette

## Requirements
   Python >= 3.10.6
   Python pip
   Python venv
   Docker (just for the production stage)

This is some usefull commands for working with python virtual environments.
```bash
#create a new virtual environment inside the project you are working to.
python3 -m venv venv

#start the virtual environment.
source venv/bin/activate
```

This is some usefull commands for working with docker.
Please see the Docker documentation for install and other stuff.

#first of all you'll need a Dockerfile inside the repo you want to Dockerize.
here is an example of how it should be
```bash
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
```

```bash
#show the list of currently running docker container
sudo docker container ps

#show the list of the history docker container runned.
sudo docker container ps -a

#create a docker image
sudo docker image build -t <dir_name>

#run a docker container using port 5000 into port 5000. (test only)
sudo docker run -p 5000:5000 -d <dir_name>
```

Contributors:
Vale and Nico
