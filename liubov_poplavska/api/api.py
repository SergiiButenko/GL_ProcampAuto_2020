import datetime
import json

import jwt
import requests

base_url = 'http://0.0.0.0:5002/'

class Session:

    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token

    def token(self):
        return jwt.decode(self.access_token, verify=False)

    def is_expired(self):
        return self.token()['exp'] <= datetime.datetime.timestamp(datetime.datetime.now())

    def renew_token(self):
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.refresh_token}"}
        res = requests.post(url=base_url + "refresh", headers=headers)
        self.access_token = res.json()['access_token']
        return self.access_token

class API:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.session = None

    def login(self):
        payload = {'username': self.username, 'password': self.password}
        headers = {"Content-Type": "application/json"}
        res = requests.post(url=base_url + "login", data=json.dumps(payload), headers=headers)
        self.session = Session(**res.json())

    def get_items(self):
        if self.session.is_expired():
            self.session.renew_token()
        headers = {'Authorization': f"Bearer {self.session.access_token}"}
        requests.get(url=base_url + 'items', headers=headers)