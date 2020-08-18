import pygame
import json
from pygame.locals import *
from classes.ship import Ship 
from classes.enemy import Enemy
from  pygame import mixer

pygame.init()

FPS = 60
text = pygame.font.SysFont('console', 30, True)


#Screen Settings
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 900 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Py Ship Ulegos")
Background = pygame.image.load('src/img/bg.png')
Background = pygame.transform.scale(Background, (SCREEN_WIDTH,SCREEN_HEIGHT))

#Keys Shortcuts
K_LEFT = pygame.K_LEFT
K_RIGHT = pygame.K_RIGHT
K_UP = pygame.K_UP
K_DOWN = pygame.K_DOWN
K_SPACE = pygame.K_SPACE

click = False

clock = pygame.time.Clock()

def KEYS():
    '''Return key.get_pressed()'''
    return pygame.key.get_pressed()    

def event_quit():
    """Close the game if you pressed "X" in the corner """
    for event  in pygame.event.get():
        if event.type == QUIT:
            quit()
    pygame.display.update()

def main_update():
    """Update logical things"""
    global SCORE
    global diff, seeing_score, is_playing
    m_ship.update(KEYS(), K_LEFT, K_RIGHT, K_UP, K_DOWN, SCREEN_WIDTH, SCREEN_HEIGHT)
    m_ship.shoot(KEYS(), K_SPACE, SCREEN, SCREEN_HEIGHT)
    m_ship.get_hit(rect,SCREEN_WIDTH,SCREEN_HEIGHT)
    rect.update(SCREEN_WIDTH, SCREEN_HEIGHT)
    rect.get_hit(m_ship.get_bullets())
    SCORE += rect.get_score()
    win_msg = text.render("GANASTE!!!", 1, (255,153,153)) 
    lost_msg = text.render("Perdiste! tonto", 1, (255, 153, 153)) 

    if m_ship.hp < 1:
        final_msg = lost_msg

    if rect.lost_count > 2:
        diff = "UdC"
        rect.set_vel(6)
    
    if rect.lost_count > 6:
        diff = "PUEC"
        rect.set_vel(8)

    if rect.lost_count > 9:
        final_msg = win_msg 

    if m_ship.hp < 1 or rect.lost_count > 9:
        SCREEN.blit(final_msg, (SCREEN_WIDTH//2-final_msg.get_width()//2, SCREEN_HEIGHT//2-final_msg.get_height()//2))
        seeing_score = True
        is_playing = False
        pygame.display.update()
        pygame.time.delay(2000)

def main_draw():
    """Draw all the things """
    global SCORE
    global diff
    global final_msg, win_msg, lost_msg
    diff_txt = text.render("Dificultad: "+diff, 1, (255,153,153))
    HP = text.render("Vidas:"+str(m_ship.hp),1, (255, 153, 153))
    HP_enemy = text.render("Vidas enemigo:"+str(rect.hp),1, (255, 153, 153))
    Score = text.render("Score:"+str(SCORE), 30, (255,153,153))
    SCREEN.blit(Background, (0,0))
    SCREEN.blit(Score, (SCREEN_WIDTH-Score.get_width(),0))
    SCREEN.blit(HP, (0,0))
    SCREEN.blit(HP_enemy, (0,30))
    SCREEN.blit(diff_txt, (0,60))
    m_ship.draw(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)
    rect.draw(SCREEN)
    pygame.display.update()

def reset_scores():
    '''reset the json file'''
    with open('scores.json', 'r') as f:
        data = json.load(f)
    with open('scores.json', 'w') as f:
        for i in range(len(data)):
            data.popitem()

        data.update({"Score1" : 0})
        json.dump(data, f)



def score_screen():
    '''Display the Score you have'''
    click3 = False
    seeing_score = True
    while seeing_score:
        mx, my = pygame.mouse.get_pos()
        SCREEN.blit(Background, (0,0))

        back_btn = pygame.Rect(150, 800, 150,50)
        back_txt = text.render("Volver", 1, (255,25,255))
        reset_btn = pygame.Rect(350, 800, 150, 50)
        reset_txt = text.render("Reset", 1, (255,25,255))
        pygame.draw.rect(SCREEN, (200, 200, 200), back_btn)
        pygame.draw.rect(SCREEN, (200,200,200), reset_btn)
        SCREEN.blit(back_txt, (180,810))
        SCREEN.blit(reset_txt, (380,810))
        
        with open('scores.json', 'r') as f:
            data = json.load(f)
            if data["Score1"] != 0: 
                for i in range(len(data)): 
                    score_txt = text.render("Score " +str(i+1)+ ": "+ str(data['Score'+str(i+1)]), 1 , (255,25,255)) 
                    SCREEN.blit(score_txt, (150, 300+i*35))
            else:
                SCREEN.blit(text.render("No tienes puntaje aun", 1, (255,25,255)), (150, 300))


        if back_btn.collidepoint((mx,my)) and click3:
            seeing_score = False

        if reset_btn.collidepoint((mx,my)) and click3:
            reset_scores()

        click3 = False
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click3 = True
        pygame.display.update()

def select_ship():
    """Select type and color of the Ship"""
    global SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT
    global m_ship

    back_text = text.render("Volver", 1, (255,25,255))
    test_ships = []
    preview_ship = m_ship

    back_button = pygame.Rect(250, 800, 200,50)
    rect_blue = pygame.Rect(80, 500, 50,50)
    rect_green = pygame.Rect(80*2, 500, 50,50)
    rect_n_blue = pygame.Rect(80*3, 500, 50,50)
    rect_orange = pygame.Rect(80*4, 500, 50,50)
    rect_purple = pygame.Rect(80*5, 500, 50,50)
    rect_red = pygame.Rect(80*6, 500, 50,50)
    rect_yellow = pygame.Rect(80*7, 500, 50,50)

    preview_ship.set_pos(250,300)
    preview_ship.resize(2)
    for i in range(1,7):
       test_ships.append(Ship("RED", str(i), SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT,  90*i, 600))
    
    click2 = False
    selecting = True
    while selecting:
        mx, my = pygame.mouse.get_pos()
        SCREEN.blit(Background, (0,0))
        preview_ship.draw(SCREEN, SCREEN_HEIGHT, SCREEN_HEIGHT)
        pygame.draw.rect(SCREEN, (200, 200, 200), back_button)
        SCREEN.blit(back_text, (280,810))

        i = 0
        for ships in test_ships:
            ships.draw(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)
            if ships.get_hb_as_rect().collidepoint((mx,my)) and click2:
                m_ship.set_type(str(i+1), m_ship.get_scale())
                preview_ship.set_type(str(i+1), preview_ship.get_scale()*2)
                print(preview_ship.get_color())
            i += 1


        pygame.draw.rect(SCREEN, (0, 0, 255), rect_blue)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect_green)
        pygame.draw.rect(SCREEN, (35, 35, 142), rect_n_blue)
        pygame.draw.rect(SCREEN, (255, 165, 0), rect_orange)
        pygame.draw.rect(SCREEN, (255, 0, 255), rect_purple)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect_red)
        pygame.draw.rect(SCREEN, (255, 255, 0), rect_yellow)
        

        #TEDIOUS PART!!!!!!!!!!!!!!!!!!!!!!!!
        if back_button.collidepoint((mx,my)) and click2:
            m_ship.set_color(preview_ship.get_color(), m_ship.get_scale())
            m_ship.set_type(preview_ship.get_type(), m_ship.get_scale())
            selecting = False
            click2 = False

        if rect_blue.collidepoint((mx,my)) and click2:
            preview_ship.set_color("BLUE", preview_ship.get_scale()*2) 

        if rect_green.collidepoint((mx,my)) and click2:
            preview_ship.set_color("GREEN", preview_ship.get_scale()*2) 
        
        if rect_n_blue.collidepoint((mx,my)) and click2:
            preview_ship.set_color("NAVY BLUE", preview_ship.get_scale()*2) 

        if rect_orange.collidepoint((mx,my)) and click2:
            preview_ship.set_color("ORANGE", preview_ship.get_scale()*2) 

        if rect_purple.collidepoint((mx,my)) and click2:
            preview_ship.set_color("PURPLE", preview_ship.get_scale()*2) 

        if rect_red.collidepoint((mx,my))  and click2:
            preview_ship.set_color("RED", preview_ship.get_scale()*2) 
        
        if rect_yellow.collidepoint((mx,my)) and click2:
            preview_ship.set_color("YELLOW", preview_ship.get_scale()*2) 

        click2 = False
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click2 = True

        pygame.display.update()


