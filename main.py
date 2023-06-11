from character.hero.utils import generate_heroes
from game.utils import get_last_login_or_create_last_login_user
from user.user import Player
from menu.menu import MainMenu

import pygame
pygame.init()

pygame.display.set_caption("Menu")

if __name__ == '__main__':
    generate_heroes()
    last_user = get_last_login_or_create_last_login_user()
    heroes_owned = list()
    for hero in last_user['heroes_owned']:
        heroes_owned.append(hero)
    last_user = Player(
        username=last_user['username'],
        password=last_user['password'],
        heroes_owned=heroes_owned,
        current_rank=last_user['current_rank'],
        battle_point=last_user['battle_point'],
        diamonds=last_user['diamonds']
    )
    
    menu = MainMenu(last_user) 
    menu.menu_started()   
    # while menu.get_is_loopable():
    #     menu.menu_started()
        