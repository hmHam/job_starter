'''
when you use jwt to run runserver
you can use this script for
getting json data from your backend!! 
'''

import json
import requests

## change your data pass
from tutorial.todoapp.models import Todo

HOST_LOCATION = 'http://localhost:8000/'
## fill in test username & password
USERNAME = 'taro'
PASSWORD = 'test'

TOKEN_GET_URL = 'api/obtain/token/'

AUTHENTICATION_DATA = {'username': USERNAME, 'password': PASSWORD}

BAKEND_URL = 'api/v1/todoes/'

res = requests.post(HOST_LOCATION + TOKEN_GET_URL, AUTHENTICATION_DATA)

token = json.loads(res.text)['token']

headers = {'token': token}

todoes = requests.get(HOST_LOCATION + BAKEND_URL, headers=headers)

### write some script for using todoes
### following is a example

with open('data.json', 'w') as f:
    json.dump(todoes, f, indent=2)
