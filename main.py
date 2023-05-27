from character.hero.utils import generate_heroes
from game.utils import get_last_login_or_create_last_login_user
from user.utils import create_player_object_from_existing_object
from menu.menu import MainMenu

if __name__ == '__main__':
    generate_heroes()
    last_user = get_last_login_or_create_last_login_user()
    last_user = create_player_object_from_existing_object(
        last_user['username'],
        last_user['password'],
        last_user['heroes_owned'],
        last_user['battle_point'],
        last_user['diamonds']
        )
    menu = MainMenu(last_user)    
    while menu.get_is_loopable():
        menu.menu_started()
        