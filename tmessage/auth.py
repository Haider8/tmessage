#!python

import os
import jwt
import requests as r
import dotenv as env
env.load_dotenv()

API_BASE_URL = os.environ.get("TMESSAGE_API_URL") or "https://peaceful-waters-15584.herokuapp.com"
API_USER_URL = f'{API_BASE_URL}/api/user'


def checkExisted(user_name):
    ENDPOINT_URL = f'{API_USER_URL}/checkExist/{user_name}'
    response = r.get(ENDPOINT_URL)
    if response.status_code == 200:
        data = response.json()
        return data['exist']
    else:
        error = response.json()
        raise Exception(f'Error Verifying User: {error["message"]}')


def authenticate(user_name, password):
    ENDPOINT_URL = f'{API_USER_URL}/login'
    headers = {
        "Content-Type": "application/json"
    }
    credential = {
        "user_name": user_name,
        "password": password
    }
    response = r.post(ENDPOINT_URL, json=credential, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return jwt.decode(data['token'], verify=False)
    else:
        error = response.json()
        raise Exception(f'Error Authenticating User: {error["message"]}')


def register(user_name, displayed_name, password, password_confirm):
    ENDPOINT_URL = f'{API_USER_URL}/register'
    headers = {
        "Content-Type": "application/json"
    }
    newUser = {
        "user_name": user_name,
        "displayed_name": displayed_name,
        "password": password,
        "password_confirm": password_confirm
    }
    response = r.post(ENDPOINT_URL, json=newUser, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return jwt.decode(data['token'], verify=False)
    else:
        error = response.json()
        raise Exception(f'Error Registering User: {error["message"]}')
