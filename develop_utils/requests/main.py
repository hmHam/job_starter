import requests

from . import BASE_URL
from .decorators import json_request, token_authorize


@json_request
@token_authorize
def get(path='/', query={}, headers={}):
    return requests.get(BASE_URL + path, query, headers=headers).json()


@json_request
@token_authorize
def post(path='/', data={}, headers={}, is_text=True):
    return requests.post(BASE_URL + path, data=data, headers=headers).json()