def main_menu():
    global click, menu_loop, seeing_score
    SCREEN.blit(Background, (0,0))
    mx, my = pygame.mouse.get_pos()

    play_button = pygame.Rect(50, 100, 200, 50)
    select_ship_button = pygame.Rect(50, 200, 200, 50)
    scores_button = pygame.Rect(50, 300, 200, 50)
    
    if play_button.collidepoint((mx,my)) and click:
        menu_loop = False
        click = False
    if select_ship_button.collidepoint((mx,my)) and click:
        select_ship()
        click = False
    if (scores_button.collidepoint((mx,my)) and click) or seeing_score :
        seeing_score = False
        score_screen()
        click = False

    pygame.draw.rect(SCREEN, (200, 200, 200), play_button)
    pygame.draw.rect(SCREEN, (200, 200, 200), select_ship_button)
    pygame.draw.rect(SCREEN, (200, 200, 200), scores_button)

    select_ship_text = text.render("Elegir nave", 1, (255, 25,255))
    play_text = text.render("JUGAR!",1,(255,25,255))
    scores_text = text.render("Puntajes",1,(255,25,255))
    SCREEN.blit(play_text, (50,100))
    SCREEN.blit(select_ship_text, (50,200))
    SCREEN.blit(scores_text, (50,300))

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True


"""
MAIN LOOP - GAME LOOP

"""
diff = ""
main_loop = True
seeing_score = False
while main_loop:
    m_ship = Ship("NAVY BLUE", "1", SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT )
    rect = Enemy(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT) 
    global SCORE 
    SCORE = 0

    #json_file = pen("scores.json", "r+", encoding="utf-8")
    #j_score = json.load(json_file)
    #BACKGROUND Sound
    mixer.music.load('src/sounds/Mercury.mp3')
    mixer.music.play(-1)

    """
    MENUS LOOP
    """
    menu_loop = True
    while menu_loop:
        main_menu()
        clock.tick(FPS)
        event_quit()


    """
    Loop while is Playing
    """
    m_ship.set_pos(300,800)
    diff = "ULegos"
    is_playing = True 
    while is_playing:
        event_quit()
        clock.tick(FPS)

        main_update()
        main_draw()
        if m_ship.hp < 1 or rect.lost_count > 9 :
            with open('scores.json', 'r') as f:
                data = json.load(f)
            with open('scores.json', 'w') as f:

                if data["Score1"] == 0:
                    data.update({"Score1" : SCORE})
                    print(data)
                else:
                    string = "Score"+str(len(data)+1)
                    data.update({string: SCORE})
                json.dump(data, f)
                print(f)
            is_playing = False

pygame.quit()
