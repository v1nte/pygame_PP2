import pygame
from classes.bullet import Bullet

class Ship():
    def __init__(self, color, ship_type, Screen, Screen_width, Screen_height):
        self.x = 300
        self.y = 800
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

    def get_bullets(self):
        """Get Bullets"""
        return self.bullets
    def get_hp(self):
        '''return HP'''
        return self.hp

    def shoot(self, KEYS, K_space, Screen, S_height):
        """Create the bullets and append it"""
    
        if KEYS[K_space]:
            B = Bullet(self.x+self.width/2, self.y, Screen)
            self.bullets.append(B)


    def draw(self, Screen, S_width, S_height):
        """Draw where the ship is located, and the bullets"""

        if self.hp > 0:
            Screen.blit(self.img, (self.x, self.y))
            #Just while coding - HITBOX
            #pygame.draw.rect(Screen, (255,0,0),  self.hitbox, 2)

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
    
    def get_hit(self, enemy, S_width, S_height):
        '''HP -= 1 if get hit by enemy'''
        w_comparation1 = enemy.hitbox[0] >= self.x and enemy.hitbox[0] <= self.x + self.height 
        h_comparation1 = enemy.hitbox[1] >= self.y and enemy.hitbox[1] <= self.y + self.height   
        comp1 = w_comparation1 and h_comparation1
        
        w_comparation2 = enemy.hitbox[0] + enemy.hitbox[2] >= self.x and enemy.hitbox[0] <= self.x + self.height 
        h_comparation2 = enemy.hitbox[1] + enemy.hitbox[3]>= self.y and enemy.hitbox[1] <= self.y + self.height   
        comp2 = w_comparation2 and h_comparation2

        if comp1 or comp2:
            enemy.relocate(S_width, S_height)
            self.hp -= 1
            print("Ship HP: ",self.hp)
        if enemy.y + enemy.height + 5 > S_height:
            self.hp -= 1
            print("Ship HP: ",self.hp)
