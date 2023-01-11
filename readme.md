# The Dark Side of Moulinette

## Requirements
* Python >= 3.10
* Python pip
* Python venv
* for the other python package check the requirements txt file
* Docker (just for the deployment stage)
-------------------------------------------------------------------------------
## Python virtual environment
This is some usefull commands for working with python virtual environments.
```bash
#create a new virtual environment inside the project you are working to.
python3 -m venv venv

#start the virtual environment.
source venv/bin/activate
```
-------------------------------------------------------------------------------
## Dockerfile config
Dockerfile example of configuration.
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
-------------------------------------------------------------------------------
## Docker commands
Please see the Docker documentation for install and other stuff.
```bash
#show the list of currently running docker container
sudo docker container ps

#show the list of the history docker container runned.
sudo docker container ps -a

#create a docker image
sudo docker image build -t <dir_name>

#run a docker container using port 5000 into port 5000.
sudo docker run -p 5000:5000 -d <dir_name>

#restart a docker run
sudo docker restar <container_ID>
```
-------------------------------------------------------------------------------
## Nginx config docker setup

The last step to run our application is to add a rule to our nginx conf file.
This will give us the ability to create a reverse proxy between our application
which is running in a localhost (inside the server) and our site which is public.

```
location <url> {
	proxy_set_header X-Real-IP $remote_addr;
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_set_header Host $host;
	proxy_set_header X-NginX-Proxy true;

	proxy_pass http://localhost:<port_number>/;
	proxy_redirect http://localhost:<port_number>/ https://$server_name/;
}

# this is an example of configuration that uses port number 4242 and point to the url called "asd"

location /asd/ {
	proxy_set_header X-Real-IP $remote_addr;
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	proxy_set_header Host $host;
	proxy_set_header X-NginX-Proxy true;

	proxy_pass http://localhost:4242/;
	proxy_redirect http://localhost:4242/ https://$server_name/;
}

```
-------------------------------------------------------------------------------
### Contributors:
| *Valerio pescetelli* |
| *Marco Coppola*      |
| *Nicolò Tamiano*     |
