from character.hero.utils import generate_heroes
from menu.menu import MainMenu
if __name__ == '__main__':
    generate_heroes()
    menu = MainMenu()
    
    while menu.is_loopable:
        menu.start()
        