FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get -y install libpq-dev ffmpeg gcc

RUN pip install --upgrade pip && \
    pip install poetry

WORKDIR /FastAPI_project

COPY . .

RUN poetry config virtualenvs.create false && \
    poetry install --only main

WORKDIR /FastAPI_project/App
