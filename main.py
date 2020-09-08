#!/usr/bin/python3
# programm launch
#coding: UTF-8
#import pygame and launch it
import time
from config.constant import *
from classes.human import Human
from classes.item import Item
from classes.labyrinthe import Labyrinthe


def main():
    pygame.init()

    # generate windows game
    # configure windows size
    # Title Game and Icone
    pygame.display.set_icon(ICONE)
    pygame.display.set_caption("Nadir, Save MacGyver !!")
    screen = pygame.display.set_mode((450, 450))

    #Loading screen welcome
    screen.blit(BLACK_GROUND, (0, 0))
    screen.blit(WELCOME, (-2, 35))


    #+++++++++++The Main Loop+++++++##
    MAIN_LOOP = True
    while MAIN_LOOP:

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
                    screen.blit(BACKGROUND, (0, 0))
                    pygame.display.flip()
                    time.sleep(1)

                    WELCOME_LOOP = False
                    GAME_LOOP = True

                    #Load the game's map
                    FILE = "ressource/lab.txt"


        print("Menu terminé, passage au jeu.")

        if FILE != "": #We make sure that the file really exists and is not empty
            #load the background
            screen.blit(BACKGROUND, (30, 30))

                 #generate the labyrinth
            labyrinthe = Labyrinthe(FILE)
            labyrinthe.generate()
            labyrinthe.display(screen)

            #Get the items in the labyrinthe

            seringue = Item("seringue", SERINGUE, labyrinthe)
            seringue.locate_item()
            seringue.pin_items()

            ether = Item("ether", ETHER, labyrinthe)
            ether.locate_item()
            ether.pin_items()

            tube = Item("tube", TUBE, labyrinthe)
            tube.locate_item()
            tube.pin_items()

            #Add arrived icon
            ARRIVED = pygame.image.load("ressource/arrived.JPG").convert_alpha()
            screen.blit(ARRIVED, (390,420))
           #Add MacGyver in the Labyrinth with his position
            MacGyver = Human(labyrinthe)
            MacGyver = pygame.image.load(PATH + "MacGyver.png").convert_alpha()
            move_MacGyver = MacGyver.get_rect()
            screen.blit(MacGyver, (0,0))# + 30 for the offset of the black outline

        #++++++++GAME_LOOP++++++++++++++++++#
        #Initialyse at every game_loop an empty list to put the elements inside
        TOOLS = []
        while  GAME_LOOP:
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():

                #Quit the program
                if event.type == QUIT:
                    print("See you next time !")
                    MAIN_LOOP = False
                    GAME_LOOP = False

                elif event.type == KEYDOWN:

                    #Quit the game and go back Home
                    if event.key == K_ESCAPE:
                            GAME_LOOP = False

                    #create event to move player
                    elif event.key == K_RIGHT:
                            Macgyverright.move("right")

                    elif event.key == K_LEFT:
                        Macgyverleft.move("left")

                    elif event.key == K_UP:
                            Macgyverup.move("up")

                    elif event.key == K_DOWN:
                            Macgyverdown.move("down")


            #Display the game board
            screen.blit(BACKGROUND, (0, 0))
            screen.blit(MacGyver, move_MacGyver)
            labyrinthe.display(screen)


            pygame.display.flip()

            #Add conditionnal display of Element

            #tube.display_item(screen, MacGyver, TOOLS)
            #seringue.display_item(screen, MacGyver, TOOLS)
            #ether.display_item(screen, MacGyver, TOOLS)



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


if __name__ == "__main__":
    main()


