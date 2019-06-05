import json

import requests

from . import TOKEN_AUTHENTICATE_URL


def json_request(func):
    def decorated_func(*args, **kwargs):
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

# token 認証機能


def _authorize_by_token(headers={}):
    assert TOKEN_AUTHENTICATE_URL and USER_INFO, (
        "TOKEN認証用のURLとユーザー情報がセットされていません"
        "set_user_infoとset_token_authorize_urlを用いてセットしてください")
    res = requests.post(TOKEN_AUTHENTICATE_URL, USER_INFO, headers=headers)
    return json.loads(res.content)['token']


def token_authorize(func):
    def decorated_func(*args, **kwargs):
        token = _authorize_by_token()
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
