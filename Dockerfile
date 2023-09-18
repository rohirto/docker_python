# Use an official Python base image
FROM python:3.9-slim-buster

# Install debugging tools (pdb and ptvsd for VS Code)
RUN pip install ptvsd

# Install Git
RUN apt-get update && apt-get install -y git

# Install libraries
# Data Processing
RUN pip install matplotlib
RUN pip install tensorflow
RUN pip install numpy 
RUN pip install opencv-python
RUN pip install cvlib
# Web related
RUN pip install django

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# Set the working directory inside the container
WORKDIR /workspace

# Copy your Python code and project files into the container
# If you have a project directory on your host, you can use a bind mount instead
# COPY . /workspace

# Expose port 5678 for remote debugging
EXPOSE 5678

# Entry point to keep the container running
CMD ["tail", "-f", "/dev/null"]