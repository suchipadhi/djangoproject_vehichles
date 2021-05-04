FROM python:3.7
RUN apt-get update && apt-get install
RUN python -m pip install --upgrade pip

ENV PYTHONUNBUFFERED=1
RUN mkdir /vehicles
WORKDIR /vehicles/
COPY requirements.txt /vehicles/
RUN python -m pip install -r requirements.txt
COPY vehicles /vehicles/