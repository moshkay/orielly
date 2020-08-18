FROM python:3.6.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get update


WORKDIR /code
COPY requirements.txt /code/


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/
RUN pip install -r requirements.txt

EXPOSE 5001


