# -*-coding:utf-8 -
import pygame
import random
from config.constant import *
#create class object
#attibut name
class Item:
    def __init__(self,name, SURFACE, Labyrinthe):
        # attribute position pixel
        self.x = 0
        self.y = 0
        # attribute position in square
        self.sprite_x = 0
        self.sprite_y = 0
        # attribute name of item
        self.name = name
        # attribute Labyrinth
        self.labyrinthe = Labyrinthe
        # attribute Surface
        self.surface = SURFACE
        print(f"Initialisation de l'item {name}")
    def locate_item(self):
        #+++To locate one element: we detecte empty cells+++## 
        #+++We catch the coordinate in a list of tuple (y,x), we choose one pair of co-ordinate++##
        position = []
        coordinates = ()
        num_line = 0
        for num_line in range(15):

            for num_cell in range(15):

                if self.labyrinthe.grid[num_line][num_cell] == "0":
                    coordinates = (num_line, num_cell)
                    position.append(coordinates)
        items_coordinates = random.choice(position)
        self.sprite_y = items_coordinates[0]
        self.sprite_x = items_coordinates[1]
        self.x = self.sprite_x * SPRITE_SIZE
        self.y = self.sprite_y * SPRITE_SIZE
        print(f"{self.name} vient doit être placé en ("
              f"{self.sprite_x}, {self.sprite_y})")

    def pin_items(self):
        #+++++Pin the name of the items to be kept by MacGyver+++#
        self.labyrinthe.grid[self.sprite_y][self.sprite_x] = self.name
    
    def display_item(self, screen, MacGyver, TOOLS):
        #++ Conditional display of the items:
        #++ if MacGyver caught item we write "0" instead of self.name on labyrinth.
        #++ The display is True if the name of the items is in place of it, 
        #++ else we display nothing +++##

        if self.labyrinthe.grid[self.sprite_y][self.sprite_x] == self.name:
            screen.blit(self.surface, (self.x + 30, self.y + 30)) # + 30 for the offset of the black outline
        
        if self.labyrinthe.grid[MacGyver.sprite_y][MacGyver.sprite_x] == self.name:

           #++++++dysplay : Let's pick-up of the elements+++++++##
            screen.blit(PICKUP, (90 + 30, 120 + 30)) # + 30 for the offset of the black outline
            pygame.display.flip()
            #JINGLE.play()
            time.sleep(1)
            ##++++++++++++++++++++++++++++++++++++++++++++++++++##

            print("Yes! One more {}!".format(self.name))
            self.labyrinthe.grid[MacGyver.sprite_y][MacGyver.sprite_x] = "0"
            TOOLS.append(self.name) 

          # display the scoreboard
        if self.name in TOOLS:
            screen.blit(self.surface, (TOOLS.index(self.name) * SPRITE_SIZE, 0))




