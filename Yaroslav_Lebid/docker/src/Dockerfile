FROM python:3.7

RUN pip install -U pytest
RUN pip install pytest-json-report --upgrade 
RUN pip install requests
RUN pip install jwt

WORKDIR /src

COPY . .

CMD [ "pytest", "--json-report", "--json-report-summary", "-v", "test_refresh_token.py" ]