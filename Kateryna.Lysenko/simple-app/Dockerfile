FROM python:3.7

COPY simple-app.py  ./

COPY requirements.txt ./

EXPOSE 5002

RUN pip install -r requirements.txt

CMD [ "python", "./simple-app.py" ]
