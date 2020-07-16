FROM python:3.8-slim
WORKDIR /liubov_poplavska
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
RUN mkdir /reports
ENTRYPOINT ["pytest"]
CMD ["--html=/reports/lpo_report.html",  "test/test_token.py"]