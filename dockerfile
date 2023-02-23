#specify the base image you want to use
FROM python:3.9-alpine

#Install any required dependencies for your Django application. 
#For example, you can install Django and any other required packages using pip:
RUN pip install Django
RUN pip install requests

#Copy your Django code into the Docker image.
#Copy the entire project directory into the image:
COPY . /furniture_app


#Set the working directory for the Docker image to the root directory of your Django project:
WORKDIR /furniture_app


#Expose the port that your Django application will be running on.
#For example, you can expose port 8000:
EXPOSE 8001

#Specify the command that will start your Django application.
#For example, you can start the Django development server:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]