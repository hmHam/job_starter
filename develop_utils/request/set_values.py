from . import (
    BASE_URL,
    HOST_NAME,
    PORT,
    TOKEN_AUTHENTICATE_URL,
    USER_INFO,
)


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
