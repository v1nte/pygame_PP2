import pygame

class Bullet(object):
    def __init__(self, x, y, Screen):
        self.x = x
        self.y = y
        self.velocity = -25
        self.acc = -0.5
        self.img = pygame.image.load('src/img/Flame_01.png')
        self.img = pygame.transform.scale(self.img, (90,90))
        self.velocity -= self.acc
        self.y -= self.velocity 
    def __del__(self):
        """Destroy the object to don't waste memory""" 
        pass
            
    def draw(self, Screen, s_height):
        """ Draw the bullet if is on screen""" 
        if self.y in range(-200,s_height): 
            Screen.blit(self.img, (self.x, self.y))

    def update(self):
        """Bullets always go up""" 
        self.velocity += self.acc
        self.y += self.velocity 
