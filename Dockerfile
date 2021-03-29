FROM python:3-slim

RUN apt-get update && \
    apt-get install -y \
    gcc \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*
COPY src/ /app/src
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

WORKDIR /app/src
CMD [ "python", "./main.py" ]
