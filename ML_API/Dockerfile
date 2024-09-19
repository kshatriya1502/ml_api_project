#This sets up the container with python 3.10
FROM python:3.10-slim


#this copies everything in the Dockerfile directory to /app directory in the container : 
COPY . /app

#change working dir :
WORKDIR /app

#installing the dependencies
RUN pip install -r requirements.txt

#exposing port 80  : port at which our FastApi is running 
EXPOSE 80

#command to run 
CMD ["uvicorn" , "ml_api:app","--host","0.0.0.0" , "--port" , "80"]
