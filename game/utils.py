from button import Button
from user.utils import create_new_user, get_user_account
from user.user import Player
from utils import last_login_json_path, clear_screen, get_font
from character.hero.utils import heroes_dict

from copy import copy, deepcopy

import json
import pygame
import random
import sys
import time
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
    # main__player = [popped_player for popped_player in all_players if popped_player.get_username() == main_player.get_username()]
    # main__player = main__player[0]
    # ally_team.update({main__player.get_username(): main__player})
    
    #SET ENEMY TEAM
    while len(enemy_team) !=5:
        random_number = random.randrange(0,len(all_players)-1)
        popped_player = all_players[random_number]
        if popped_player.get_username() == main_player.get_username():
            # print("pass")
            pass
        else:
            popped_player = all_players.pop(random_number)
            enemy_team.update({popped_player.get_username(): popped_player})
            # print("update enemy team")
    print(f"player left: {len(all_players)}")
    
    #SET ALLY TEAM
    while len(ally_team) != 5:
        # random_number = random.randrange(0,len(all_players)-1)
        # popped_player = all_players.pop(0)
        # if popped_player.get_username() == main__player.get_username():
        #     pass
        # else:
        popped_player = all_players.pop(0)
        ally_team.update({popped_player.get_username(): popped_player})
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
    

def team_picking(main_player: Player, team, all_heroes):
    all_heroes_list = list(all_heroes)
    for player in team:
        if player == main_player.get_username():
            show_heroes(all_heroes)
            pick_hero = input(f"Pick a hero for player {player}: ")
            pick_hero = int(pick_hero)
            picked_hero = all_heroes_list.pop(pick_hero-1)
        else: 
            random_pick = random.randrange(len(all_heroes_list))
            picked_hero_name = all_heroes_list.pop(random_pick)
            picked_hero = all_heroes[picked_hero_name]
        team[player].set_hero_used_in_game(picked_hero)
        # print(f"hero used by {player}: {team[player].get_hero_used_in_game()}")
        # print(f"get picked hero from all heroes: {all_heroes[picked_hero_name]}")
        all_heroes[picked_hero_name].set_is_picked(True)


def randomize_player_order(all_players: list):
    random_all_player=[]
    while len(all_players) != 0:
        if len(all_players) == 1:
            random_number = 0
        else:
            random_number = random.randrange(0,len(all_players)-1)
        random_player = all_players.pop(random_number)
        random_all_player.append(random_player)
    return random_all_player

def check_hero_icon_input(SHOP_MOUSE_POS, SCREEN, main_player, mark_picked_heroes, hero_btn_with_class, current_turn, ally_team: dict, ally_team_turn):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for hero in hero_btn_with_class:
            if current_turn == main_player.get_username():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if hero[0].checkForInput(SHOP_MOUSE_POS):
                        set_hero_for_main_player_and_update_picked_heroes(ally_team, current_turn, hero, ally_team_turn, mark_picked_heroes)
                        set_hero_for_ally_player_and_update_picked_heroes(ally_team_turn, ally_team,hero_btn_with_class)
                        # player=ally_team.get(current_turn)
                        # if not hero[1].get_is_picked():
                        #     player.set_hero_used_in_game(hero[1])
                        #     picked_hero = {
                        #         hero[1].get_hero_name(): {
                        #             "hero_name": hero[1].get_hero_name(),
                        #             "IMAGE_X_POS": hero[0].x_pos,
                        #             "IMAGE_Y_POS": hero[0].y_pos
                        #         }
                        #     }
                        #     mark_picked_heroes.update(picked_hero)
                        #     ally_team_turn.pop(current_turn)
                            # for player in ally_team_turn:
                            #     print(f"current player turn: {player}")
                            #     random_number = random.randrange(len(hero_btn_with_class))
                            #     hero_picked = hero_btn_with_class[random_number]
                                # while hero_picked[1].get_is_picked():
                                #     random_number = random.randrange(len(hero_btn_with_class))
                                #     hero_picked = hero_btn_with_class[random_number]
                                # current_player_turn=ally_team.get(player)
                                # current_player_turn.set_hero_used_in_game(hero_picked[1])
                            #     picked_hero = {
                            #         hero_picked[1].get_hero_name(): {
                            #             "hero_name": hero_picked[1].get_hero_name(),
                            #             "IMAGE_X_POS": hero_picked[0].x_pos,
                            #             "IMAGE_Y_POS": hero_picked[0].y_pos
                            #         }
                            #     }
                        #     print(f"get all player's selected hero")
                        #     for player in ally_team:
                        #         print(f"{player}: {ally_team.get(player).get_hero_used_in_game()}, {ally_team.get(player).get_hero_used_in_game().get_hero_name()}")
                                
                        
                pass
                # print(f"current turn is: {current_turn}")
            elif current_turn != main_player.get_username():
                print(f"current turn is not {main_player.get_username()}")

