FROM python:3.7-slim

WORKDIR /app

COPY requirements .
RUN pip3 install -r requirements

COPY . /app/

ENTRYPOINT [ "python3", "/app/src/server/simple-app-v2.py" ]
