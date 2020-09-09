FROM python:3.8.3-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /code /code/static /code/media
RUN apk update && apk add libressl-dev musl-dev libffi-dev postgresql-dev gcc python3-dev musl-dev
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./src/ /code/
