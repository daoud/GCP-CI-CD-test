##FROM python:3.10-slim

#ENV APP_HOME /app
#WORKDIR $APP_HOME
#COPY . ./

#RUN pip install --no-cache-dir -r requirements.txt

#CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
#"""
####### new code#######
# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables for Cloud Run
ENV PYTHONUNBUFFERED=1
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/credentials.json"

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY main.py requirements.txt credentials.json ./ 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port from environment variable
# Cloud Run automatically assigns a port. We'll use it dynamically
EXPOSE ${PORT:-8080}

# Define the command to run the application
CMD ["python", "main.py"]
