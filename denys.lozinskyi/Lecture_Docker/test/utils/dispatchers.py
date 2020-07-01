import requests
from datetime import datetime
from urllib.parse import urljoin
from ..config import URLs


def server_dispatcher(timeout=8):
    """
    Verifies if the server to be tested is running through the timeout in seconds provided as a parameter.
    Over the time given, sends GET requests to the server root endpoint attempting to get 2** status code in response.
    Raises an exception, if failed to (the server is not responding with 2** status code
    """
    time_start = datetime.now()
    while (datetime.now() - time_start).seconds < timeout:
        try:
            response = requests.get(urljoin(URLs.base_url, URLs.root_endpoint))
            response.raise_for_status()
        except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError):
            continue
        else:
            break
    else:
        raise Exception("Server is not responding")
