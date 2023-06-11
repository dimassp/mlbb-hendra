import pygame

import sys, time

from button import Button
from utils import (write_per_character, clear_screen, 
                   SCREEN, BG, PLAY_IMAGE_PATH, OPTION_IMAGE_PATH, QUIT_IMAGE_PATH, FONT_PATH,
                   LEFT_ARROW_IMAGE_PATH, RIGHT_ARROW_IMAGE_PATH)
from user.user import Player
def get_font(size):
    return pygame.font.Font(FONT_PATH,size)

def create_left_right_arrow(left_arrow_pos: tuple, right_arrow_pos: tuple):
    LEFT_ARROW_BUTTON = Button(image=pygame.image.load(LEFT_ARROW_IMAGE_PATH),
                         pos=left_arrow_pos,
                         text_input="",
                         font=get_font(15),
                         base_color="#d7fcd4",
                         hovering_color="White"
                         )
    
    RIGHT_ARROW_BUTTON = Button(image=pygame.image.load(RIGHT_ARROW_IMAGE_PATH),
                         pos=right_arrow_pos,
                         text_input="",
                         font=get_font(15),
                         base_color="#d7fcd4",
                         hovering_color="White"
                         )
    
    return LEFT_ARROW_BUTTON, RIGHT_ARROW_BUTTON

def update_screen_with_button_and_change_button_color(button_list: list, MENU_MOUSE_POS: tuple):
    for button in button_list:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)

def check_mouse_input(button_list_with_class: list, QUIT_BUTTON: Button, MENU_MOUSE_POS: tuple):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in button_list_with_class:
                if button[2]:
                    if button[0].checkForInput(MENU_MOUSE_POS):
                        button[1].start_game()
                else:
                    if button[0].checkForInput(MENU_MOUSE_POS):
                        button[1].menu_started()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()
    pass

def create_button(btn_info_list: list):
    
    # CREATE USER PROFILE BUTTON
    button_list = list()
    for btn_info in btn_info_list:
        if btn_info[0] is None:
            image=None
        else:
            image=pygame.image.load(btn_info[0])
        new_button = Button(image=image,
                         pos=btn_info[1],
                         text_input=btn_info[2],
                         font=get_font(btn_info[3]),
                         base_color=btn_info[4],
                         hovering_color=btn_info[5]
                         )
        button_list.append(new_button)
    return button_list
