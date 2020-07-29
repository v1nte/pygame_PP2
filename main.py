import pygame
from classes.ship import Ship 

pygame.init()

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

clock = pygame.time.Clock()

def update_and_draw():
    '''update and draw, duh'''
    SCREEN.blit(Background, (0,0))
    m_ship.draw(SCREEN)
    pygame.display.update()

main_loop = True
while main_loop:

    m_ship = Ship("RED", "01", SCREEN_WIDTH, SCREEN_HEIGHT )
#    imagen_fondo = pygame.image.load('img/bg.jpg')
    
    is_playing = True 
    while is_playing:
        for event  in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        clock.tick(60)

        KEYS = pygame.key.get_pressed()
        m_ship.update(KEYS, K_LEFT, K_RIGHT, K_UP, K_DOWN, SCREEN_WIDTH, SCREEN_HEIGHT)

        update_and_draw()

pygame.quit()

 
