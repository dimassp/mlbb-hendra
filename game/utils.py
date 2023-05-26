from user.utils import create_new_user, get_user_account
from utils import last_login_json_path
import json

def update_last_login_dict(username):
    return {
        "last_login": username
    }
    
def save_last_login(username):
    last_login = update_last_login_dict(username)
    
    with open(last_login_json_path, 'w') as json_file:
        json.dump(last_login, json_file, indent=3)

def get_last_login():
    with open(last_login_json_path) as last_user:
        data = json.load(last_user)
    return data['last_login']

## GET LAST LOGIN USER. IF DOESN'T EXIST, CREATE NEW USER AND RETURN NEW USER TO GAME
def get_last_login_or_create_last_login_user():
    last_login = get_last_login()
    if last_login == "":
        new_username = create_new_user()
        save_last_login(new_username)
        last_login = get_last_login()
    else: 
        return get_user_account(last_login)
    return get_user_account(last_login)