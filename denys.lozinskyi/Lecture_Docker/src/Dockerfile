FROM python:3.7-slim
EXPOSE 5002

WORKDIR /app

COPY requirements .
RUN pip install -r requirements

COPY . .

ENTRYPOINT [ "python", "./simple-app-v2.py" ]