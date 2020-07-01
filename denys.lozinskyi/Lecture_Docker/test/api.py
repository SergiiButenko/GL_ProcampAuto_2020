import requests
import datetime
from jwt import decode
from requests import Response
from .config import URLs


class API:

    """ contains base methods to work with the 111server API """

    @staticmethod
    def jwt_authenticate(credentials: dict) -> Response:
        """ Authenticates a user in the 111server with the credentials provided.
            Returns the 111server response from authentication
            :param credentials : a dict with user_name and password
            :return : authentication response object
        """
        auth_response = requests.post(
            URLs.url_login, json={'username': credentials['user_name'], 'password': credentials['password']}
        )
        return auth_response

    @staticmethod
    def jwt_authorize(access_token) -> Response:
        """ Authorizes in the 111server with an access token passed as a parameter
            :param access_token : str
            :return : 111server response object
        """
        return requests.get(URLs.url_protected, headers={'Authorization': f'Bearer {access_token}'})

    @staticmethod
    def create_resource(access_token: str, resource: dict) -> tuple:
        """ Creates a resource in the 111server. Returns 111server response and an id of the resource created.
            :param access_token: jwt access token
            :param resource: resource to create
            :return : tuple (server_response, resource_id). If resource creation failed, the id is None
        """
        response = requests.post(URLs.url_items, json=resource, headers={'Authorization': f'Bearer {access_token}'})
        try:
            # resource is (id - 1), because the 111server stores items in a list,
            # and makes them accessible by the index in that list. Thus, actual item id is its index
            resource_id = response.json()['id'] - 1
        except KeyError:
            return response, None
        else:
            # return resource id as a str, because the 111server expects resource id being str
            return response, str(resource_id)

    @staticmethod
    def read_resource(access_token: str, resource_id: str) -> tuple:
        """ Reads a resource by its id. Returns the 111server response, and the resource created content.
            :param access_token: jwt access token
            :param resource_id: resource id
            :return : tuple (server_response, resource_content). If resource reading failed, the resource_content is None
        """
        response = requests.get(
            f'{URLs.url_items}/{resource_id}', headers={'Authorization': f'Bearer {access_token}'}
        )
        try:
            resource_content = response.json()['items']
        except KeyError:
            return response, None
        else:
            return response, resource_content

    @staticmethod
    def delete_resource(access_token: str, resource_id: str) -> Response:
        """ Deletes a resource by its id. Returns the 111server response.
            :param access_token: jwt access token
            :param resource_id: resource id
            :return : server_response object
        """
        response = requests.delete(
            f'{URLs.url_items}/{resource_id}', headers={'Authorization': f'Bearer {access_token}'}
        )
        return response


class Session(API):

    """ when instantiated with user credentials provided, extracts and keeps the access and refresh tokens.
        Contains self methods to verify freshness of and to renew the access token for the session.
        Accesses methods from API class by inheritance
    """

    def __init__(self, credentials):
        auth_response = self.jwt_authenticate(credentials)
        self.access_token = self.get_tokens(auth_response)['access_token']
        self.refresh_token = self.get_tokens(auth_response)['refresh_token']

    @staticmethod
    def get_tokens(auth_response: Response) -> dict:
        """ extracts the access and refresh tokens from the authentication response at the class instantiation """
        try:
            access_token = auth_response.json()['access_token']
        except KeyError:
            access_token = None
        try:
            refresh_token = auth_response.json()['refresh_token']
        except KeyError:
            refresh_token = None
        return {'access_token': access_token, 'refresh_token': refresh_token}

    @property
    def decoded_access_token(self) -> dict:
        """ returns decoded access token from the current session """
        return decode(self.access_token, verify=False)

    def is_access_token_expired(self) -> bool:
        """ returns True, if the current session access token got expired,
            and False otherwise
        """
        return self.decoded_access_token['exp'] <= datetime.datetime.now().timestamp()

    def renew_access_token(self) -> str:
        """ renews the access token for the current session """
        response = requests.post(URLs.url_refresh, headers={"Authorization": f"Bearer {self.refresh_token}"})
        self.access_token = response.json()['access_token']
        return self.access_token
