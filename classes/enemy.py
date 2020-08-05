from classes.bullet import Bullet
import pygame
import random

class Enemy(object):
    def __init__(self, Screen, S_width, S_height):
        self.width = 100
        self.height = 50
        self.x = random.uniform(0, S_width-self.width)
        self.y = random.uniform(0, S_height/10) 
        self.velocity = 10
        self.hp = 100
        self.color = (123,9,250) # bruh
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.img = pygame.Rect(self.x, self.y, self.width, self.height)


    def draw(self, Screen):
        """Just Draw where the "enemy" is """
        pygame.draw.rect(Screen, self.color,  self.img)
            

    def update(self, S_width, S_height):
        """Update logic things"""
        self.y += self.velocity
        self.hitbox[1] += self.velocity 
        self.img = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.hp < 0 or self.y-self.height > S_height:
            """Relocate if hp is below 0 or is below the Screen"""

            self.x = random.uniform(0, S_width-self.width) 
            self.y = random.uniform(0, S_height/10) 
            self.img = pygame.Rect(self.x, self.y, self.width, self.height)
            self.hitbox = [self.x, self.y, self.width, self.height]
            self.hp = 100

    def get_hit(self, other_hitbox):
        """HP -= 1 if get hit by bullet, and destroy that bullet"""
        
        for i in other_hitbox:
            width_comparation = i.hitbox[0] >= self.x and i.hitbox[0] <= self.x + self.width
            height_comparation = i.hitbox[1] >= self.y and i.hitbox[1] <= self.y + self.height   
            if width_comparation and height_comparation:
                other_hitbox.remove(i) 
                self.hp -= 1
                print(self.hp)
