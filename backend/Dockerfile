# CVXPY + Backend Docker image scaffolding appropriated from https://github.com/mariohsouto/cvxpy_docker

# Official Python 3.7.7 Docker image based off of Debian Buster in its slim variant
FROM python:3.7.7-slim-buster

# Set a working directory inside your container to control where commands are run
WORKDIR /usr/src/app

# Install backend dependencies necessary to compile SCS and other solvers
RUN apt-get update && apt-get install -y build-essential g++ libgl1-mesa-glx libx11-6

# Install Python packages
RUN python -m pip install \
        numpy \
        cvxpy \
		json \
		requests

