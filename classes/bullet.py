import pygame

class Bullet(object):
    def __init__(self, x, y, Screen):
        self.x = x
        self.y = y
        self.velocity = 25
        self.acc = 0.5
        self.img = pygame.image.load('src/img/Flame_01.png')

        self.velocity -= self.acc
        self.y -= self.velocity 

    def draw(self, Screen, s_width, s_height):
        """ Draw the bullet if is on screen""" 
        if self.x in range(s_width) and self.y in range(s_height):
            Screen.blit(self.img, (self.x, self.y))

    def update(self):
        """Bullets always go up""" 
        self.velocity -= self.acc
        self.y -= self.velocity 
