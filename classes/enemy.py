from classes.bullet import Bullet
import pygame
import random

class Enemy(object):
    def __init__(self, Screen,  S_width, S_height):
        self.x = S_width/2
        self.y = S_height/2
        self.velocity = 10
        self.hp = 10
        self.color = (0,0,250)
        self.width = 100
        self.height = 50
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.img = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y += self.velocity
        self.hitbox[1] += self.velocity 

    def draw(self, Screen):
        if self.hp > 0:
            pygame.draw.rect(Screen, (255,0,0),  self.img)
        #Screen.blit(self.img, (self.x, self.y))

    def get_hit(self, other_hitbox):
        for i in other_hitbox:
            width_comparation = i.hitbox[0] >= self.x and i.hitbox[0] <= self.x + self.width
            height_comparation = i.hitbox[1] >= self.y and i.hitbox[1] <= self.y + self.height   
            if width_comparation and height_comparation:
                self.hp -= 1
                print(self.hp)
