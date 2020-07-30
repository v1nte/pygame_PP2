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
        self.img_path = "src/img/Spaceships/"+ship_type+"/Spaceship_"+ship_type+"_"+color+".png"
        self.img = (pygame.image.load(self.img_path))
        self.img = pygame.transform.scale(self.img, (100,100))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.hitbox = (self.x+self.width//2, self.x-self.width//2, self.y+self.height//2, self.y-self.height//2)
        self.bullets = []

    def shoot(self, KEYS, K_space, Screen, S_height):
        if KEYS[K_space]:
            B = Bullet(self.x, self.y, Screen)
            self.bullets.append(B)

    def draw(self, screen, S_width, S_height):
        """Draw where the ship is located"""
        if self.hp > 0:
            screen.blit(self.img, (self.x, self.y))

        for Bs in self.bullets: 
            Bs.update()
            Bs.draw(screen, S_height)

            #Pop if is not on Screen
            if Bs.y < 0: 
               self.bullets.remove(Bs) 

        #   self.hitbox = (self.x+self.width//2, self.x-self.width//2, self.y+self.height//2, self.y-self.height//2)

    def update(self, move_to, left, right, up, down, Screen_width, Screen_height):
        """This funciton implement the movement of the character/ship"""
        if move_to[left] and self.x  > self.velocity:
            self.x -= self.velocity

        if move_to[right] and self.x + self.width + self.velocity < Screen_width:
            self.x += self.velocity

        if move_to[up] and self.y > self.velocity:
            self.y -= self.velocity

        if move_to[down] and self.y + self.height + self.velocity < Screen_height:
            self.y += self.velocity
        
            
