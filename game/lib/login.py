import pygame
import os
import json
from game.lib import gamestates
from game.lib import input
from game.lib import button
from game.lib import colors

game_config = None
file_exists = os.path.isfile("lib/config/game_config.json")
if file_exists:
    with open("lib/config/game_config.json") as json_file:
        game_config = json.load(json_file)

FONT_STYLE = game_config['font'] if game_config is not None else "Segoe UI"
FONT_SIZE = game_config['login_font_size'] if game_config is not None else 50


class Login(object):
    def __init__(self, game):
        self.__game = game
        self.__title = pygame.font.SysFont(FONT_STYLE, FONT_SIZE)
        self.__input_login = input.Input(0.25, 0.3, 0.5, 0.1, 'Username')
        self.__input_password = input.Input(0.25, 0.5, 0.5, 0.1, 'Password', is_password=True)
        self.__login_button = button.Button(0.25, 0.65, 0.5, 0.1, text='LOGIN', function=self.login)
        self.__info = button.Button(0.1, 0.85, 0.8, 0.1, text='Enter your username and password',
                                    function=self.hide_info, hover_color=colors.GREEN, nohover_color=colors.GREEN,
                                    button_border=1)
        self.__show_info = True
        print("Login initialized")

    def hide_info(self):
        self.__show_info = False
        self.__info.set_text('')

    def login(self):
        login = self.__input_login.get_value()
        password = self.__input_password.get_value()
        # Test login without connection to server
        print("Try to login")
        if login == '' and password == '':
            self.__info.set_text('You need to type something')
            self.__info.set_color(colors.YELLOW)
            self.__show_info = True
        elif login == '':
            self.__info.set_text('Enter username')
            self.__info.set_color(colors.YELLOW)
            self.__show_info = True
        elif password == '':
            self.__info.set_text('Enter password')
            self.__info.set_color(colors.YELLOW)
            self.__show_info = True
        elif login == 'test' and password == 'test':
            print("Login success")
            self.__game.set_state(gamestates.MAIN_MENU)
        else:
            print("Login failure")
            self.__info.set_text('Wrong username or password')
            self.__info.set_color(colors.RED)
            self.__show_info = True

    def loop(self):
        events = pygame.event.get()
        display_surface = pygame.display.get_surface()
        for event in events:
            if event.type == pygame.QUIT:
                self.__game.set_state(gamestates.QUIT)
        title = self.__title.render("Don\'t u panic a**hole", True, colors.BLACK)
        title_rect = title.get_rect()
        title_rect.center = (display_surface.get_width() / 2, display_surface.get_height() * 0.1)
        display_surface.blit(title, title_rect)
        if self.__show_info:
            self.__info.draw(events)
        self.__input_login.draw(events)
        self.__input_password.draw(events)
        self.__login_button.draw(events)