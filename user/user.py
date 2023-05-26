from abc import ABC, abstractmethod

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
                 heroes_owned: list(),
                 battle_point: int=0,
                 diamonds: int=0,
                 ):
        self.__username = username
        self.__password = password
        self.__heroes_owned = heroes_owned
        self.__battle_point = battle_point
        self.__diamonds = diamonds
        super().__init__()
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_heroes_owned(self):
        return self.__heroes_owned
    
    def get_battle_point(self):
        return self.__battle_point
    
    def get_diamonds(self):
        return self.__diamonds
    
    def buy_diamond(self):
        pass
    
    def buy_hero(self):
        pass
    
    def change_username(self):
        pass
    
    def change_password(self):
        pass