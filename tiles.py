import pygame

world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 14, 14, 15, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 5, 5, 6, 0, 0, 0, 0, 0, 0, 0, 0], 
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 
    [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    ]

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

class Tiles:
    
    def __init__(self, tile_size):

        self.tileList = []
        self.tile_size = tile_size
        self.loadTileList()

    def draw(self, screen):
        for tile in self.tileList:
            screen.blit(tile[0], tile[1])


    def loadTileList(self): 
        for row in range(20):
            for col in range(20):
                if world_data[row][col] > 0:
                    if world_data[row][col] == 1:
                        img = pygame.transform.scale(grass_topLeft, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 2:
                        img = pygame.transform.scale(grass_topMid, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 3:
                        img = pygame.transform.scale(grass_topRight, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 4:
                        img = pygame.transform.scale(grass_midLeft, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 5:
                        img = pygame.transform.scale(grass_midMid, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 6:
                        img = pygame.transform.scale(grass_midRight, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 7:
                        img = pygame.transform.scale(grass_midConnectLeft, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 8:
                        img = pygame.transform.scale(grass_bottomLeft, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 9:
                        img = pygame.transform.scale(grass_bottomMid, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 10:
                        img = pygame.transform.scale(grass_bottomRight, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                    if world_data[row][col] == 11:
                        img = pygame.transform.scale(grass_midConnectRight, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 12:
                        img = pygame.transform.scale(dirt_bottomLeft, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 13:
                        img = pygame.transform.scale(floating_grass_left, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 14:
                        img = pygame.transform.scale(floating_grass_mid, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 15:
                        img = pygame.transform.scale(floating_grass_right, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)
                    if world_data[row][col] == 16:
                        img = pygame.transform.scale(dirt_bottomRight, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()   
                        img_rect.x = col * self.tile_size
                        img_rect.y = row * self.tile_size
                        tile = (img, img_rect)
                        self.tileList.append(tile)

    def update(self, keys):
        pass