def draw_hero_icon(HERO_BTN, MOUSE_POS, SCREEN):
    for hero_btn in HERO_BTN:
        hero_btn.changeColor(MOUSE_POS)
        hero_btn.update(SCREEN)

def draw_mark_for_picked_heroes(SCREEN, mark_picked_heroes):
    for picked_hero in mark_picked_heroes:
        print(f"drawing {picked_hero} as marked")
        s = pygame.Surface((75,75))
        s.set_alpha(128)
        s.fill((255,0,0))
        SCREEN.blit(s,(mark_picked_heroes[picked_hero]['IMAGE_X_POS']-37,mark_picked_heroes[picked_hero]['IMAGE_Y_POS']-37))

def draw_player_slot(main_player: Player, player_with_slot: dict, team: dict, SCREEN):
    main_player.username = main_player.get_username()
    for player in player_with_slot:
        # print(f"ally team player username: {team.get(player).get_username()}")
        # print(f"ally team player: {team.get(player).get_hero_used_in_game()}")
        player_info = player_with_slot.get(player)
        player_slot = pygame.Surface((256,144))
        player_slot.set_alpha(128)
        player_slot.fill((0,0,255))
        player_username_text = get_font(10).render(player, False, (255,0,0))
        SCREEN.blit(player_slot,player_info['player_slot_pos'])
        try:
            hero_selected = team.get(player).get_hero_used_in_game().get_hero_image_selected_for_slot()
            # print(f"hero selected: {hero_selected}")
            player_selected_hero_image = pygame.image.load(hero_selected)
            SCREEN.blit(player_selected_hero_image,player_info['player_slot_pos'])
        except (TypeError, AttributeError):
            pass
        finally:
            SCREEN.blit(player_username_text, player_info['player_username_text_pos'])

def first_time_draw_player_slot(ally_team, SCREEN):
    X_POS = 0
    Y_POS = 0
    player_slot_dict = {}
    for player in ally_team:
        print(f"")
        player_slot = pygame.Surface((256,144))
        player_slot.set_alpha(128)
        player_slot.fill((0,0,255))
        player_username_text = get_font(10).render(player, False, (255,0,0))
        SCREEN.blit(player_slot,(X_POS,Y_POS))
        SCREEN.blit(player_username_text, (0,Y_POS+144-29))
        player_and_slot = {
            player: {
                "username": player,
                "player_object": ally_team.get(player),
                "player_slot_pos": (X_POS,Y_POS),
                "player_username_text_pos": (0, Y_POS+144-29)
            }
        }
        player_slot_dict.update(player_and_slot)
        Y_POS += 144
        
    return player_slot_dict

