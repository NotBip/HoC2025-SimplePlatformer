import pygame

class Player:
    def __init__(self, x, y, tileList):
        self.images_right = []
        self.images_left = []
        self.tileList = tileList
        self.index = 0
        self.counter = 0
        self.aniSpeed = 5

        for num in range(1, 5):
            image_right = pygame.image.load(f'Images/Player/player_0{num}.png')
            image_right = pygame.transform.scale(image_right, (54, 54))
            image_left = pygame.transform.flip(image_right, True, False)
            self.images_left.append(image_left)
            self.images_right.append(image_right)

        self.image = self.images_right[self.index]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.movSpeed = 3

        self.jumpMax = 15
        self.vel_y = 0 
        self.jumped = False
        self.maxGravAcc = 10

        self.direction = 0


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, keys):
        
        dx = 0
        dy = 0

        if keys[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -self.jumpMax
            self.jumped = True

        if keys[pygame.K_SPACE] == False:
            self.jumped = False

        if keys[pygame.K_d]:
            dx += self.movSpeed
            self.counter += 1
            self.direction = 1

        elif keys[pygame.K_a]:
            dx -= self.movSpeed
            self.counter += 1
            self.direction = -1

        if keys[pygame.K_d] == False and keys[pygame.K_a] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            elif self.direction == -1: 
                self.image = self.images_left[self.index]

        if self.counter > self.aniSpeed:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            elif self.direction == -1: 
                self.image = self.images_left[self.index]



        # gravity
        self.vel_y += 1
        if self.vel_y > self.maxGravAcc:
            self.vel_y = self.maxGravAcc
        dy += self.vel_y

        #   
        for tile in self.tileList:
            # horizontal collision
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            # vertical collision
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check above
                if self.vel_y < 0: 
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # check below   
                elif self.vel_y >= 0: 
                    dy = tile[1].top - self.rect.bottom
        
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > 720:
            self.rect.bottom = 720
            dy = 0



