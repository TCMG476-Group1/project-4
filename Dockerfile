#Creating our Docker image using Python 3
FROM python:3

#Setting up the working directory to /api
WORKDIR /app

#Copying the current directory to
ADD . /app

#Getting the installbase ready
RUN pip install Flask
Run pip install requests

#Exposing the port 5000
EXPOSE 5000

#Launching api.py with the system startup
CMD ["python", "api.py"]
