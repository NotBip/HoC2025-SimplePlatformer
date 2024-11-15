class Background:
    def __init__(self, x, y, w, h, image):
        self.x, self.y, self.w, self.h, self.image = x, y, w, h, image

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, keys):
        pass