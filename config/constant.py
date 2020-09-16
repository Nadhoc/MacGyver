#!/usr/bin/python3.5
# -*-coding:utf-8 -
#++++here we have all constants of the MacGiver escape Game+++##
import pygame
from pygame.locals import *

PATH = "ressource/"
#Constant for loops
MAIN_LOOP = True
WELCOME_LOOP = True
GAME_LOOP = True

#Dimensions of game Screen
NB_SPRITE = 15
SPRITE_SIZE = 30
SCREEN_SIZE = ((NB_SPRITE + 2) * SPRITE_SIZE, (NB_SPRITE + 2) * SPRITE_SIZE)

#Display video of Screen game
Screen = pygame.display.set_mode(SCREEN_SIZE)
TITLE_screen = "Help MacGyver to escape "
ICONE = pygame.image.load(PATH + "Gardien.png").convert_alpha()

#Screen "home"
WELCOME = pygame.image.load("ressource/Home_mgver.JPG").convert()

#Screen Pick-up Elements
PICKUP = pygame.image.load("ressource/One_more.JPG").convert_alpha()

#Screen Game-Over
GAMEOVER = pygame.image.load("ressource/Game_Over.JPG").convert_alpha()

#Screen You win
WIN = pygame.image.load("ressource/win.JPG").convert_alpha()

#Game background
BLACK_GROUND = pygame.image.load("ressource/back_ground.png").convert()
BACKGROUND = pygame.image.load("ressource/background.jpg").convert()

#kind of sprite
WALL = pygame.image.load("ressource/floor.JPG")
ARRIVAL = pygame.image.load("ressource/Gardien.png").convert_alpha()

#kind of tools
TUBE = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
ETHER = pygame.image.load("ressource/ether.png").convert_alpha()
SERINGUE = pygame.image.load("ressource/seringue.png").convert_alpha()

#Display MacGyver
MACGYVER_IMAGE = pygame.image.load(PATH + "MacGyver.png").convert_alpha()

#variable contain map
FILE = ""

#sound bégin and finish ok
#begin = pygame.mixer.Sound("sound/Macgyver_sound.wav")
