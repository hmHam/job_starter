import requests
import json
from pprint import pprint
from pathlib import Path

HOST_NAME = 'localhost'
PORT = '8000'
BASE_URL = ''
USER_INFO = {}
ACCESS_LIST = []

TOKEN_AUTHENTICATE_URL = ''


def json_request(func):
    def decorated_func(*args, **kwargs):
        global ACCESS_LIST
        ACCESS_LIST.append(BASE_URL + kwargs['path'])
        if 'headers' in kwargs:
            kwargs['headers'].update({
                'Content-Type': 'application/json'
            })
        else:
            kwargs['headers'] = {
                'Content-Type': 'application/json'
            }
        return func(**kwargs)
    return decorated_func


def authorize_by_token(headers={}):
    assert TOKEN_AUTHENTICATE_URL and USER_INFO, (
        "TOKEN認証用のURLとユーザー情報がセットされていません"
        "set_user_infoとset_token_authorize_urlを用いてセットしてください")
    res = requests.post(TOKEN_AUTHENTICATE_URL, USER_INFO, headers=headers)
    return json.loads(res.content)['token']


def token_authorize(func):
    def decorated_func(*args, **kwargs):
        token = authorize_by_token()
        if 'headers' in kwargs:
            kwargs['headers'].update({
                'Authorization': 'JWT ' + token
            })
        else:
            kwargs['headers'] = {
                'Authorization': 'JWT ' + token
            }
        return func(**kwargs)
    return decorated_func


def set_token_authorize_url(path):
    global TOKEN_AUTHENTICATE_URL
    TOKEN_AUTHENTICATE_URL = BASE_URL + path
    print('TOKEN_AUTHENTICATE_URL=%s' % TOKEN_AUTHENTICATE_URL)


def set_host(hostname=HOST_NAME, port=PORT):
    global HOST_NAME, PORT
    HOST_NAME = hostname
    PORT = port


def set_baseurl(version):
    global BASE_URL
    if version[-1] != '/':
        version += '/'
    BASE_URL = f'http://{HOST_NAME}:{PORT}/{version}'


def set_user_info(userinfo):
    global USER_INFO
    if 'username' not in userinfo or 'password' not in userinfo:
        raise KeyError('You need to input username and password')
    USER_INFO = userinfo


def get_info():
    print(f'HOST_NAME: {HOST_NAME}')
    print(f'PORT: {PORT}')
    print(f'BASE_URL: {BASE_URL}')
    print(f'TOKEN_AUTHORIZE_URL: {TOKEN_AUTHENTICATE_URL}')
    print(f'USER_INFO: {USER_INFO.get("username")}')
    print('access log')
    print("\n".join(ACCESS_LIST))


@json_request
@token_authorize
def get(path='/', query={}, headers={}, format='json'):
    return requests.get(BASE_URL + path, query, format=format, headers=headers)


@json_request
@token_authorize
def post(path='/', data={}, headers={}, is_text=True):
    return requests.post(BASE_URL + path, json=data, headers=headers)


@json_request
@token_authorize
def put(path='/', data={}, headers={}, is_text=True):
    print(path)
    return requests.put(BASE_URL + path, json=data, headers=headers)


@json_request
@token_authorize
def patch(path='/', data={}, headers={}, is_text=True):
    return requests.patch(BASE_URL + path, json=data, headers=headers)


@json_request
@token_authorize
def delete(path='/', headers={}, is_text=True):
    return requests.delete(BASE_URL + path, headers=headers)


def return_disable_supplier_data():
    return {"disabled_suppliers": [43]}

def return_ordermain_data():
    fname = Path(__file__).parent / 'data/ordermain.json'
    with open(fname) as f:
        return json.load(f)


def more_od_data():
    fname = Path(__file__).parent / 'data/orderdetail.json'
    with open(fname) as f:
        return json.load(f)

def easy_set(username='admin'):
    set_host(port=8080)
    set_baseurl('api/v2/')
    set_user_info({"username": username, "password": "neko3daisuki"})
    set_token_authorize_url('supplier_login/')

