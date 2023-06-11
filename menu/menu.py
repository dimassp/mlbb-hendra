from abc import ABC, abstractmethod
from button import Button
from utils import (write_per_character, clear_screen, get_font,
                   SCREEN, BG, PLAY_IMAGE_PATH, OPTION_IMAGE_PATH, QUIT_IMAGE_PATH, SHOP_IMAGE_PATH,
                   LEFT_ARROW_IMAGE_PATH, RIGHT_ARROW_IMAGE_PATH, FONT_PATH)
from menu.utils import (create_button, update_screen_with_button_and_change_button_color, 
                        check_mouse_input)
from user.user import Player
from game.game import Ranked, Classic, Brawl


import sys
import pygame
pygame.init()

class MenuAbstract(ABC):
    @abstractmethod
    def menu_started(self):
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
        # self.__menus = {
        #     1: self.play_classic,
        #     2: self.play_ranked,
        #     # 3: self.exit_menu,
        #     # 's': self.shop,
        #     # 'p': self.shop,
        # }
        self.is_from_beginning=True
        super().__init__(player)
        
    
    def menu_started(self):
        while True:
            SCREEN.blit(BG,(0,0))
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            # button_list = [USERNAME_BTN, SHOP_BTN,  QUIT_BTN] = create_button([
            button_list = [USERNAME_BTN, SHOP_BTN, LEFT_ARROW_BTN, RIGHT_ARROW_BTN, RANKED_BTN, QUIT_BTN] = create_button([
                (None, (75, 15), f"{self.get_player().get_username()}", 15, "#d7fcd4","White"), #CREATE PROFILE BUTTON
                (None, (75, 100), "SHOP", 20, "#d7fcd4","White"), #CREATE SHOP BUTTON
                (LEFT_ARROW_IMAGE_PATH, (400, 550), "", 75, "#d7fcd4","White"), #CREATE LEFT BUTTON
                (RIGHT_ARROW_IMAGE_PATH, (860, 550), "", 75, "#d7fcd4","White"), #CREATE RIGHT BUTTON
                (None, (640, 550), "Ranked", 50, "#d7fcd4","White"), #CREATE RIGHT BUTTON
                (None, (1175, 30), "EXIT GAME", 20, "#d7fcd4","White") #CREATE QUIT BUTTON
                ])
            
            button_list_with_class_for_menu = [
                (USERNAME_BTN,ProfileMenu(self.get_player()), False),
                (SHOP_BTN,ShopMenu(self.get_player()), False),
                (LEFT_ARROW_BTN,ClassicMenu(self.get_player()), False),
                (RIGHT_ARROW_BTN,BrawlMenu(self.get_player()), False),
                ]
            update_screen_with_button_and_change_button_color(button_list,MENU_MOUSE_POS)
            check_mouse_input(button_list_with_class_for_menu, QUIT_BTN, MENU_MOUSE_POS) 
            pygame.display.update()

        
    # def play_classic(self):
    #     print(f"player: {self.get_player().get_username()}")
    #     print(f"The game is started playing in classic mode")
    #     classic = Classic(self.get_player())
    #     while classic.get_is_loopable():
    #         classic.start_game()
        
        
    # def play_ranked(self):
    #     print(f"player: {self.get_player().get_username()}")
    #     print(f"The game is started playing in ranked mode")

class ClassicMenu(Menu):
    def __init__(self, player: Player):
        super().__init__(player)
    
    def menu_started(self):
        while True:
            SCREEN.blit(BG,(0,0))
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            # button_list = [USERNAME_BTN, SHOP_BTN,  QUIT_BTN] = create_button([
            button_list = [USERNAME_BTN, SHOP_BTN, LEFT_ARROW_BTN, RIGHT_ARROW_BTN, CLASSIC_BTN, QUIT_BTN] = create_button([
                (None, (75, 15), f"{self.get_player().get_username()}", 15, "#d7fcd4","White"), #CREATE PROFILE BUTTON
                (None, (75, 100), "SHOP", 20, "#d7fcd4","White"), #CREATE SHOP BUTTON
                (LEFT_ARROW_IMAGE_PATH, (400, 550), "", 75, "#d7fcd4","White"), #CREATE LEFT BUTTON
                (RIGHT_ARROW_IMAGE_PATH, (860, 550), "", 75, "#d7fcd4","White"), #CREATE RIGHT BUTTON
                (None, (640, 550), "Classic" , 50, "#d7fcd4","White"), #CREATE QUIT BUTTON
                (None, (1175, 30), "EXIT GAME", 20, "#d7fcd4","White") #CREATE QUIT BUTTON
                ])
            
            button_list_with_class_for_menu = [
                (USERNAME_BTN, ProfileMenu(self.get_player()), False), 
                (SHOP_BTN, ShopMenu(self.get_player()), False), 
                (CLASSIC_BTN, Classic(self.get_player()), True), 
                (LEFT_ARROW_BTN, BrawlMenu(self.get_player()), False), 
                (RIGHT_ARROW_BTN, MainMenu(self.get_player()), False), 
                ]
            update_screen_with_button_and_change_button_color(button_list,MENU_MOUSE_POS)
            check_mouse_input(button_list_with_class_for_menu, QUIT_BTN, MENU_MOUSE_POS) 
            pygame.display.update()
    

