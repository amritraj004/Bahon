# Use an official Python runtime as a base image (os: alpine linux)
FROM python:3.6.1-alpine

# Add requirements.txt before rest of repo, for Docker caching purposes
# See http://ilikestuffblog.com/2014/01/06/
ADD requirements.txt /app/

# Set the working directory to /app
WORKDIR app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app

# Define environment variable
ENV NAME Bahon_Web
