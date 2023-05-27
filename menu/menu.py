from abc import ABC, abstractmethod
from utils import write_per_character, clear_screen
from user.user import Player
import time, json

class MenuAbstract(ABC):
    @abstractmethod
    def menu_options(self):
        pass
    
    @abstractmethod
    def menu_started(self):
        pass
    
    @abstractmethod
    def get_menus(self):
        pass
    
    def exit_menu(self):
        pass

class Menu(MenuAbstract):
    def __init__(self, player: Player):
        self.__is_loopable = True
        self.__player = player
        
    def get_player(self):
        return self.__player
    
    # def set_player(self, value: Player):
    #     self.__player = player
        
    def get_is_loopable(self):
        return self.__is_loopable
    
    def set_is_loopable(self, value:bool()):
        self.__is_loopable = value
        
class MainMenu(Menu):
    def __init__(self, player: Player):
        self.__menus = {
            1: self.play_classic,
            2: self.play_ranked,
            3: self.exit_menu,
            's': self.shop,
            # 'p': self.shop,
        }
        self.is_from_beginning=True
        super().__init__(player)
        
    def menu_options(self):
        print(f"[P]Profile ")
        print(f"[S]Shop\n")
        print(f"[1]Play Classic [2]Play Ranked [3]Exit Game\n")
    
    def get_menus(self):
        return self.__menus
    
    def menu_started(self):
        if self.is_from_beginning:
            write_per_character("Welcome to Mobile Legends: Bang Bang",0.03,1.3)
            self.is_from_beginning=False
        clear_screen(0)
        self.menu_options()
        choose_menu = input("Select menu: ")
        try:
            choose_menu = int(choose_menu)
        except ValueError:
            choose_menu = choose_menu.lower()
            
        self.get_menus()[choose_menu]()
        
    def play_classic(self):
        print(f"player: {self.get_player().get_username()}")
        print(f"The game is started playing in classic mode")
        
    def play_ranked(self):
        print(f"player: {self.get_player().get_username()}")
        print(f"The game is started playing in ranked mode")
    
    def shop(self):
        print(f"player: {self.get_player().get_username()}")
        shop_menu = ShopMenu(self.get_player())
        while shop_menu.get_is_loopable():
            shop_menu.menu_started()
        # print(f"Shop Menu is showing right now")
    
    def exit_menu(self):
        self.set_is_loopable(False)


class ShopMenu(Menu):
    def __init__(self, player: Player):
        self.__menus = {
            'r': self.recommend,
            'h': self.heroes,
            's': self.skins,
            'd': self.draw,
            'e': self.exit_menu,
            # 'p': self.shop,
        }
        super().__init__(player)
        
    def menu_options(self):
        print(f"[R]Recommend")
        print(f"[S]Skins")
        print(f"[D]Draw")
        print(f"[E]Exit Shop\n")
    
    def get_menus(self):
        return self.__menus
    
    def menu_started(self):
        clear_screen(0)
        write_per_character("Mobile Legends: Bang Bang\n",0.02,0)
        write_per_character("Shop Menu",0.02,0)
        print("\n")
        self.menu_options()
        choose_menu = input("Select menu: ")
        try:
            choose_menu = int(choose_menu)
        except ValueError:
            choose_menu = choose_menu.lower()
            
        self.get_menus()[choose_menu]()
    
    def recommend(self):
        write_per_character("Recommend option",0.02,1)
    
    def heroes(self):
        write_per_character("Hero option",0.02,1)
        pass
    
    def skins(self):
        write_per_character("Skin option",0.02,1)
        pass
    
    def draw(self):
        write_per_character("Draw option",0.02,1)
        pass
    
    def exit_menu(self):
        self.set_is_loopable(False)