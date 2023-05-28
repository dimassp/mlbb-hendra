from abc import ABC, abstractmethod
from character.hero.hero import Hero_3Skill, Hero_4Skill
class PlayerAbstract(ABC):
    @abstractmethod
    def buy_diamond(self):
        pass
    
    @abstractmethod
    def buy_hero(self):
        pass
    
    @abstractmethod
    def change_username(self):
        pass
    
    @abstractmethod
    def change_password(self):
        pass
        

class Player(PlayerAbstract):
    def __init__(self, 
                 username: str,
                 password: str,
                 heroes_owned: list,
                 current_rank: int=0,
                 battle_point: int=0,
                 diamonds: int=0,
                 ):
        self.__username = username
        self.__password = password
        self.__current_rank = current_rank
        self.__heroes_owned = heroes_owned
        self.__battle_point = battle_point
        self.__diamonds = diamonds
        self.__hero_used_in_game:  Hero_3Skill | Hero_4Skill=None
        super().__init__()
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_current_rank(self):
        return self.__current_rank
    
    def get_heroes_owned(self):
        return self.__heroes_owned
    
    def get_battle_point(self):
        return self.__battle_point
    
    def get_diamonds(self):
        return self.__diamonds
    
    def get_hero_used_in_game(self):
        return self.__hero_used_in_game
    
    def buy_diamond(self):
        pass
    
    def buy_hero(self):
        pass
    
    def set_hero_used_in_game(self, hero: Hero_3Skill | Hero_4Skill |None):
        self.__hero_used_in_game = hero
    
    def set_current_rank(self, value: int):
        self.__current_rank += value
    
    def change_username(self):
        pass
    
    def change_password(self):
        pass