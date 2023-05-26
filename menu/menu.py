from abc import ABC, abstractmethod
from utils import write_per_character, clear_screen
from game.utils import get_last_login_or_create_last_login_user
from user.utils import create_new_user
import time, json

class Menu(ABC):
    @abstractmethod
    def menu_option(self):
        pass
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def get_menus(self):
        pass
    
class MainMenu(Menu):
    def __init__(self):
        self.is_loopable = True
        super().__init__()
        self.__menus = {
            1: self.play_classic,
            2: self.play_ranked,
            3: self.exit,
            's': self.shop,
        }
    
    def menu_option(self):
        print("Main Menu\n")
        print(f"[1]Play Classic [2]Play Ranked [3]Exit Game\n")
        print(f"[S]Shop ")
    
    def get_menus(self):
        return self.__menus
    
    def start(self):
        write_per_character("Welcome to Mobile Legends: Bang Bang",0.03,1.3)
        clear_screen(0)
        last_user = get_last_login_or_create_last_login_user()
        
        self.menu_option()
        choose_menu = input("Select menu: ")
        try:
            choose_menu = int(choose_menu)
        except ValueError:
            choose_menu = choose_menu.lower()
            
        self.get_menus()[choose_menu]()
        time.sleep(3)
        
    def play_classic(self):
        print(f"The game is started playing in classic mode")
        
    def play_ranked(self):
        print(f"The game is started playing in ranked mode")
    
    def shop(self):
        print(f"Shop Menu is showing right now")
    
    def exit(self):
        self.is_loopable = False
        