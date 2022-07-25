
import requests
import os
from getpass import getpass
import json
import base64
from time import sleep



url = 'https://cae-bootstore.herokuapp.com'

endpoint_login = "/login"
endpoint_user = "/user"
endpoint_book = "/book"
endpoint_question = "/question"
endpoint_question_all = "/question/all"
endpoint_edit_question = "/question/"

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')


def register_user(payload):
    payload_json_string = json.dumps(payload)
    headers = {
        'Content-Type':'application/json'
    }
    response = requests.post(
        url + endpoint_user,
        data = payload_json_string,
        headers = headers
    )
    return response.text

import base64

def login_user(user_name, password):
    auth_string = user_name + ":" + password
    
    headers={
        'Authorization' : "Basic "+base64.b64encode(auth_string.encode()).decode()
    }
    
    user_data = requests.get(
        url + endpoint_login,
        headers=headers
    )
    return user_data.json()
def get_token(user_name, password):
    auth_string = user_name + ":" + password
    
    headers={
        'Authorization' : "Basic "+base64.b64encode(auth_string.encode()).decode()
    }
    
    user_data = requests.get(
        url + endpoint_login,
        headers=headers
    )
    return user_data.json()['token']

def edit_user(token, payload):
    payload_json_string = json.dumps(payload)
    headers={
        'Content-Type':'application/json',
        'Authorization':'Bearer ' + token
    }
    response = requests.put(
        url + endpoint_user,
        data=payload_json_string,
        headers=headers
    )
    return response.text

def delete_user(token):
    headers = {
        'Authorization':"Bearer " + token
    }
    
    response = requests.delete(
        url+endpoint_user,
        headers=headers
    )
    return response.text


             
                
                
             