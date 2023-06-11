import time, sys
import pygame
from abc import ABC, abstractmethod
from button import Button
from copy import copy, deepcopy
from character.hero.utils import heroes_dict
from game.utils import (
    
                        draw_player_slot,
                        first_time_draw_player_slot,
                        hero_pick,
                        set_ally_and_enemy_team_and_heroes, 
                        team_picking)
from utils import (write_per_character, clear_screen, get_font,
                   SCREEN, BG, PLAY_IMAGE_PATH, OPTION_IMAGE_PATH, QUIT_IMAGE_PATH, SHOP_IMAGE_PATH,
                   LEFT_ARROW_IMAGE_PATH, RIGHT_ARROW_IMAGE_PATH, FONT_PATH)
from user.user import Player
mark_picked_heroes = {}
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
        heroes_for_computer = [hero for hero in heroes_dict]
        self.__is_loopable = True,
        self.__player1 = player1
        self.computer1 = Player('Computer 1','computer1computer1',heroes_for_computer)
        self.computer2 = Player('Computer 2','computer2computer2',heroes_for_computer)
        self.computer3 = Player('Computer 3','computer3computer3',heroes_for_computer)
        self.computer4 = Player('Computer 4','computer4computer4',heroes_for_computer)
        self.computer5 = Player('Computer 5','computer5computer5',heroes_for_computer)
        self.computer6 = Player('Computer 6','computer6computer6',heroes_for_computer)
        self.computer7 = Player('Computer 7','computer7computer7',heroes_for_computer)
        self.computer8 = Player('Computer 8','computer8computer8',heroes_for_computer)
        self.computer9 = Player('Computer 9','computer9computer9',heroes_for_computer)
    
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
        # classic_or_below_epic_pick(player1=self.get_player(), player2=self.computer1,
        #                            player3=self.computer2, player4=self.computer3,
        #                            player5=self.computer4, player6=self.computer5,
        #                            player7=self.computer6, player8=self.computer7,
        #                            player9=self.computer8, player10=self.computer9
        #                            )
        pass
    
    def start_game(self):
        for hero in heroes_dict:
            print(f"{hero} Image path: {heroes_dict[hero].get_select_hero_icon()}")
        ally_team, team_ally_all_heroes, enemy_team, team_enemy_all_heroes=set_ally_and_enemy_team_and_heroes(
            player1=self.get_player(), player2=self.computer1, player3=self.computer2, player4=self.computer3, player5=self.computer4, 
            player6=self.computer5, player7=self.computer6, player8=self.computer7, player9=self.computer8, player10=self.computer9
                                   )
        slot_for_each_player = first_time_draw_player_slot(ally_team, SCREEN)
        main_player=self.get_player()
        team_picking(main_player, enemy_team, team_enemy_all_heroes)
        hero_pick(SCREEN, main_player, slot_for_each_player, ally_team, team_ally_all_heroes)
        
class Brawl(Game):
    def __init__(self, player1: Player):
        super().__init__(player1)
        
    def pick_hero(self):
        pass
    
    def start_game(self):
        pass