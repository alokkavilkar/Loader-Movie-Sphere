FROM python:3.7.3
LABEL maintainer = "alokkavilkar"
LABEL description ="Dockerfile for artifact from loader microservice."

WORKDIR /app

COPY requirements.txt /app/
COPY loader.py /app/
COPY movies.json /app/

RUN pip install --no-cache-dir -r requirements.txt && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    sudo ./aws/install 



