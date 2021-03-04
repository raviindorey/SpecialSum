FROM python:3.8

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

EXPOSE 5000

WORKDIR /code

COPY Pipfile Pipfile.lock /code/

RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install --dev --system

COPY . .