# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
ENV APP_HOME /app
WORKDIR $APP_HOME

# Copy the machine learning model and API code 

COPY model $APP_HOME/model
COPY service $APP_HOME/service
COPY src $APP_HOME/src
COPY uploads $APP_HOME/uploads
COPY server.py .
COPY app.py .
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run the API with Gunicorn
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 server:app
