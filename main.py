import pygame
from classes.ship import Ship 
from classes.enemy import Enemy

pygame.init()

FPS = 60

#Screen Settings
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 900 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working on it...")
Background = pygame.image.load('src/img/bg.png')
Background = pygame.transform.scale(Background, (SCREEN_WIDTH,SCREEN_HEIGHT))

#Keys Shortcuts
K_LEFT = pygame.K_LEFT
K_RIGHT = pygame.K_RIGHT
K_UP = pygame.K_UP
K_DOWN = pygame.K_DOWN
K_SPACE = pygame.K_SPACE

clock = pygame.time.Clock()

def KEYS():
    '''Return key.get_pressed()'''
    return pygame.key.get_pressed()    

def event_quit():
    """Close the game if you pressed "X" in the corner """
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

def main_update():
    """Update all the things, lmao"""
    m_ship.update(KEYS(), K_LEFT, K_RIGHT, K_UP, K_DOWN, SCREEN_WIDTH, SCREEN_HEIGHT)
    m_ship.shoot(KEYS(), K_SPACE, SCREEN, SCREEN_HEIGHT)
    rect.update(SCREEN_WIDTH, SCREEN_WIDTH)
    rect.get_hit(m_ship.get_bullets())

def main_draw():
    """Draw all the things, lmao"""

    SCREEN.blit(Background, (0,0))
    m_ship.draw(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)
    rect.draw(SCREEN)
    pygame.display.update()

"""

MAIN LOOP - GAME LOOP

"""
main_loop = True
while main_loop:
    m_ship = Ship("PURPLE", "4", SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT )
    rect = Enemy(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT) 


    """
    Loop while is Playing
    """
    is_playing = True 
    while is_playing:
        event_quit()
        clock.tick(FPS)

        main_update()
        main_draw()

pygame.quit()
 
