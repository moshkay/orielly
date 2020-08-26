FROM python:3.6.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get update


WORKDIR /code
COPY requirements.txt /code/


RUN pip install --upgrade pip

COPY . /code/
RUN pip install -r requirements.txt

EXPOSE 5001
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "oreilly.asgi:application"]

