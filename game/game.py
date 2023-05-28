import time
from abc import ABC, abstractmethod
from user.user import Player
from game.utils import classic_or_below_epic_pick
class GameAbstract(ABC ):
    @abstractmethod
    def pick_hero(self):
        pass
    
    @abstractmethod
    def start_game(self):
        pass
    
    # @abstractmethod
    # def in_game(self):
    #     pass
    

class Game(GameAbstract):
    def __init__(self, player1: Player):
        self.__is_loopable = True,
        self.__player1 = player1
        self.computer1 = Player('Computer 1','computer1computer1',['Gord','Layla'])
        self.computer2 = Player('Computer 2','computer2computer2',['Gord','Layla'])
        self.computer3 = Player('Computer 3','computer3computer3',['Gord','Layla'])
        self.computer4 = Player('Computer 4','computer4computer4',['Gord','Layla'])
        self.computer5 = Player('Computer 5','computer5computer5',['Gord','Layla'])
        self.computer6 = Player('Computer 6','computer6computer6',['Gord','Layla'])
        self.computer7 = Player('Computer 7','computer7computer7',['Gord','Layla'])
        self.computer8 = Player('Computer 8','computer8computer8',['Gord','Layla'])
        self.computer9 = Player('Computer 9','computer9computer9',['Gord','Layla'])
    
    def get_is_loopable(self):
        return self.__is_loopable
    
    def get_player(self):
        return self.__player1
    
    def set_is_loopbale(self, value: bool):
        self.__is_loopable = value
    
class Ranked(Game):
    def __init__(self, player1: Player):
        super().__init__(player1)
        
    def pick_hero(self):
        pass
    
    def start_game(self):
        pass
    
class Classic(Game):
    def __init__(self, player1: Player):
        super().__init__(player1)
        
    def pick_hero(self):
        classic_or_below_epic_pick(player1=self.get_player(), player2=self.computer1,
                                   player3=self.computer2, player4=self.computer3,
                                   player5=self.computer4, player6=self.computer5,
                                   player7=self.computer6, player8=self.computer7,
                                   player9=self.computer8, player10=self.computer9
                                   )
    
    def start_game(self):
        print(f"classic game.")
        print(f"player username: {self.get_player().get_username()}")
        print(f"player password: {self.get_player().get_password()}")
        print(f"player current_rank: {self.get_player().get_current_rank()}")
        print(f"player heroes_owned: {self.get_player().get_heroes_owned()}")
        print(f"player battle_point: {self.get_player().get_battle_point()}")
        self.pick_hero()
        time.sleep(5)
        pass
    
class Brawl(Game):
    def __init__(self, player1: Player):
        super().__init__(player1)
        
    def pick_hero(self):
        pass
    
    def start_game(self):
        pass