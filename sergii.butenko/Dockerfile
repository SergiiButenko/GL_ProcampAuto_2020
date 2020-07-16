FROM python:3.8-slim
EXPOSE 5002
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["python", "./simple-app.py"]

