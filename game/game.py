from abc import ABC, abstractmethod
from user.user import Player
class GameAbstract(ABC ):
    @abstractmethod
    def pick_hero(self):
        pass
    

class Game(GameAbstract):
    def __init__(self, player1: Player):
        self.__is_loopable = True
        self.__player1 = player1
        self.__computer1 = Player('Computer 1','computer1computer1')
        self.__computer2 = Player('Computer 2','computer2computer2')
        self.__computer3 = Player('Computer 3','computer3computer3')
        self.__computer4 = Player('Computer 4','computer4computer4')
        self.__computer5 = Player('Computer 5','computer5computer5')
        self.__computer6 = Player('Computer 6','computer6computer6')
        self.__computer7 = Player('Computer 7','computer7computer7')
        self.__computer8 = Player('Computer 8','computer8computer8')
        self.__computer9 = Player('Computer 9','computer9computer9')
    
    def get_is_loopable(self):
        return self.__is_loopable
    
    def set_is_loopbale(self, value: bool()):
        self.__is_loopable = value
    
class Ranked(Game):
    def __init__(self, player1: Player):
        super().__init__(player1)
        
    def pick_hero(self):
        pass
    
class Classic(Game):
    def __init__(self, player1: Player):
        super().__init__(player1)
        
    def pick_hero(self):
        pass
    
class Brawl(Game):
    def __init__(self, player1: Player):
        super().__init__(player1)
        
    def pick_hero(self):
        pass