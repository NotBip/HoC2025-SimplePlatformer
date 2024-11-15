import pygame
import pickle
from os import path


pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
tile_size = 36	
cols = 20
margin = 100
screen_width = tile_size * cols
screen_height = (tile_size * cols)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Editor')


#load images
bg_img = pygame.image.load('Images/BG/BG.png')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))

grass_topLeft = pygame.image.load('Images/Tiles/1.png')
grass_topMid = pygame.image.load('Images/Tiles/2.png')
grass_topRight = pygame.image.load('Images/Tiles/3.png')
grass_midLeft = pygame.image.load('Images/Tiles/4.png')
grass_midMid = pygame.image.load('Images/Tiles/5.png')
grass_midRight = pygame.image.load('Images/Tiles/6.png')
grass_midConnectLeft = pygame.image.load('Images/Tiles/7.png')
grass_bottomLeft = pygame.image.load('Images/Tiles/8.png')
grass_bottomMid = pygame.image.load('Images/Tiles/9.png')
grass_bottomRight = pygame.image.load('Images/Tiles/10.png')
grass_midConnectRight = pygame.image.load('Images/Tiles/11.png')
dirt_bottomLeft = pygame.image.load('Images/Tiles/12.png')
floating_grass_left = pygame.image.load('Images/Tiles/13.png')
floating_grass_mid = pygame.image.load('Images/Tiles/14.png')
floating_grass_right = pygame.image.load('Images/Tiles/15.png')
dirt_bottomRight = pygame.image.load('Images/Tiles/16.png')

#define game variables
clicked = False
level = 1
printed = False

#define colours
white = (255, 255, 255)
green = (144, 201, 120)

font = pygame.font.SysFont('Futura', 24)

#create empty tile list
world_data = []
for row in range(20):
	r = [0] * 20
	world_data.append(r)

#create boundary
for tile in range(0, 20):
	world_data[19][tile] = 5
	world_data[18][tile] = 5
	world_data[17][tile] = 2

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def draw_grid():
	for c in range(21):
		#vertical lines
		pygame.draw.line(screen, white, (c * tile_size, 0), (c * tile_size, screen_height - margin))
		#horizontal lines
		pygame.draw.line(screen, white, (0, c * tile_size), (screen_width, c * tile_size))


def draw_world():
	for row in range(20):
		for col in range(20):
			if world_data[row][col] > 0:
				if world_data[row][col] == 1:
					#dirt blocks
					img = pygame.transform.scale(grass_topLeft, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 2:
					#grass blocks
					img = pygame.transform.scale(grass_topMid, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 3:
					#enemy blocks
					img = pygame.transform.scale(grass_topRight, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 4:
					#horizontally moving platform
					img = pygame.transform.scale(grass_midLeft, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 5:
					#vertically moving platform
					img = pygame.transform.scale(grass_midMid, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 6:
					#lava
					img = pygame.transform.scale(grass_midRight, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 7:
					#coin
					img = pygame.transform.scale(grass_midConnectLeft, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 8:
					#exit
					img = pygame.transform.scale(grass_bottomLeft, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 9:
					#exit
					img = pygame.transform.scale(grass_bottomMid, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 10:
					#exit
					img = pygame.transform.scale(grass_bottomRight, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 11:
					#exit
					img = pygame.transform.scale(grass_midConnectRight, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 12:
					#exit
					img = pygame.transform.scale(dirt_bottomLeft, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 13:
					#exit
					img = pygame.transform.scale(floating_grass_left, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 14:
					#exit
					img = pygame.transform.scale(floating_grass_mid, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 15:
					#exit
					img = pygame.transform.scale(floating_grass_right, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 16:
					#exit
					img = pygame.transform.scale(dirt_bottomRight, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))


#main game loop
run = True
while run:

	clock.tick(fps)

	#draw background
	screen.fill(green)
	screen.blit(bg_img, (0, 0))

	keys = pygame.key.get_pressed()

	#load and save level
	if keys[pygame.K_e] and printed == False:
		printed = True
		print(world_data)
	
	if keys[pygame.K_e] == False:
		printed = False



	#show the grid and draw the level tiles
	draw_grid()
	draw_world()


	#text showing current level
	draw_text(f'Level: {level}', font, white, tile_size, screen_height - 60)
	draw_text('Press UP or DOWN to change level', font, white, tile_size, screen_height - 40)

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
		#mouseclicks to change tiles
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
			pos = pygame.mouse.get_pos()
			x = pos[0] // tile_size
			y = pos[1] // tile_size
			#check that the coordinates are within the tile area
			if x < 20 and y < 20:
				#update tile value
				if pygame.mouse.get_pressed()[0] == 1:
					world_data[y][x] += 1
					if world_data[y][x] > 16:
						world_data[y][x] = 0
				elif pygame.mouse.get_pressed()[2] == 1:
					world_data[y][x] -= 1
					if world_data[y][x] < 0:
						world_data[y][x] = 16
		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False
		#up and down key presses to change level number
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				level += 1
			elif event.key == pygame.K_DOWN and level > 1:
				level -= 1

	#update game display window
	pygame.display.update()

pygame.quit()