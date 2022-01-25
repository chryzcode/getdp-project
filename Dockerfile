# pull base image
FROM python:3.9.5

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set working directory
WORKDIR /getdp-project

#install pipfile requirements dependencies
COPY Pipfile Pipfile.lock /getdp-project/
RUN pip install pipenv && pipenv install --system


# Copy project
COPY . /getdp-project/