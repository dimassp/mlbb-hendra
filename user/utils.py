from user.user import Player
from utils import write_per_character, clear_screen, users_json_path
from character.hero.utils import add_heroes_to_player, heroes_dict

from json import JSONEncoder
import json
import time

def get_all_existing_users():
    with open(users_json_path, 'r') as users:
        data = json.load(users)
    return data

def get_user_account(username):
    with open(users_json_path, 'r') as users:
        data = json.load(users)
    user_account = data.get(username)
    return user_account
    
def create_player_object_from_existing_object(username, password, heroes_owned, battle_point, diamonds):
    player = Player(username, password, heroes_owned, battle_point, diamonds)
    return player

def create_new_user():
    write_per_character("Enter your username: ", 0.02, 1)
    username = input("")
    username = create_new_username(username)
    
    write_per_character("Enter new password: ", 0.02, 1)
    password = input("")
    password = create_new_password(password)
    
    new_user_dict = create_user_dict(username, password)
    
    users_data = get_all_existing_users()
    
    users_data.update(new_user_dict)
    save_to_json(users_data)
    
    write_per_character("New account successfully created",0.02,0)
    clear_screen(1)
    return username
    

def save_to_json(users_data):
    with open(users_json_path,'w') as json_file:
        json.dump(users_data, json_file,indent=3)

def create_user_dict(username, password):
    new_user = {
        username: {
            "username": username,
            "password": password,
            "current_rank": 0,
            "battle_point": 0,
            "diamonds": 0,
            "heroes_owned": {}
        }
    }
    
    starter_heroes = ["Gord", "Layla", "Fredrin"]
    for hero in starter_heroes:
        new_user[username]["heroes_owned"].update({hero: heroes_dict.get(hero).my_own_hero_encoder()})
    return new_user

def create_new_username(username):
    check_if_username_dont_have_characters(username)
    
    while check_if_username_exist(username) is not None:
        if check_if_username_exist(username) is not None:
            write_per_character("Username already used by another player...",0.02, 0.8)
            write_per_character(" Please use another username.",0.02, 0.8)
            clear_screen(0)
            write_per_character("Enter your username: ", 0.02, 1)
            username = input("")
            username = check_if_username_dont_have_characters(username)
    return username

def check_if_username_dont_have_characters(username):
    while len(username.strip()) <=0:
        write_per_character("Username should have at least one character", 0.02,1)
        clear_screen(0)
        write_per_character("Enter your username: ", 0.02, 1)
        username = input("")
    return username

def check_if_username_exist(username):
    data = get_all_existing_users()
    return data.get(username)


def create_new_password(password):
    password = check_if_password_length_less_than_10(password)
    return password

def check_if_password_length_less_than_10(password):
    while len(password) < 10 :
        write_per_character("Password should have at least 10 characters", 0.02, 1)
        clear_screen(0)
        write_per_character("Enter new password: ", 0.02, 1)
        password = input("")
    return password