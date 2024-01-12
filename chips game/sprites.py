import pygame as pg
from pygame.sprite import Sprite
from settings import *
from os import path

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

'''
    Description: Function for creating the player sprite and its interaction with the other blocks/sprites

    Arguments:
    arg1: self - serves as a pointer to the Player class. | e.g. self.CHIPS_AMOUNT means that CHIPS_AMOUNT is a variable of the game object.
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

'''  
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.players
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.transform.scale(PLAYER_FRONT_IMAGE,(TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.CHIPS_AMOUNT = []
        self.CHIPS1_AMOUNT = [1,1,1,1,1,1,1,1,1,1]
        self.RED_CHIPS_AMOUNT = []
        self.BLUE_CHIPS_AMOUNT = []
        self.YELLOW_CHIPS_AMOUNT = []
        self.GREEN_CHIPS_AMOUNT = []
        self.FIRE_ELEMENT = []
        self.WATER_ELEMENT = []

    '''
    Description: Function for the movement of the player

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    # Movement command
    def move(self, dx=0, dy=0):

        if not self.collision(dx, dy)  and not self.reddoor_collision(dx,dy) and not self.greendoor_collision(dx,dy) and not self.bluedoor_collision(dx,dy) and not self.yellowdoor_collision(dx,dy) and not self.exit_collision(dx,dy):
            self.x += dx
            self.y += dy

    '''
    Description: Function for the collision of the player to Walls

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    # Wall collision function
    def collision(self, dx = 0, dy = 0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    '''
    Description: Function for the collision of the player to the exit door

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1(exit_unlock): bool - returns true if player coordinates matches the object's coordinates

    ''' 
    # Exit collision function
    def exit_collision(self, dx=0,dy=0):
        for door in self.game.exit:
            if door.x == self.x + dx and door.y == self.y + dy and len(self.CHIPS_AMOUNT) < len(self.CHIPS1_AMOUNT):
                return True
        return False
    
    def exit_unlock(self,dx = 0,dy = 0):
        for door in self.game.exit:
            if door.x == self.x + dx and door.y == self.y + dy and len(self.CHIPS_AMOUNT) >= len(self.CHIPS1_AMOUNT):
                return True
        return False
    
    '''
    Description: Function for the collision of the player to the red door

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1(reddoor_unlock): bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def reddoor_collision(self, dx=0,dy=0):
        for door in self.game.reddoor:
            if door.x == self.x + dx and door.y == self.y + dy and len(self.RED_CHIPS_AMOUNT) < 1:
                return True
        return False

    def reddoor_unlock(self,dx = 0,dy = 0):
        for door in self.game.reddoor:
            if door.x == self.x + dx and door.y == self.y + dy and len(self.RED_CHIPS_AMOUNT) >= 1:
                return True
        return False

    
    '''
    Description: Function for the collision of the player to the green door

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1(greendoor_unlock): bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def greendoor_collision(self, dx=0,dy=0):
        for door in self.game.greendoor:
            if door.x == self.x + dx and door.y == self.y + dy and len(self.GREEN_CHIPS_AMOUNT) < 1:
                return True
        return False

    def greendoor_unlock(self,dx = 0,dy = 0):
        for door in self.game.greendoor:
            if door.x == self.x + dx and door.y == self.y + dy and len(self.GREEN_CHIPS_AMOUNT) >= 1:
                return True
        return False

    '''
    Description: Function for the collision of the player to the blue door

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1(bluedoor_unlock): bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def bluedoor_collision(self, dx=0,dy=0):
        for door in self.game.bluedoor:
            if door.x == self.x + dx and door.y == self.y + dy and len(self.BLUE_CHIPS_AMOUNT) < 1:
                return True
        return False

    def bluedoor_unlock(self,dx = 0,dy = 0):
        for door in self.game.bluedoor:
            if door.x == self.x + dx and door.y == self.y + dy and len(self.BLUE_CHIPS_AMOUNT) >= 1:
                return True
        return False
    
    '''
    Description: Function for the collision of the player to the yellow door

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1(yellowdoor_unlock): bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def yellowdoor_collision(self, dx=0,dy=0):
        for door in self.game.yellowdoor:
            if door.x == self.x + dx and door.y == self.y + dy and len(self.YELLOW_CHIPS_AMOUNT) < 1:
                return True
        return False

    def yellowdoor_unlock(self,dx = 0,dy = 0):
        for door in self.game.yellowdoor:
            if door.x == self.x + dx and door.y == self.y + dy and len(self.YELLOW_CHIPS_AMOUNT) >= 1:
                return True
        return False
    
    '''
    Description: Function for collecting red keys

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def redcollect(self, dx = 0, dy = 0):
        for chiploc in self.game.redkeys:
            if chiploc.x == self.x + dx and chiploc.y == self.y + dy:
                return True
        return False
    
    '''
    Description: Function for collecting green keys

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def greencollect(self, dx = 0, dy = 0):
        for chiploc in self.game.greenkeys:
            if chiploc.x == self.x + dx and chiploc.y == self.y + dy:
                return True
        return False
    
    '''
    Description: Function for collecting blue keys

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def bluecollect(self, dx = 0, dy = 0):
        for chiploc in self.game.bluekeys:
            if chiploc.x == self.x + dx and chiploc.y == self.y + dy:
                return True
        return False
    
    '''
    Description: Function for collecting yellow keys

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    '''
    def yellowcollect(self, dx = 0, dy = 0):
        for chiploc in self.game.yellowkeys:
            if chiploc.x == self.x + dx and chiploc.y == self.y + dy:
                return True
        return False

    
    '''
    Description: Function for collecting chips

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    '''
    def chipscollect(self, dx = 0, dy = 0):
        for chiploc in self.game.chips:
            if chiploc.x == self.x + dx and chiploc.y == self.y + dy:
                return True
        return False

    '''
    Description: Function for collecting fire immunity

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    '''
    def FireCollect (self, dx = 0, dy = 0):
        for fireloc in self.game.fire_element:
             if fireloc.x == self.x + dx and fireloc.y == self.y + dy:
                return True
        return False

    
    '''
    Description: Function for the collision of the player to a fire tile

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1(FireTouch): bool - returns true if player coordinates matches the object's coordinates

    '''
    def FireTouch(self,dx = 0, dy = 0):
        for fireloc in self.game.fire_block:
             if fireloc.x == self.x + dx and fireloc.y == self.y + dy and len(self.FIRE_ELEMENT) < 1:
                return True
        return False
    
    def FireDie(self,dx = 0 ,dy = 0):
        if self.FireTouch(dx,dy):
            self.kill()

    
    '''
    Description: Function for collecting water immunity

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    '''
    def WaterCollect (self, dx = 0, dy = 0):
        for fireloc in self.game.water_element:
             if fireloc.x == self.x + dx and fireloc.y == self.y + dy:
                return True
        return False

    '''
    Description: Function for the collision of the player to a water tile

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1(Water Touch): bool - returns true if player coordinates matches the object's coordinates

    '''
    def WaterTouch(self,dx = 0, dy = 0):
        for fireloc in self.game.water_block:
             if fireloc.x == self.x + dx and fireloc.y == self.y + dy and len(self.WATER_ELEMENT) < 1:
                return True
        return False
    
    def WaterDie(self,dx = 0 ,dy = 0):
        if self.WaterTouch(dx,dy):
            self.kill()

    '''
    Description: Function for the collision of the player to an enemy

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pg.sprite.spritecollide - used for checking collision between 2 variables

    Returns: Specify the return value of the function if there is
    ret1(EnemyTouch): bool - returns true if player coordinates matches the object's coordinates

    '''
    def EnemyTouch(self,dx = 0, dy = 0):
        if pg.sprite.spritecollide(self, self.game.enemy, False):
            return True
        return False
    
    def EnemyDie(self,dx = 0 ,dy = 0):
        if self.EnemyTouch(dx,dy):
            self.kill()

    '''
    Description: Function for the collision of the player to a slide tile

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    '''
    def RSlide_Touch(self,dx = 0,dy = 0):
        for rslideloc in self.game.rslide_tile:
             if rslideloc.x == self.x + dx and rslideloc.y == self.y + dy:
                return True
        return False

    def LSlide_Touch(self,dx = 0,dy = 0):
        for rslideloc in self.game.lslide_tile:
             if rslideloc.x == self.x + dx and rslideloc.y == self.y + dy:
                return True
        return False
    
    def USlide_Touch(self,dx = 0,dy = 0):
        for rslideloc in self.game.uslide_tile:
             if rslideloc.x == self.x + dx and rslideloc.y == self.y + dy:
                return True
        return False
    
    def DSlide_Touch(self,dx = 0,dy = 0):
        for rslideloc in self.game.dslide_tile:
             if rslideloc.x == self.x + dx and rslideloc.y == self.y + dy:
                return True
        return False

    '''
    Description: Function for the collision of the player to a thief tile

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    '''
    def Reset_Touch(self,dx = 0,dy = 0):
        for resloc in self.game.reset_tile:
             if resloc.x == self.x + dx and resloc.y == self.y + dy :
                return True
        return False

    '''
    Description: Function for displaying the inventory on the screen

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: 

    '''
    def showredkey(self):
        if len(self.RED_CHIPS_AMOUNT) == 1:
            # set the pygame window name
            pygame.display.set_caption('Image')
            # create a surface object, image is drawn on it.
            image = pygame.image.load('Images/KeyRed_1.png')
            screen.blit(image, ((TILESIZE-10)/4, (TILESIZE+120)/2))
            clock.tick(60)
        if len(self.RED_CHIPS_AMOUNT) == 2:
            # set the pygame window name
            pygame.display.set_caption('Image')
            # create a surface object, image is drawn on it.
            image = pygame.image.load('Images/KeyRed_1.png')
            screen.blit(image, ((TILESIZE-10)/4, (TILESIZE+120)/2))
            image2 = pygame.image.load('Images/KeyRed_1.png')
            screen.blit(image2, (TILESIZE+3, (TILESIZE+120)/2))
            clock.tick(60)
    
    def showbluekey(self):
        if len(self.BLUE_CHIPS_AMOUNT) == 1:
            # set the pygame window name
            pygame.display.set_caption('Image')
            # create a surface object, image is drawn on it.
            image = pygame.image.load('Images/KeyBlue_1.png')
            screen.blit(image, ((TILESIZE-10)/4, (TILESIZE+190)/2))
            clock.tick(60)
        if len(self.BLUE_CHIPS_AMOUNT) == 2:
            # set the pygame window name
            pygame.display.set_caption('Image')
            # create a surface object, image is drawn on it.
            image = pygame.image.load('Images/KeyBlue_1.png')
            screen.blit(image, ((TILESIZE-10)/4, (TILESIZE+190)/2))
            image2 = pygame.image.load('Images/KeyBlue_1.png')
            screen.blit(image2, (TILESIZE+3, (TILESIZE+190)/2)) 
            clock.tick(60)
        
    def showgreenkey(self):
        if len(self.GREEN_CHIPS_AMOUNT) == 1:
            # set the pygame window name
            pygame.display.set_caption('Image')
            # create a surface object, image is drawn on it.
            image = pygame.image.load('Images/KeyGreen_1.png')
            screen.blit(image, ((TILESIZE-10)/4, (TILESIZE+260)/2))
            clock.tick(60)
        if len(self.GREEN_CHIPS_AMOUNT) == 2:
            # set the pygame window name
            pygame.display.set_caption('Image')
            # create a surface object, image is drawn on it.
            image = pygame.image.load('Images/KeyGreen_1.png')
            screen.blit(image, ((TILESIZE-10)/4, (TILESIZE+260)/2))
            image2 = pygame.image.load('Images/KeyGreen_1.png')
            screen.blit(image2, (TILESIZE+3, (TILESIZE+260)/2)) 
            clock.tick(60)
        
    def showyellowkey(self):
        if len(self.YELLOW_CHIPS_AMOUNT) == 1:
            # set the pygame window name
            pygame.display.set_caption('Image')
            # create a surface object, image is drawn on it.
            image = pygame.image.load('Images/KeyYellow_1.png')
            screen.blit(image, ((TILESIZE-10)/4, (TILESIZE+320)/2))
            clock.tick(60)
        if len(self.YELLOW_CHIPS_AMOUNT) == 2:
            # set the pygame window name
            pygame.display.set_caption('Image')
            # create a surface object, image is drawn on it.
            image = pygame.image.load('Images/KeyYellow_1.png')
            screen.blit(image, ((TILESIZE-10)/4, (TILESIZE+320)/2))
            image2 = pygame.image.load('Images/KeyYellow_1.png')
            screen.blit(image2, (TILESIZE+3, (TILESIZE+320)/2)) 
            clock.tick(60)

    def showfireelement(self):
        if len(self.FIRE_ELEMENT) == 1:
            # set the pygame window name
            pygame.display.set_caption('Image')
            # create a surface object, image is drawn on it.
            FIRE_IMAGE = pg.image.load('Images/Fire_Aspect.png')
            image = pg.transform.scale(FIRE_IMAGE,(TILESIZE,TILESIZE))
            screen.blit(image, (950,1))
            clock.tick(60)
    
    def showwaterelement(self):
        if len(self.WATER_ELEMENT) == 1:
            # set the pygame window name
            pygame.display.set_caption('Image')
            # create a surface object, image is drawn on it.
            WATER_IMAGE = pg.image.load('Images/platformPack_item007.png')
            image = pg.transform.scale(WATER_IMAGE,(TILESIZE,TILESIZE))
            screen.blit(image, (950,1))
            clock.tick(60)

    '''
    Description: Function for updating the inventory checking if the player has collected a token from the game or if an item was used.

    Arguments:
    arg1: self - uses all variables connected to the Player class


    Returns: Specify the return value of the function if there is
    ret1: 

    '''
    def inv_update(self, dx = 0, dy = 0):
        if self.redcollect(dx,dy):
            chips = 1
            self.RED_CHIPS_AMOUNT.append(chips)
        if len(self.RED_CHIPS_AMOUNT) >= 1:  
            self.showredkey()
        if self.reddoor_unlock(dx,dy):
            self.RED_CHIPS_AMOUNT.pop()
        if self.greencollect(dx,dy):
            chips = 1
            self.GREEN_CHIPS_AMOUNT.append(chips)
        if len(self.GREEN_CHIPS_AMOUNT) >= 1:  
            self.showgreenkey()
        if self.greendoor_unlock(dx,dy):
            self.GREEN_CHIPS_AMOUNT.pop()
        if self.bluecollect(dx,dy):
            chips = 1
            self.BLUE_CHIPS_AMOUNT.append(chips)
        if len(self.BLUE_CHIPS_AMOUNT) >= 1:  
            self.showbluekey()
        if self.bluedoor_unlock(dx,dy):
            self.BLUE_CHIPS_AMOUNT.pop()
        if self.yellowcollect(dx,dy):
            chips = 1
            self.YELLOW_CHIPS_AMOUNT.append(chips)
        if len(self.YELLOW_CHIPS_AMOUNT) >= 1:  
            self.showyellowkey()
        if self.yellowdoor_unlock(dx,dy):
            self.YELLOW_CHIPS_AMOUNT.pop()
        if self.chipscollect(dx,dy):
            chips = 1
            self.CHIPS_AMOUNT.append(chips)    
        if self.FireCollect(dx,dy):
            element = 2
            if len(self.WATER_ELEMENT) == 1:
                self.WATER_ELEMENT.pop()
            self.FIRE_ELEMENT.append(element)
        if len(self.FIRE_ELEMENT) == 1:
            self.showfireelement()
        if self.WaterCollect(dx,dy):
            element = 2
            if len(self.FIRE_ELEMENT) == 1:
                self.FIRE_ELEMENT.pop()
            self.WATER_ELEMENT.append(element)      
        if len(self.WATER_ELEMENT)==1:
            self.showwaterelement()

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

'''
    Description: Function for creating a sprite object and assigning an image for different walls

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

''' 

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/stone.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class GoldWall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/stone_gold_alt.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class DiamondWall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/stone_diamond_alt.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class CoalWall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/stone_coal_alt.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class Trunk(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pg.image.load('tile_05.png')
        picture = pg.image.load('Images/trunk_top.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

'''
    Description: Function for creating a sprite object and assigning an image for different Keys and checking for collisions

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

''' 
class RedKey(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.redkeys
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        KEY_IMAGE = pg.image.load('Images/KeyRed.png')
        self.image = pg.transform.scale(KEY_IMAGE,(TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE 
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Kcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Kcollision(dx,dy):
            self.kill()

class GreenKey(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.greenkeys
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/keyGreen.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Kcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Kcollision(dx,dy):
            self.kill() 

class YellowKey(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.yellowkeys
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/keyYellow.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Kcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Kcollision(dx,dy):
            self.kill()

class BlueKey(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.bluekeys
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/keyBlue.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Kcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Kcollision(dx,dy):
            self.kill() 

'''
    Description: Function for creating a sprite object and assigning an image for Chips and checking for collisions

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

''' 
class Chips(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.chips
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/ore_gold.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE 
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Dcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Dcollision(dx,dy):
            self.kill()

'''
    Description: Function for creating a sprite object and assigning an image for different doors and checking for collisions

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

''' 
class RedDoor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.reddoor
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        RED_DOOR_IMAGE = pg.image.load('Images/Reddoor.png')
        self.image = pg.transform.scale(RED_DOOR_IMAGE,(TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE 
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Dcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Dcollision(dx,dy):
            self.kill()

class GreenDoor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.greendoor
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/Greendoor.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE 
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Dcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Dcollision(dx,dy):
            self.kill()

class YellowDoor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.yellowdoor
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/Yellowdoor.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Dcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Dcollision(dx,dy):
            self.kill()

class BlueDoor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.bluedoor
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/Bluedoor.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Dcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Dcollision(dx,dy):
            self.kill()

'''
    Description: Function for creating a sprite object and assigning an image for the fire immunity and checking for collisions

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

''' 
class FireElement(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.fire_element
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        FIRE_ELEMENT_IMAGE = pg.image.load('Images/fireimmu.png')
        self.image = pg.transform.scale(FIRE_ELEMENT_IMAGE,(TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE 
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Dcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Dcollision(dx,dy):
            self.kill()

'''
    Description: Function for creating a sprite object and assigning an image for Fire tiles

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

''' 
class FireBlock(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.fire_block
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/lava(1).png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class FireBlock1(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.fire_block
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/f.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class FireBlock2(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.fire_block
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/fi.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class FireBlock3(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.fire_block
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/fir.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
    
class FireBlock4(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.fire_block
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/fire.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

'''
    Description: Function for creating a sprite object and assigning an image for water immunity and checking for collisions

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

''' 
class WaterElement(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.water_element
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        WATER_ELEMENT_IMAGE = pg.image.load('Images/waterimmu.png')
        self.image = pg.transform.scale(WATER_ELEMENT_IMAGE,(TILESIZE,TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE 
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Dcollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
    '''
    Description: Function for removing the object upon colliding with the player sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self, dx=0,dy=0):
        if self.player_Dcollision(dx,dy):
            self.kill()

'''
    Description: Function for creating a sprite object and assigning an image for water tiles

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

''' 
class WaterBlock(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.water_block
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/water(1).png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class WaterBlock1(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.water_block
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/w.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class WaterBlock2(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.water_block
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/wa.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class WaterBlock3(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.water_block
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/wat.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class WaterBlock4(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.water_block
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/wate.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

'''
    Description: Function for creating a sprite object and assigning an image for the Enemies and checking for collisions

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

''' 
class Enemy1(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemy
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/platformPack_tile012.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
        self.move_direction = 1
        self.move_counter = 0
    '''
    Description: Function for the movement of the enemy object

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 1000:
            self.move_direction *= -1
            self.move_counter = 0

class Enemy2(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemy
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/platformPack_tile024.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
        self.move_direction = 1
        self.move_counter = 0
    '''
    Description: Function for the movement of the enemy object

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self):
        self.rect.x -= self.move_direction
        self.move_counter += 1
        if self.move_counter > 1000:
            self.move_direction *= -1
            self.move_counter = 0

class Enemy3(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemy
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/platformPack_tile011.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
        self.move_direction = 1
        self.move_counter = 0
    '''
    Description: Function for the movement of the enemy object

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self):
        self.rect.y += self.move_direction
        self.move_counter += 1
        if self.move_counter > 500:
            self.move_direction *= -1
            self.move_counter = 0

class Enemy4(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemy
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/platformPack_tile023.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
        self.move_direction = 1
        self.move_counter = 0
    '''
    Description: Function for the movement of the enemy object

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self):
        self.rect.y -= self.move_direction
        self.move_counter += 1
        if self.move_counter > 500:
            self.move_direction *= -1
            self.move_counter = 0
    
class Enemy5(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemy
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/platformPack_tile012.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
        self.move_direction = 1
        self.move_counter = 0
    '''
    Description: Function for the movement of the enemy object

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 500:
            self.move_direction *= -1
            self.move_counter = 0

class Enemy6(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemy
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/platformPack_tile024.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
        self.move_direction = 1
        self.move_counter = 0
    '''
    Description: Function for the movement of the enemy object

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: 

    ''' 
    def update(self):
        self.rect.x -= self.move_direction
        self.move_counter += 1
        if self.move_counter > 500:
            self.move_direction *= -1
            self.move_counter = 0
    

'''
    Description: Function for creating a sprite object and assigning an image for Slide tile

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

'''     
class RSlide(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.rslide_tile
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/platformIndustrial_070.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class LSlide(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.lslide_tile
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/platformIndustrial_098.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class USlide(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.uslide_tile
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/platformIndustrial_084.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

class DSlide(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.dslide_tile
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/platformIndustrial_112.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

'''
    Description: Function for creating a sprite object and assigning an image for thief tile

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

'''   
class Reset(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.reset_tile
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/boxItem.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE

'''
    Description: Function for creating a sprite object and assigning an image for the Exit and checking for collisions

    Arguments:
    arg1: self - uses all variables connected to the Player class
    arg2: pygame.image.load - used for opening/loading an image file
    arg3: pg.transform.scale - used for resizing an image 

    Returns: Specify the return value of the function if there is
    ret1: 

''' 
class Exit(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.exit
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        picture = pg.image.load('Images/Exit.png')
        self.image = pg.transform.scale(picture, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y 
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE
    '''
    Description: Function for the collision of the player to the sprite

    Arguments:
    arg1: self - uses all variables connected to the class


    Returns: Specify the return value of the function if there is
    ret1: bool - returns true if player coordinates matches the object's coordinates

    ''' 
    def player_Ecollision(self, dx = 0, dy = 0):
        for player in self.game.players:
           if player.x == self.x + dx and player.y == self.y + dy:
                return True
        return False
        




   
    

    




