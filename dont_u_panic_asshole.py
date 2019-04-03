import pygame
import json
import os
from lib import gamestates
from lib import intro
from lib import login
from lib import colors


class Game(object):
    def __init__(self):
        self.__game_title = 'Dont\'t u panic asshole'
        self.__settings = None
        self.__settings_file = "settings.json"
        self.__state = None
        self.__clock = None
        self.__screen = None

    def get_screen(self):
        return self.__screen

    def get_settings(self):
        file_exists = os.path.isfile(self.__settings_file)
        if not file_exists:
            self.crash("Settings file does not exists")
        with open("settings.json") as json_file:
            data = json.load(json_file)
        self.__settings = data
        return data

    def init(self):
        if self.__settings is None:
            self.get_settings()
        width = self.__settings['width']
        height = self.__settings['height']
        if self.__settings['fullscreen']:
            display_mode = pygame.FULLSCREEN
        else:
            display_mode = 0
        self.__clock = pygame.time.Clock()
        pygame.init()
        self.__screen = pygame.display.set_mode((width,height),display_mode)
        pygame.display.set_caption(self.__game_title)
        if self.__settings['intro_enable']:
            self.__state = gamestates.GAME_INTRO
        else:
            self.__state = gamestates.GAME_LOGIN
        print("Game initialized")

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def tick(self):
        pygame.display.update()
        self.__clock.tick(self.__settings['fps_max'])
        self.__screen.fill(colors.WHITE)

    def crash(self, msg):
        print(msg)
        pygame.quit()
        exit(-1)

    def quit(self):
        print("Bye bye :(")
        pygame.quit()
        exit(0)


if __name__=="__main__":
    main_loop = Game()
    main_loop.init()
    intro = None
    login = None
    main_menu = None
    server_list = None
    settings = None
    settings_video = None
    settings_controls = None
    settings_audio = None
    creators = None
    game = None
    while True:
        if main_loop.get_state() == gamestates.QUIT:
            main_loop.quit()
        elif main_loop.get_state() == gamestates.INTRO:
            if intro is None:
                game_intro = intro.Intro(game)
            main_loop.set_state(intro.loop())
        elif main_loop.get_state() == gamestates.LOGIN:
            if login is None:
                game_login = login.Login(game)
            main_loop.set_state(login.loop())
        elif main_loop.get_state() == gamestates.MAIN_MENU:
            pass
        elif main_loop.get_state() == gamestates.SERVER_LIST:
            pass
        elif main_loop.get_state() == gamestates.SETTINGS:
            pass
        elif main_loop.get_state() == gamestates.SETTINGS_VIDEO:
            pass
        elif main_loop.get_state() == gamestates.SETTINGS_CONTROLS:
            pass
        elif main_loop.get_state() == gamestates.SETTINGS_AUDIO:
            pass
        elif main_loop.get_state() == gamestates.CREATORS:
            pass
        elif main_loop.get_state() == gamestates.GAME:
            pass
        else:
            main_loop.crash("Unknown game state")
        main_loop.tick()