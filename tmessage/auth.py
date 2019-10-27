""" Auth : Register new user, check or authenticate existing user """
import os
import jwt
import requests as r
import dotenv as env
env.load_dotenv()

API_BASE_URL_A = os.environ.get("TMESSAGE_API_URL")
API_BASE_URL_B = "https://peaceful-waters-15584.herokuapp.com"
API_BASE_URL = API_BASE_URL_B or API_BASE_URL_A
API_USER_URL = f'{API_BASE_URL}/api/user'


def check_existed(user_name):
    """ Check if  user already exist """
    endpoint_url = f'{API_USER_URL}/checkExist/{user_name}'
    response = r.get(endpoint_url)
    if response.status_code == 200:
        data = response.json()
        return data['exist']
    error = response.json()
    raise Exception(f'Error Verifying User: {error["message"]}')


def authenticate(user_name, password):
    """ Authenticate already registered User """
    endpoint_url = f'{API_USER_URL}/login'
    headers = {
        "Content-Type": "application/json"
    }
    credential = {
        "user_name": user_name,
        "password": password
    }
    response = r.post(endpoint_url, json=credential, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return jwt.decode(data['token'], verify=False)
    error = response.json()
    raise Exception(f'Error Authenticating User: {error["message"]}')


def register(user_name, displayed_name, password, password_confirm):
    """ Register a new User """
    endpoint_url = f'{API_USER_URL}/register'
    headers = {
        "Content-Type": "application/json"
    }
    new_user = {
        "user_name": user_name,
        "displayed_name": displayed_name,
        "password": password,
        "password_confirm": password_confirm
    }
    response = r.post(endpoint_url, json=new_user, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return jwt.decode(data['token'], verify=False)
    error = response.json()
    raise Exception(f'Error Registering User: {error["message"]}')
