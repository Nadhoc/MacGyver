# -*-coding:utf-8 -
import pygame
#CREATE human class and sprite graphic coponent
class Human:
    
    def __init__(self, labyrinthe):
        print("création d'un humain")   
        self.image = pygame.image.load('ressource/MacGyver.png')
        #++Picture go right++##
        self.right = pygame.image.load('ressource/MacGyver.png')
        #++Picture go left++##
        self.left = pygame.image.load('MacGyverleft.png')
        #++Picture go Down++##
        self.down = pygame.image.load('MacGyverDown.png')
        ##++Picture go Up++##
        self.up = pygame.image.load('MacGyverup.png')
        #++Position in pixe++#
        self.x = 0
        self.y = 0
        #Position in square+++#
        self.sprite_x = 0
        self.sprite_y = 0
        #++default direction++#
        self.direction = self.right
        #++Labyrinth++##
        self.labyrinthe = labyrinthe
       

        
    def move(self, direction):
        ##+++Method whitch allows to move the character++## 
        ##+++This method takes in parmeter++## 
        ##+++the direction where Mac Gyver must go (letf, Right, Up and down)++##

        #++In order to Move to the right
        if direction == "right":
            if self.sprite_x < NB_SPRITE -1: #++In order to avoid go out of the screen++#
                if self.labyrinthe.grid[self.sprite_y][self.sprite_x+1] != "0": #++Don't go to a wall++#
                    #++to move of a sprite
                    self.sprite_x += 1
                    #++the Position in pixel:
                    self.x = self.sprite_x * SPRITE_SIZE 
            self.direction = self.right

        #++In order to Move to the Left
        if direction == "left":
            if self.sprite_x > 0: #++Inorder to avoid go out of the screen
                if self.labyrinthe.grid[self.sprite_y][self.sprite_x-1] != "0": #++Don't go to a wall++#
                    #++ to move of one sprite
                    self.sprite_x -= 1
                    #++The Position in pixel:
                    self.x = self.sprite_x * SPRITE_SIZE    
            self.direction = self.left       

        #++ In order to Move to the Down
        if direction == "down":
            if self.sprite_y < NB_SPRITE-1: #++In order to avoid go out of the screen++##
                if self.labyrinthe.grid[self.sprite_y+1][self.sprite_x] != "0": #Don't go to a wall++#
                    #++ tomove on one sprite
                    self.sprite_y += 1
                    #++ The Position in pixel:
                    self.y = self.sprite_y * SPRITE_SIZE
            self.direction = self.down
            
       
        #++ In order to Move Up
        if direction == "up":
            if self.sprite_y > 0: #++In order to avoid go out of the screen++##
                if self.labyrinthe.grid[self.sprite_y-1][self.sprite_x] != "0": #Don't go to a wall++##
                    #++ to move on one sprite++##
                    self.sprite_y -= 1
                    #++ The Position in pixel:
                    self.y = self.sprite_y * SPRITE_SIZE
            self.direction = self.up


