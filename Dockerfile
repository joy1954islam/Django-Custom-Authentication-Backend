FROM python:3.11
ENV PYTHONUNBUFFERED 1

ENV LIBRARY_PATH=/lib:/usr/lib
RUN mkdir /code
WORKDIR /code
RUN mkdir /code/static
RUN mkdir /code/media
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

