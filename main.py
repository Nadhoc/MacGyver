#!/usr/bin/python3
# programm launch
#coding: UTF-8
#import pygame and launch it
import pygame
import random
import time
from pygame.locals import *
from Constant import *
from classes.human import Human
from classes.Item import Item
from classes.Labyrinthe import Labyrinthe

pygame.init()


# generate windows game
# configure windows size
# Title Game and Icone
pygame.display.set_icon(ICONE)
pygame.display.set_caption("TITLE-screen")
screen = pygame.display.set_mode((720, 580))

#+++++++++++The Main Loop+++++++##
MAIN_LOOP = True
while MAIN_LOOP:

    #Loading screen welcome
    screen.blit(BLACK_GROUND, (0, 0))
    screen.blit(WELCOME, (30, 30))
    #refresh the screen
    pygame.display.flip()

#++++++++The Welcome LOOP+++++++++##
    WELCOME_LOOP = True
    while WELCOME_LOOP:

        #LOOP Speed Limit
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            #Quit the program
            if event.type == QUIT:
                print("See you next time !")
                MAIN_LOOP = False
                WELCOME_LOOP = False
                GAME_LOOP = False

            #Quit Welcome loop to enter in game loop
            if event.type == KEYDOWN and event.key == K_RETURN:

                #######WELCOME TO THE GAME##########
                ###SOUNDTRACK.stop()
                screen.blit(BACKGROUND, (30, 30))
                screen.blit(WELCOME, (120, 150))
                pygame.display.flip()
                time.sleep(1)

                WELCOME_LOOP = False
                GAME_LOOP = True
  
                #Load the game's map
                FILE = "ressource/lab.txt"

    if FILE != "": #We make sure that the file really exists and is not empty

        #load the background
        screen.blit(BACKGROUND, (30, 30))
        
        #generate the labyrinth
        labyrinthe = Labyrinthe(FILE)
        labyrinthe.generate()
        labyrinthe.display(screen)

        #Get the items in the labyrinthe

        SERINGUE = Item("seringue", SERINGUE, labyrinthe)
        SERINGUE.locate_item()
        SERINGUE.pin_items()

        ETHER = Item("ether", ETHER, Labyrinthe)
        ETHER.locate_item()
        ETHER.pin_items()

        TUBE = Item("tube", TUBE, labyrinthe)
        TUBE.locate_item()
        TUBE.pin_items()

        # go to create MacGyver
        MacGyver = Human()

#++++++++GAME_LOOP++++++++++++++++++#
    #Initialyse at every game_loop an empty list to put the elements inside
TOOLS = []
while  GAME_LOOP:

    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
            
        #Quit the program
        if event.type == QUIT:
            print("See you net time !")
            MAIN_LOOP = False
            GAME_LOOP = False 

        if event.type == KEYDOWN:

            #Quit the game and go back Home
            if event.key == K_ESCAPE:
                GAME_LOOP = False

            #create event to move player
            if event.key == K_RIGHT:
                MacGyver.move("right")
            if event.key == K_LEFT:
                MacGyver.move("left")
            if event.key == K_DOWN:
                MacGyver.move("bottom")
            if event.key == K_UP:
                MacGyver.move("up")  


    #Display the game board
    screen.blit(BACKGROUND, (0+30, 0+30))
    labyrinthe.display(screen)

    #Add MacGyver in the Labyrinth with his position
    screen.blit(MacGyver, (MacGyver.x + 30, MacGyver.y + 30)) # + 30 for the offset of the black outline

     #Add conditionnal display of Element

    tube.display_item(screen, MacGyver, TOOLS)
    seringue.display_item(screen, MacGyver, TOOLS)
    ether.display_item(screen, MacGyver, TOOLS)

    pygame.display.flip() 

    if labyrinthe.grid[MacGyver.sprite_x][MacGyver.sprite_y] == "a":

        #The player wins if he collects the tree items
        if len(TOOLS) < 3:

            #+++++DISPLAY GAME OVER++++#
            screen.blit(GAMEOVER, (150+30, 150+30))
            pygame.display.flip()
            time.sleep(2)
            #+++++++++++++++++++++++++++++#
            print("You loose")
            GAME_LOOP = False
            #+++++++++++++++++++++++++++++#
        if len(TOOLS) == 3:
            #+++++DISPLAY YOU WIN+++++++++#        
            screen.blit(WIN, (100+30, 150+30))
            pygame.display.flip()
            time.sleep(2)
            #+++++++++++++++++++++++++++++#                
            print("You win!")
            GAME_LOOP = False




