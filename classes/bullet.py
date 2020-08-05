import pygame

class Bullet(object):
    def __init__(self, x, y, Screen):
        self.x = x
        self.y = y
        self.velocity = -20
        self.acc = -0 
        self.img = pygame.image.load('src/img/Flame_01.png')
        self.img = pygame.transform.scale(self.img, (10,10))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.hitbox = [self.x, self.y, self.width, self.height]
            
    def draw(self, Screen, s_height):
        """ Draw the bullet if is on screen""" 
        if self.y in range(-200,s_height): 
            Screen.blit(self.img, (self.x, self.y))
            #HITBOX
            #pygame.draw.rect(Screen, (255,0,0),  self.hitbox, 2)

    def update(self):
        """Bullets always go up""" 
        self.velocity += self.acc
        self.y += self.velocity 
        self.hitbox[1] += self.velocity
