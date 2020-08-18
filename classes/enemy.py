from classes.bullet import Bullet
import pygame
import random

class Enemy(object):
    def __init__(self, Screen, S_width, S_height):
        self.width = 100
        self.height = 50
        self.x = random.uniform(0, S_width-self.width)
        self.y = random.uniform(0, S_height/10) 
        self.lost_count = 0
        self.velocity = 5
        self.hp = 50
        self.color = (153, 255, 153)# bruh
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.img = pygame.Rect(self.x, self.y, self.width, self.height)


    def relocate(self, S_width, S_height):
        '''Relocate the box'''
        self.x = random.uniform(0, S_width-self.width) 
        self.y = random.uniform(0, S_height/10) 
        self.img = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.hp = 50

    def draw(self, Screen):
        """Just Draw where the "enemy" is """
        pygame.draw.rect(Screen, self.color,  self.img)
        #hitbox    
        #pygame.draw.rect(Screen, (255,0,0),  self.hitbox, 2)

    def update(self, S_width, S_height):
        """Update logic things"""
        self.y += self.velocity
        self.hitbox[1] += self.velocity 
        self.img = pygame.Rect(self.x, self.y, self.width, self.height)

        if self.hp < 1:
            self.lost_count += 1
            #print("Lost count: ",self.lost_count)

        if self.hp < 1 or self.y+self.height > S_height:
            self.relocate(S_width, S_height)
        

    def get_hitbox(self):
        '''Return Hitbox'''
        return self.hitbox

    def get_score(self):
        return (50 - self.hp) 

    def get_hit(self, other_hitbox):
        """HP -= 1 if get hit by bullet, and destroy that bullet"""
        for i in other_hitbox:
            width_comparation = i.hitbox[0] >= self.x and i.hitbox[0] <= self.x + self.width
            height_comparation = i.hitbox[1] >= self.y and i.hitbox[1] <= self.y + self.height   
            if width_comparation and height_comparation:
                other_hitbox.remove(i) 
                self.hp -= 1
#                print(self.hp)
