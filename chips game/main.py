import pygame
import sys
from os import path
from pygame import mixer
from settings import *
from sprites import *
from map_camera import *

#Variable Initiation
mixer.init()
CURRENT_LEVEL = [0]

'''
Description: Function for creating the Game class/object

Arguments:
arg1: self - serves as a pointer to the game class. | e.g. self.screen means that screen is a variable of the game object.

Returns: Specify the return value of the function if there is
ret1: 

'''
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        #command for hold key
        pygame.key.set_repeat(50, 90)

    '''
    Description: Function for creating a new game based on the current level of the player

    Arguments:
    arg1: self - points all variables created to the game class 

    Returns: Specify the return value of the function if there is
    ret1: 

    '''
    def new(self):
        # selects the main folder and map file to be used.
        main_folder = path.dirname(__file__)
        self.map = Map(path.join(main_folder,f'floor{str(len(CURRENT_LEVEL))}.txt'))
        # Assigns the sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.redkeys = pygame.sprite.Group()
        self.greenkeys = pygame.sprite.Group()
        self.bluekeys = pygame.sprite.Group()
        self.yellowkeys = pygame.sprite.Group()
        self.reddoor = pygame.sprite.Group()
        self.greendoor = pygame.sprite.Group()
        self.bluedoor = pygame.sprite.Group()
        self.yellowdoor = pygame.sprite.Group()
        self.chips = pygame.sprite.Group()
        self.exit = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.fire_element = pygame.sprite.Group()
        self.fire_block = pygame.sprite.Group()
        self.water_element = pygame.sprite.Group()
        self.water_block = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.rslide_tile = pygame.sprite.Group()
        self.lslide_tile = pygame.sprite.Group()
        self.uslide_tile = pygame.sprite.Group()
        self.dslide_tile = pygame.sprite.Group()
        self.reset_tile = pygame.sprite.Group()

        #Traverses the txt file to acquire coordinates for wall placement.
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                #player spawn
                if tile == 'a':
                    self.player = Player(self, col, row)
                #wall placement
                if tile == 'w':
                    Wall(self, col, row)
                if tile == '1':
                    GoldWall(self, col, row)
                if tile == '2':
                    DiamondWall(self, col, row)
                if tile == '3':
                    CoalWall(self, col, row)
                if tile == '4':
                    Trunk(self, col, row)
                if tile == 'E':
                    Exit(self, col, row)
                #Keys, Chips, Doors, Elements, and Tiles Placements
                if tile == 'c':
                    Chips(self, col, row)
                if tile == 'g':
                    GreenKey(self, col, row)
                if tile == 'G':
                    GreenDoor(self, col, row)
                if tile == 'r':
                    RedKey(self, col, row)
                if tile == 'R':
                    RedDoor(self,col,row)
                if tile == 'b':
                    BlueKey(self, col, row)
                if tile == 'B':
                    BlueDoor(self, col, row)
                if tile == 'y':
                    YellowKey(self, col, row)
                if tile == 'Y':
                    YellowDoor(self, col, row)
                if tile == 'f':
                    FireElement(self,col,row)
                if tile == ']':
                    FireBlock(self,col,row)
                if tile == 'F':
                    FireBlock1(self,col,row)
                if tile == '(':
                    FireBlock2(self,col,row)
                if tile == ')':
                    FireBlock3(self,col,row)
                if tile == '[':
                    FireBlock4(self,col,row)
                if tile == 't':
                    WaterElement(self,col,row)
                if tile == 'T':
                    WaterBlock(self,col,row)
                if tile == '5':
                    WaterBlock1(self,col,row)
                if tile == '6':
                    WaterBlock2(self,col,row)
                if tile == '7':
                    WaterBlock3(self,col,row)
                if tile == '8':
                    WaterBlock4(self,col,row)
                if tile == '>':
                    RSlide(self,col,row)
                if tile == '<':
                    LSlide(self,col,row)
                if tile == 'u':
                    USlide(self,col,row)
                if tile == 'd':
                    DSlide(self,col,row)
                if tile == 'z':
                    Reset(self,col,row)
                #Enemy Placements
                if tile == 'N':
                    Enemy1(self,col,row)
                if tile == 'n':
                    Enemy2(self,col,row)
                if tile == 'M':
                    Enemy3(self,col,row)
                if tile == 'm':
                    Enemy4(self,col,row)
                if tile == '+':
                    Enemy5(self,col,row)
                if tile == '-':
                    Enemy6(self,col,row)
        # Camera assignment
        self.cam = Camera(self.map.width,self.map.height)
    '''
    Description: Function for the game loop and catches all events while playing

    Arguments:
    arg1: self - uses all variables connected to the game class

    Returns: Specify the return value of the function if there is
    ret1: 

    '''
    def run(self):
        # game loop - set self.playing = False to end the game
        game_folder = path.dirname(__file__)
        music_folder = path.join(game_folder, 'Music')
        self.bg_music = path.join(music_folder, 'bg.mp3')
        mixer.music.load(self.bg_music)
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)

        self.playing = True
        while self.playing:
            
            self.dt = self.clock.tick(FPS) / 1000
            self.commands()
            self.update()
            self.draw()
            self.display()
            self.player.inv_update()
        
            if self.player.Reset_Touch():
                    self.new()
                    
            if self.player.RSlide_Touch():
                self.player.move(dx = 2)
            
            if self.player.LSlide_Touch():
                self.player.move(dx = -2)
            
            if self.player.USlide_Touch():
                self.player.move(dy = -2)
            
            if self.player.DSlide_Touch():
                self.player.move(dy = 2)

            if self.player.FireTouch():
                self.player.kill()
                if len(CURRENT_LEVEL) == 2:
                    CURRENT_LEVEL.pop()
                if len(CURRENT_LEVEL) == 3:
                    CURRENT_LEVEL.pop()
                    CURRENT_LEVEL.pop()
                self.playing = False

            if self.player.WaterTouch():
                self.player.kill()
                if len(CURRENT_LEVEL) == 2:
                    CURRENT_LEVEL.pop()
                if len(CURRENT_LEVEL) == 3:
                    CURRENT_LEVEL.pop()
                    CURRENT_LEVEL.pop()
                self.playing = False

            if self.player.EnemyTouch():
                self.player.kill()
                if len(CURRENT_LEVEL) == 2:
                    CURRENT_LEVEL.pop()
                if len(CURRENT_LEVEL) == 3:
                    CURRENT_LEVEL.pop()
                    CURRENT_LEVEL.pop()
                self.playing = False

            if self.player.exit_unlock():
                level = 0
                if len(CURRENT_LEVEL) == 3:
                    CURRENT_LEVEL.pop()
                    CURRENT_LEVEL.pop()
                    CURRENT_LEVEL.pop()
                    self.show_go_screen()
                if len(CURRENT_LEVEL) < 4:
                    CURRENT_LEVEL.append(level)
                    self.new()
                    
    '''
    Description: Function for aligning and drawing text on the screen

    Arguments:
    arg1: self - uses all variables connected to the game class
    arg2: text - the text/string to be displayed
    arg3: font_name - font style to be used
    arg4: size - font size of the text
    arg5: color - color of the text in RGB input
    arg6: x - x-coordinate of the text
    arg7: y - y-coordinate of the text
    arg8: align - alignment of the text based on the canvas

    Returns: Specify the return value of the function if there is
    ret1: 

    '''        
    def draw_text(self, text, font_name, size, color, x, y, align):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)
    '''
    Description: Function for displaying text and the inventory on the screen

    Arguments:
    arg1: self - uses all variables connected to the game class along with the functions connected to the sprites


    Returns: Specify the return value of the function if there is
    ret1: 

    '''       
    def display(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'Fonts')
        self.title_font = path.join(img_folder, 'KenneyMiniSquare.ttf')
        chips = len(self.player.CHIPS_AMOUNT)
        chipsneed = len(self.player.CHIPS1_AMOUNT)
        self.draw_text( 'Chips collected: ' + str(chips), self.title_font, 30, WHITE, TILESIZE/ 4, (TILESIZE+30) / 2, align="nw")
        self.draw_text("Chips to be Collected: " + str(chipsneed), self.title_font, 30, WHITE, TILESIZE / 4, TILESIZE / 4, align="nw")
        self.draw_text("Inventory: ", self.title_font, 20, WHITE, TILESIZE / 4, (TILESIZE+100) / 2, align="nw")
        self.draw_text( "Current Immunity: ", self.title_font, 30, WHITE, 820, 30, align = 'center')
        self.player.showyellowkey()
        self.player.showbluekey()
        self.player.showgreenkey()
        self.player.showredkey()
        self.player.showfireelement()
        self.player.showwaterelement()
        pygame.display.update()
    '''
    Description: Function for quitting the program 

    Arguments:
    arg1: self - uses all variables connected to the game class


    Returns: Specify the return value of the function if there is
    ret1: 

    '''       
    def quit(self):
        pygame.quit()
        sys.exit()
    '''
    Description: Function for updating all sprites with respect to the update function called in each one.

    Arguments:
    arg1: self - uses all variables connected to the game class

    Returns: Specify the return value of the function if there is
    ret1: 

    '''       
    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.cam.follow(self.player)
   
    #tanggalin na ata natin to di na need
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    '''
    Description: Function for displaying all sprites of the game

    Arguments:
    arg1: self - uses all variables connected to the game class


    Returns: Specify the return value of the function if there is
    ret1: 

    '''       
    def draw(self):
        self.screen.fill(BGCOLOR)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.cam.moveCam(sprite))
    '''
    Description: Function for getting user input 

    Arguments:
    arg1: self - uses all variables connected to the game class


    Returns: Specify the return value of the function if there is
    ret1: 

    '''           
    def commands(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                #Player input 
                keys_pressed = pygame.key.get_pressed()
                if  keys_pressed[pygame.K_LEFT]:
                    self.player.image = pg.transform.scale(PLAYER_LEFT_IMAGE,(TILESIZE,TILESIZE))
                    self.player.move(dx = -VEL)
                    self.player.inv_update()
                       
                if keys_pressed[pygame.K_RIGHT]:
                    self.player.image = pg.transform.scale(PLAYER_RIGHT_IMAGE,(TILESIZE,TILESIZE))
                    self.player.move(dx= VEL)
                    self.player.inv_update()
                    
                if keys_pressed[pygame.K_UP]:
                    self.player.image = pg.transform.scale(PLAYER_BACK_IMAGE,(TILESIZE,TILESIZE))
                    self.player.move(dy= -VEL)
                    self.player.inv_update()
                    
                if keys_pressed[pygame.K_DOWN]:
                    self.player.image = pg.transform.scale(PLAYER_FRONT_IMAGE,(TILESIZE,TILESIZE))
                    self.player.move(dy= VEL)
                    self.player.inv_update()            

    '''
    Description: Function for displaying start screen

    Arguments:
    arg1: self - uses all variables connected to the game class


    Returns: Specify the return value of the function if there is
    ret1: 

    '''              
    def show_start_screen(self):
        game_folder = path.dirname(__file__)
        music_folder = path.join(game_folder, 'Music')
        self.start_music = path.join(music_folder, 'start.mp3')
        mixer.music.load(self.start_music)
        mixer.music.set_volume(0.2)
        mixer.music.play()

        self.screen.fill(BGCOLOR)
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'Fonts')
        self.title_font = path.join(img_folder, 'KenneyMiniSquare.ttf')
        self.draw_text("Cheap's Challenge", self.title_font, 74, WHITE, 500, 300, align="center")
        self.draw_text("Press S to start.", self.title_font, 40, RED, 500, 400, align="s")
        self.draw_text("Press ESC to Exit.", self.title_font, 20, RED, 500, 700, align="s")
        self.draw_text("Creators: Erica Mae Antonino & Marvin Andrew Rosales", self.title_font, 20, WHITE, 500, 750, align="s")
        pygame.display.flip()
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key== pg.K_s:
                        waiting = False
                        return True
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
    '''
    Description: Function for displaying game over screen 

    Arguments:
    arg1: self - uses all variables connected to the game class


    Returns: Specify the return value of the function if there is
    ret1: 

    '''  
    def show_go_screen(self):
            game_folder = path.dirname(__file__)
            music_folder = path.join(game_folder, 'Music')
            self.go_music = path.join(music_folder, 'go.wav')
            mixer.music.load(self.go_music)
            mixer.music.set_volume(0.1)
            mixer.music.play()

            self.screen.fill(BGCOLOR)
            game_folder = path.dirname(__file__)
            img_folder = path.join(game_folder, 'Fonts')
            self.title_font = path.join(img_folder, 'KenneyMiniSquare.ttf')
            self.draw_text("GAME OVER", self.title_font, 74, WHITE, 500, 300, align="center")
            self.draw_text("Press R to restart.", self.title_font, 50, RED, 500, 400, align="s")
            self.draw_text("Press ESC to Exit.", self.title_font, 20, RED, 500, 700, align="s")
            pygame.display.flip()
            pg.event.wait()
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        self.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key== pg.K_r:
                            waiting = False
                        if event.key == pygame.K_ESCAPE:
                            self.quit()
                   

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()
        
