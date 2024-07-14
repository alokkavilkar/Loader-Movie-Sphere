FROM python:3.9-alpine3.17
LABEL maintainer = "alokkavilkar"
LABEL description ="Dockerfile for artifact from loader microservice."

WORKDIR /app

COPY requirements.txt /app/
COPY loader.py /app/
COPY movies.json /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "loader.py"]