def get_hero_icon(team_ally_all_heroes):
    IMAGE_X_POS=350
    IMAGE_Y_POS=100
    hero_btn_with_class = []
    for hero in team_ally_all_heroes:
        HERO_BTN = Button(image=pygame.image.load(heroes_dict[hero].get_select_hero_icon()), 
                            pos=(IMAGE_X_POS, IMAGE_Y_POS),
                            text_input="", 
                            font=get_font(75),
                            base_color="Black", hovering_color="Green")
        btn_with_class = (HERO_BTN,heroes_dict[hero])
        hero_btn_with_class.append(btn_with_class)
        IMAGE_X_POS +=100
        if IMAGE_X_POS >= 1000:
            IMAGE_X_POS = 350
            IMAGE_Y_POS += 100
    
    return hero_btn_with_class
    
def hero_pick(SCREEN, main_player: Player, slot_for_each_player, ally_team, team_ally_all_heroes):
    mark_picked_heroes = {}
    ally_team_turn = deepcopy(ally_team)
    current_turn = main_player.get_username()
    slot_picked_hero = slot_for_each_player
    hero_btn_with_class = get_hero_icon(team_ally_all_heroes)
    hero_btn = [hero_btn[0] for hero_btn in hero_btn_with_class]
    team_ally_all_heroes = [hero[1] for hero in hero_btn_with_class]
    is_loopable = True
    while is_loopable:
        # print(f"player left: {len(ally_team_turn)}")
        SHOP_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        draw_hero_icon(hero_btn, SHOP_MOUSE_POS, SCREEN)
        draw_player_slot(main_player, slot_for_each_player, ally_team, SCREEN)
        draw_mark_for_picked_heroes(SCREEN, mark_picked_heroes)
        check_hero_icon_input(SHOP_MOUSE_POS, SCREEN, main_player, mark_picked_heroes, hero_btn_with_class,current_turn, ally_team, ally_team_turn)
        # print(f"get main_player used hero: {main_player.get_hero_used_in_game()}")
        pygame.display.update()
    print(f"get each player's used hero")
    for player in ally_team():
        pass

def set_ally_and_enemy_team_and_heroes(
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
    random_all_player = randomize_player_order(all_players)
        
    main_player = player1
    ally_team, enemy_team = set_ally_and_enemy_team(main_player, all_players=random_all_player)
    
    team_ally_all_heroes = deepcopy(heroes_dict)
    team_enemy_all_heroes = deepcopy(heroes_dict)
    # print(f"ally team: {ally_team}")
    return ally_team, team_ally_all_heroes, enemy_team, team_enemy_all_heroes

def set_hero_for_ally_player_and_update_picked_heroes(ally_team_turn, ally_team, hero_btn_with_class):
        for player in ally_team_turn:
            print(f"current player turn: {player}")
            random_number = random.randrange(len(hero_btn_with_class))
            hero_picked = hero_btn_with_class[random_number]
            while hero_picked[1].get_is_picked():
                random_number = random.randrange(len(hero_btn_with_class))
                hero_picked = hero_btn_with_class[random_number]
            current_player_turn=ally_team.get(player)
            current_player_turn.set_hero_used_in_game(hero_picked[1])
            picked_hero = {
                hero_picked[1].get_hero_name(): {
                    "hero_name": hero_picked[1].get_hero_name(),
                    "IMAGE_X_POS": hero_picked[0].x_pos,
                    "IMAGE_Y_POS": hero_picked[0].y_pos
                }
            }

def set_hero_for_main_player_and_update_picked_heroes(ally_team, current_turn, hero, ally_team_turn, mark_picked_heroes):
    player=ally_team.get(current_turn)
    if not hero[1].get_is_picked():
        player.set_hero_used_in_game(hero[1])
        picked_hero = {
            hero[1].get_hero_name(): {
                "hero_name": hero[1].get_hero_name(),
                "IMAGE_X_POS": hero[0].x_pos,
                "IMAGE_Y_POS": hero[0].y_pos
            }
        }
        mark_picked_heroes.update(picked_hero)
        ally_team_turn.pop(current_turn)