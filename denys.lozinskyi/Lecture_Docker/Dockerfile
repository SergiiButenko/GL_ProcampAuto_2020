FROM python:3.7-slim

WORKDIR /app

VOLUME /logs

COPY requirements .
RUN pip3 install -r requirements

COPY . .

ENTRYPOINT [ "python3", "src/server/simple-app-v2.py" ]
CMD [ "pytest", "-v", ">", "logs/test_results" ]