class RankedMenu(Menu):
    def __init__(self, player: Player):
        super().__init__(player)
    
    def menu_started(self):
        while True:
            SCREEN.blit(BG,(0,0))
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            # button_list = [USERNAME_BTN, SHOP_BTN,  QUIT_BTN] = create_button([
            button_list = [USERNAME_BTN, SHOP_BTN, LEFT_ARROW_BTN, RIGHT_ARROW_BTN, CLASSIC_BTN, QUIT_BTN] = create_button([
                (None, (75, 15), f"{self.get_player().get_username()}", 15, "#d7fcd4","White"), #CREATE PROFILE BUTTON
                (None, (75, 100), "SHOP", 20, "#d7fcd4","White"), #CREATE SHOP BUTTON
                (LEFT_ARROW_IMAGE_PATH, (400, 550), "", 75, "#d7fcd4","White"), #CREATE LEFT BUTTON
                (RIGHT_ARROW_IMAGE_PATH, (860, 550), "", 75, "#d7fcd4","White"), #CREATE RIGHT BUTTON
                (None, (640, 550), "CLASSIC", 50, "#d7fcd4","White"), #CREATE QUIT BUTTON
                (None, (1175, 30), "EXIT GAME", 20, "#d7fcd4","White") #CREATE QUIT BUTTON
                ])
            
            
            button_list_with_class_for_menu = [
                (USERNAME_BTN, ProfileMenu(self.get_player()), False), 
                (SHOP_BTN, ShopMenu(self.get_player()), False), 
                (LEFT_ARROW_BTN, ClassicMenu(self.get_player()), False), 
                (RIGHT_ARROW_BTN, MainMenu(self.get_player()), False), 
                ]
            update_screen_with_button_and_change_button_color(button_list,MENU_MOUSE_POS)
            check_mouse_input(button_list_with_class_for_menu, QUIT_BTN, MENU_MOUSE_POS) 
            pygame.display.update()

class BrawlMenu(Menu):
    def __init__(self, player: Player):
        super().__init__(player)
        
    def menu_started(self):
        while True:
            SCREEN.blit(BG,(0,0))
            
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            # button_list = [USERNAME_BTN, SHOP_BTN,  QUIT_BTN] = create_button([
            button_list = [USERNAME_BTN, SHOP_BTN, LEFT_ARROW_BTN, RIGHT_ARROW_BTN, CLASSIC_BTN, QUIT_BTN] = create_button([
                (None, (75, 15), f"{self.get_player().get_username()}", 15, "#d7fcd4","White"), #CREATE PROFILE BUTTON
                (None, (75, 100), "SHOP", 20, "#d7fcd4","White"), #CREATE SHOP BUTTON
                (LEFT_ARROW_IMAGE_PATH, (400, 550), "", 75, "#d7fcd4","White"), #CREATE LEFT BUTTON
                (RIGHT_ARROW_IMAGE_PATH, (860, 550), "", 75, "#d7fcd4","White"), #CREATE RIGHT BUTTON
                (None, (640, 550), "Brawl", 50, "#d7fcd4","White"), #CREATE QUIT BUTTON
                (None, (1175, 30), "EXIT GAME", 20, "#d7fcd4","White") #CREATE QUIT BUTTON
                ])
            
            
            button_list_with_class_for_menu = [
                (USERNAME_BTN, ProfileMenu(self.get_player()), False), 
                (SHOP_BTN, ShopMenu(self.get_player()), False), 
                (LEFT_ARROW_BTN, MainMenu(self.get_player()), False), 
                (RIGHT_ARROW_BTN, ClassicMenu(self.get_player()), False), 
                ]
            update_screen_with_button_and_change_button_color(button_list,MENU_MOUSE_POS)
            check_mouse_input(button_list_with_class_for_menu, QUIT_BTN, MENU_MOUSE_POS) 
            pygame.display.update()

class ProfileMenu(Menu):
    def __init__(self, player: Player):
        super().__init__(player)
    
    def menu_started(self):
        while True:
            player_username = self.get_player().get_username()
            # print(f"player: {player_username}")
            SHOP_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("white")

            USERNAME_TEXT = get_font(20).render(f"{player_username}", True, "Black")
            USERNAME_RECT = USERNAME_TEXT.get_rect(center=(640, 100))
            SHOP_TEXT = get_font(45).render("This is the PROFILE MENU screen.", True, "Black")
            SHOP_RECT = SHOP_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(USERNAME_TEXT, USERNAME_RECT)
            SCREEN.blit(SHOP_TEXT, SHOP_RECT)

            SHOP_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

            SHOP_BACK.changeColor(SHOP_MOUSE_POS)
            SHOP_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SHOP_BACK.checkForInput(SHOP_MOUSE_POS):
                        main_menu = MainMenu(self.get_player())
                        main_menu.menu_started()
            pygame.display.update()

class ShopMenu(Menu):
    def __init__(self, player: Player):
        super().__init__(player)
        
    def menu_started(self):
        while True:
            player_username = self.get_player().get_username()
            # print(f"player: {player_username}")
            SHOP_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("white")

            USERNAME_TEXT = get_font(20).render(f"{player_username}", True, "Black")
            USERNAME_RECT = USERNAME_TEXT.get_rect(center=(640, 100))
            SHOP_TEXT = get_font(45).render("This is the SHOP screen.", True, "Black")
            SHOP_RECT = SHOP_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(USERNAME_TEXT, USERNAME_RECT)
            SCREEN.blit(SHOP_TEXT, SHOP_RECT)

            SHOP_BACK = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

            SHOP_BACK.changeColor(SHOP_MOUSE_POS)
            SHOP_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SHOP_BACK.checkForInput(SHOP_MOUSE_POS):
                        main_menu = MainMenu(self.get_player())
                        main_menu.menu_started()

            pygame.display.update() 