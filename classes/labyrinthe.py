# -*-coding:utf-8 -
from config.constant import *
class Labyrinthe:
    ## class object labyrinthe/ It has one attribut : an empty grid.
    ## and takes as parameter the file.txt which contains the map ##
    ## This class has two methods: one to generate the structure : a list of list ##
    ## and one to display the grid over the pygame window.##

    def __init__(self, file):
        self.file = file
        self.grid = []

    def generate(self):
        ## Method which generate the structure from the file.txt ##
        frame = []
        # let generate the list of lists
        with open(self.file, "r") as file:
            for line in file:
                line = line.strip() # be careful to cut the line break
                frame.append(list(line))
        self.grid = frame # we get the list of lists in the attribut

    def display(self, screen):
        # from the grid we display each sprite match with a code : 
        #"w" for picture of a wall , "a" for the guardian. Each sprite have
        # x and y coordinates and a size in pixel++##
        num_line = 0 #we begin with the first list so the fist line
        for line in self.grid:
            num_sprite = 0 # we begin with the first square
            for sprite in line:
                X = num_sprite * SPRITE_SIZE
                Y = num_line * SPRITE_SIZE
                if sprite == "m":
                    screen.blit(WALL, (X, Y)) # we load a wall picture over the window
                elif sprite == "a":                      #we add 30 for the offset of the black outline
                    screen.blit(ARRIVAL, (X, Y)) # we load a arrival picture over the window
                elif sprite == "seringue":
                    screen.blit(SERINGUE, (X, Y))
                elif sprite == "ether":
                    screen.blit(ETHER, (X, Y))
                elif sprite == "tube":
                    screen.blit(TUBE, (X, Y))
                num_sprite += 1
            num_line += 1







