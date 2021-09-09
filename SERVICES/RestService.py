import requests
import requests.auth
from enum import Enum


class HttpMethods(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class RequestService:
    def __init__(self, url, username, password, ssl_verify=True):
        self.url = url
        self.username = username
        self.password = password
        self.ssl_verify = ssl_verify

    def request_action(self, method, url, files=None, headers=None):
        headers = dict()
        try:
            auth = requests.auth.HTTPBasicAuth(self.username, self.password)

            res = requests.request(method,
                                   url,
                                   files=None,
                                   headers=headers,
                                   allow_redirects=False)
            return res

        except (ConnectionError, ConnectionRefusedError) as e:
            return str(e)