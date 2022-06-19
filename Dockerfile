# Pull base image
FROM python:3.9-alpine3.14
MAINTAINER Stepan Denisov <sd.denisoff@gmail.com>

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Install dependencies
RUN apk --update add postgresql-dev gcc python3-dev musl-dev make g++ zlib-dev
COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 80
