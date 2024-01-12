import pygame 

'''
    Description: File for assigning constant variables which will serve as a shortcut when changing variables.

    Arguments:
    arg1: pygame.image.load - used for opening/loading an image file

    Returns: Specify the return value of the function if there is
    ret1: 

'''  
# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Chips Game"
BGCOLOR = BLACK
TILESIZE = 80
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
VEL = 1

#Player rotation
PLAYER_LEFT_IMAGE = pygame.image.load('Images/player_left.png')
PLAYER_RIGHT_IMAGE = pygame.image.load('Images/player_right.png')
PLAYER_BACK_IMAGE = pygame.image.load('Images/player_back.png')
PLAYER_FRONT_IMAGE = pygame.image.load('Images/player_front.png')
