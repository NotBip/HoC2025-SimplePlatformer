import pygame
from player import Player
from background import Background
from tiles import Tiles

# Initalizing Variables
SCREEN_SIZE = (700,500)
DARK_GRAY = (50,50,50)
FPS = 60
running = True
objects = []
tile_size = 36

#init
pygame.init()
screen = pygame.display.set_mode((720, 720))  
pygame.display.set_caption("Simple Platformer Game")
clock = pygame.time.Clock()

# Background
background = Background(0, 0, 0, 0, pygame.image.load('Images/BG/BG.png'))
objects.append(background)

# Tiles
tiles = Tiles(tile_size)
objects.append(tiles)

# player
player_image = pygame.image.load('Images/Player/player_00.png')
player = Player(0, 0, tiles.tileList)


while running:

    # Set Fps
    clock.tick(FPS)

    # Initialize Events
    event = pygame.event.get()
    keys = pygame.key.get_pressed()

    for e in event:
        if e.type == pygame.QUIT:
            running = False

    # update all the objects first then player
    for obj in objects:
        obj.update(keys)
    player.update(keys)

    # draw all the objects first then draw the player
    for obj in objects:
        obj.draw(screen)    
    player.draw(screen)

    # Display
    pygame.display.flip()




pygame.quit()