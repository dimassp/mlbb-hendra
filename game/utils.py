from user.utils import create_new_user, get_user_account
from utils import last_login_json_path
from user.user import Player
from character.hero.utils import heroes_dict
import json
import time
import random
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


def set_ally_and_enemy_team(all_players: list):
    ally_team = {}
    enemy_team = {}
    for i, player in enumerate(all_players):
        random_number = random.randrange(0,len(all_players))
        print(f"number: {random_number}")
        popped_player = all_players.pop(random_number)
        ally_team.update({popped_player.get_username(): popped_player})
        
    for i, player in enumerate(all_players):
        random_number = random.randrange(0,len(all_players))
        print(f"number: {random_number}")
        popped_player = all_players.pop(random_number)
        enemy_team.update({popped_player.get_username(): popped_player})
    return ally_team, enemy_team

def classic_or_below_epic_pick(
    player1: Player, 
    player2: Player,
    player3: Player,
    player4: Player,
    player5: Player,
    player6: Player,
    player7: Player,
    player8: Player,
    player9: Player,
    player10: Player,
    ):
    all_players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
    ally_team, enemy_team = set_ally_and_enemy_team(all_players=all_players)
    time.sleep(3)