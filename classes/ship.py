import pygame
from classes.bullet import Bullet

class Ship():
    def __init__(self, color, ship_type, Screen, Screen_width, Screen_height):
        self.x = 2 
        self.y = 0
        self.velocity = 10
        self.acc = 0.1
        self.hp = 3
        self.color = color
        self.ship_type = ship_type
        self.img_path = "src/img/spaceships/"+ship_type+"/Spaceship_0"+ship_type+"_"+color+".png"
        self.img = (pygame.image.load(self.img_path))
        self.width = self.img.get_width()/4.5
        self.height = self.img.get_height()/4.5
        self.img = pygame.transform.scale(self.img, (int(self.width),int(self.height))) 
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.bullets = []

    def shoot(self, KEYS, K_space, Screen, S_height):
        """Create the bullets and append it"""
    
        if KEYS[K_space]:
            B = Bullet(self.x+self.width/2, self.y, Screen)
            self.bullets.append(B)


    def draw(self, Screen, S_width, S_height):
        """Draw where the ship is located, and the bullets"""

        if self.hp > 0:
            Screen.blit(self.img, (self.x, self.y))
            #Just while coding
            pygame.draw.rect(Screen, (255,0,0),  self.hitbox, 2)

        for Bs in self.bullets: 
            Bs.update()
            Bs.draw(Screen, S_height)

            #Remove if is not on Screen
            if Bs.y < 0: 
               self.bullets.remove(Bs) 


    def update(self, move_to, left, right, up, down, Screen_width, Screen_height):
        """This funciton implement the movement of the character/ship"""
        if move_to[left] and self.x  > self.velocity:
            self.x -= self.velocity
            self.hitbox[0] -= self.velocity

        if move_to[right] and self.x + self.width + self.velocity < Screen_width:
            self.x += self.velocity
            self.hitbox[0] += self.velocity

        if move_to[up] and self.y > self.velocity:
            self.y -= self.velocity
            self.hitbox[1] -= self.velocity

        if move_to[down] and self.y + self.height + self.velocity < Screen_height:
            self.y += self.velocity
            self.hitbox[1] += self.velocity
        
            
