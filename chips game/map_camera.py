import pygame
from settings import *

'''
    Description: Function for opening the file containing the map of the game

    Arguments:
    arg1: self - serves as a pointer to the Map class. | e.g. self.data means that data is a variable of the map object.


    Returns: Specify the return value of the function if there is
    ret1: 

''' 
class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

'''
    Description: Function for movement of the screen when following the player as it moves

    Arguments:
    arg1: self - serves as a pointer to the Camera class. | e.g. self.camera means that camera is a variable of the camera object.


    Returns: Specify the return value of the function if there is
    ret1: 

'''
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def moveCam(self, entity):
        return entity.rect.move(self.camera.topleft)

    def follow(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # limit scrolling to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - WIDTH), x)  # right
        y = max(-(self.height - HEIGHT), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)