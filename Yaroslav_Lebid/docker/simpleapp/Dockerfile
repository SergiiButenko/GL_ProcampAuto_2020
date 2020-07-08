FROM python:3.7
EXPOSE 5002
WORKDIR /simpleapp
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", "./simple-app.py" ]