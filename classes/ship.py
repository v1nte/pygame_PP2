import pygame
from classes.bullet import Bullet
from pygame import mixer

class Ship():
    def __init__(self, color, ship_type, Screen, Screen_width, Screen_height, x=300, y=800):
        self.x = x 
        self.y = y  
        self.velocity = 10
        self.acc = 0.1
        self.hp = 5
        self.scale = 1/4.5
        self.color = color
        self.ship_type = ship_type
        self.img_path = "src/img/spaceships/"+ship_type+"/Spaceship_0"+ship_type+"_"+color+".png"
        self.img = (pygame.image.load(self.img_path))
        self.width = self.img.get_width()*self.scale
        self.height = self.img.get_height()*self.scale
        self.img = pygame.transform.scale(self.img, (int(self.width),int(self.height))) 
        self.hitbox = [self.x, self.y, self.width, self.height]
        self.bullets = []

    def get_bullets(self):
        return self.bullets

    def get_hb_as_rect(self):
        '''doc string'''
        return pygame.Rect(self.hitbox)
    
    def get_hp(self):
        return self.hp

    def get_scale(self):
        return self.scale

    def get_color(self):
        return self.color

    def get_type(self):
        return self.ship_type
    
    def set_pos(self, x, y):
        '''set pos of ship'''
        self.x = x
        self.y = y

    def set_type(self,s_type, scale):
        '''set the type of ship'''
        self.img_path = "src/img/spaceships/"+s_type+"/Spaceship_0"+s_type+"_"+self.color+".png"
        self.img = (pygame.image.load(self.img_path))
        self.resize(scale)
        self.ship_type = s_type

    def set_color(self, clr, scale):
        '''set the color of ship'''
        self.img_path = "src/img/spaceships/"+self.ship_type+"/Spaceship_0"+self.ship_type+"_"+clr+".png"
        self.img = (pygame.image.load(self.img_path))
        self.resize(scale)
        self.color = clr


    def resize(self, n):
        '''resize ship'''
        self.width = self.img.get_width()*n
        self.height = self.img.get_height()*n
        self.img = pygame.transform.scale(self.img, (int(self.width),int(self.height))) 

    def shoot(self, KEYS, K_space, Screen, S_height):

        """Create the bullets and append it"""
    
        if KEYS[K_space]:
            B = Bullet(self.x+self.width/2, self.y, Screen)
            self.bullets.append(B)


    def draw_hb(self, Screen):
        pygame.draw.rect(Screen, (255,0,0),  self.hitbox, 2)

    def draw(self, Screen, S_width, S_height):
        """Draw where the ship is located, and the bullets"""

        if self.hp > 0:
            Screen.blit(self.img, (self.x, self.y))
            #Just while coding - HITBOX
            #draw_hb()

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
        destroy_fx = mixer.Sound("src/sounds/destroy_fx.wav")
        w_comparation1 = enemy.hitbox[0] >= self.x and enemy.hitbox[0] <= self.x + self.height 
        h_comparation1 = enemy.hitbox[1] >= self.y and enemy.hitbox[1] <= self.y + self.height   
        comp1 = w_comparation1 and h_comparation1
        
        w_comparation2 = enemy.hitbox[0] + enemy.hitbox[2] >= self.x and enemy.hitbox[0] <= self.x + self.height 
        h_comparation2 = enemy.hitbox[1] + enemy.hitbox[3]>= self.y and enemy.hitbox[1] <= self.y + self.height   
        comp2 = w_comparation2 and h_comparation2

        if comp1 or comp2:
            enemy.relocate(S_width, S_height)
            destroy_fx.play()
            self.hp -= 1
            #print("Ship HP: ",self.hp)
        if enemy.y + enemy.height + 5 > S_height:
            self.hp -= 1
            #print("Ship HP: ",self.hp)
