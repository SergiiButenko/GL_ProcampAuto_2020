FROM python:3.7-slim

WORKDIR /app

COPY requirements .
RUN pip install -r requirements

COPY . .

ENTRYPOINT [ "pytest", "-v", "--json-report", "--json-report-file=/logs/session_report.json", "--json-report-indent=3" ]