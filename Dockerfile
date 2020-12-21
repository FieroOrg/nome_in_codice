FROM python:3

COPY src/ /app/src
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

WORKDIR /app/src
CMD [ "python", "./main.py" ]
