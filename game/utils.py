from user.utils import create_new_user, get_user_account
from user.user import Player
from utils import last_login_json_path, clear_screen
from character.hero.utils import heroes_dict

from copy import copy, deepcopy

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


def set_ally_and_enemy_team(main_player: Player, all_players: list):
    ## MAIN PLAYER WILL ALWAYS IN ALLY TEAM
    ally_team = {}
    enemy_team = {}
    main__player = [popped_player for popped_player in all_players if popped_player.get_username() == main_player.get_username()]
    main__player = main__player[0]
    ally_team.update({main__player.get_username(): main__player})
    #SET ALLY TEAM
    while len(ally_team) != 5:
        random_number = random.randrange(0,len(all_players)-1)
        popped_player = all_players[random_number]
        if popped_player.get_username() == main__player.get_username():
            pass
        else:
            popped_player = all_players.pop(random_number)
            ally_team.update({popped_player.get_username(): popped_player})
            
    #SET ENEMY TEAM
    while len(enemy_team) !=5:
        popped_player = all_players.pop(0)
        if popped_player.get_username() == main__player.get_username():
            # print("pass")
            pass
        else:
            # print("update enemy team")
            enemy_team.update({popped_player.get_username(): popped_player})
    # print(f"player left: {len(all_players)}")
    return ally_team, enemy_team

def show_heroes(team_ally_all_heroes):    
    for i, hero in enumerate(team_ally_all_heroes):
        if team_ally_all_heroes[hero].get_is_picked():
            print(f"[{i+1}] {hero} (Picked)", end=" ")
        else:
            print(f"[{i+1}] {hero}", end=" ")
        if (i+1) % 3 == 0:
            print()
    print("\n")
    

def team_picking(main_player, team, all_heroes):
    all_heroes_list = list(all_heroes)
    for player in team:
        if player == main_player.get_username():
            show_heroes(all_heroes)
            pick_hero = input(f"Pick a hero for player {player}: ")
            pick_hero = int(pick_hero)
            picked_hero = all_heroes_list.pop(pick_hero-1)
        else: 
            random_pick = random.randrange(len(all_heroes_list))
            picked_hero = all_heroes_list.pop(random_pick)
        team[player].set_hero_used_in_game(picked_hero)
        all_heroes[picked_hero].set_is_picked(True)


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
    clear_screen(0)
    all_players = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10]
    main_player = player1
    ally_team, enemy_team = set_ally_and_enemy_team(main_player, all_players=all_players)
    
    team_ally_all_heroes = deepcopy(heroes_dict)
    team_enemy_all_heroes = deepcopy(heroes_dict)
    print(f"Ally team is picking")
    team_picking(main_player, ally_team, team_ally_all_heroes)
    print(f"Enemy team is picking")
    team_picking(main_player, enemy_team, team_enemy_all_heroes)
    print(f"Pick Phase completed...")
    clear_screen(2)
    for i in range(15,-1,-1):
        if i % 10 == 0:
            print(f"Battle started in {i}", end='\r')
            clear_screen(1)
        else:
            print(f"Battle started in {i}", end='\r')
            time.sleep(1)
        