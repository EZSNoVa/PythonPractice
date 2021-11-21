import pygame as pg, sys, random
from premade import *
pg.init()

screen = pg.display.set_mode((640, 480), pg.RESIZABLE)
clock = pg.time.Clock()
FPS = 144


# < pre logic >
# fps counter
fps_list = []
average = FPS

# coords and stuff
bot = True
bot_difficulty = 0 # 0 = easy, 1 = medium, 2 = hard, 3 = very hard, 4 = impossible
started = False
speed = 5
points = [0,0]

bar_width = 20
bar_height = 100
# bar 1
bar1_y = 200
bar1_y_speed = 0
bar1_x = 0

#bar 2
bar2_y = 200
bar2_y_speed = 0
bar2_x = 620
bar2_speed = speed
# ball
ball_x = 320
ball_y = 240
ball_x_speed = 0
ball_y_speed = 0
ball_radius = 10
ball_speed = 2

def reset():
    global bar1_y, bar2_y, ball_x, ball_y, ball_x_speed, ball_y_speed, ball_speed, started
    bar1_y = 200
    bar2_y = 200
    ball_x = 320
    ball_y = 240
    ball_x_speed = 0
    ball_y_speed = 0
    ball_speed = 2  
    started = False

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    
        # <<  KEY EVENTS >>
        # < key down >
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sys.exit()
                
            # movement
            # wasd for bar 1, arrow keys for bar 2
            if event.key == pg.K_w:
                bar1_y_speed = -speed
            if event.key == pg.K_s:
                bar1_y_speed = speed
            if bot == False:
                if event.key == pg.K_UP:
                    bar2_y_speed = -speed
                if event.key == pg.K_DOWN:
                    bar2_y_speed = speed
                
            # activate ball
            if event.key == pg.K_SPACE:
                if started == False:
                    ball_x_speed = random.choice([-ball_speed, ball_speed])
                    ball_y_speed = random.choice([-ball_speed, ball_speed])
                    started = True
        
        # < key up >
        if event.type == pg.KEYUP:
            if event.key == pg.K_w or event.key == pg.K_s:
                bar1_y_speed = 0
            if event.key == pg.K_UP or event.key == pg.K_DOWN:
                bar2_y_speed = 0
    
    
    # < base >
    screen.fill(black)
    screen_width, screen_height = screen.get_size()
    bar2_x = screen_width - bar_width
    
    # < Bot Logic >
    if bot == True:
        if bot_difficulty == 0:
            bar2_speed = random.randint(1, 2)
            ball_speed = random.randint(2, 3)
        if bot_difficulty == 1:
            bar2_speed = random.randint(2, 4)
            ball_speed = random.randint(3, 4)
        if bot_difficulty == 2:
            bar2_speed = random.randint(4, 5)
            ball_speed = random.randint(4, 5)
        if bot_difficulty == 3:
            bar2_speed = random.randint(6, 7)
            ball_speed = random.randint(5,6)
        if bot_difficulty == 4:
            bar2_speed = random.randint(8, 9)
            ball_speed = random.randint(6, 7)

        # bot movement
        if bar2_y == ball_y:
            bar2_y_speed = 0
        if bar2_y < ball_y:
            bar2_y_speed = bar2_speed
        if bar2_y > ball_y:
            bar2_y_speed = -bar2_speed
        
        
    
    # < Logic >
    
    #movement
    bar1_y += bar1_y_speed
    bar2_y += bar2_y_speed
    
    # ball
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    # < Collision >
    # bar 1
    if ball_x <= bar1_x + 20 and ball_x >= bar1_x and ball_y <= bar1_y + bar_height and ball_y >= bar1_y:
        ball_x_speed *= -1
    # bar 2
    if ball_x >= bar2_x and ball_x <= bar2_x + bar_width and ball_y <= bar2_y + bar_height and ball_y >= bar2_y:
        ball_x_speed *= -1
        
    # < Boundaries >
    # ball
    if ball_x <= 0:
        reset()
        # add point to bar 2
        points[1] += 1
        
    if ball_x >= screen_width - ball_radius:
        reset()
        # add point to bar 1
        points[0] += 1
        
    if ball_y <= 0:
        ball_y_speed *= -1
    if ball_y >= screen_height - ball_radius:
        ball_y_speed *= -1
    
    
    if bar1_y <= 0:
        bar1_y = 0
    if bar1_y >= screen_height - bar_height:
        bar1_y = screen_height - bar_height
    if bar2_y <= 0:
        bar2_y = 0
    if bar2_y >= screen_height - bar_height:
        bar2_y = screen_height - bar_height
    
    # < Drawing >
    # bars
    pg.draw.rect(screen, white, (bar1_x, bar1_y, bar_width, bar_height))
    pg.draw.rect(screen, white, (bar2_x, bar2_y, bar_width, bar_height))
    
    # ball
    pg.draw.circle(screen, white, (ball_x, ball_y), ball_radius)
    
    # show score
    score_font = pg.font.SysFont("Arial", 30)
    score_text = score_font.render(f"{points[0]} : {points[1]}", True, white)
    screen.blit(score_text, (screen_width/2 - score_text.get_width()/2, 10))
    
    # win condition
    if points[0] == 10:
        win_font = pg.font.SysFont("Arial", 50)
        win_text = win_font.render("Player 1 Wins!", True, white)
        screen.blit(win_text, (screen_width/2 - win_text.get_width()/2, screen_height/2 - win_text.get_height()/2))
        reset()
    if points[1] == 10:
        win_font = pg.font.SysFont("Arial", 50)
        win_text = win_font.render("Player 2 Wins!", True, white)
        screen.blit(win_text, (screen_width/2 - win_text.get_width()/2, screen_height/2 - win_text.get_height()/2))
        reset()
    
    # text to show stats in botton left corner
    mode = "PvP" if bot == False else f"PvB, Dificultad : {bot_difficulty}"
    stats_text = Font("Arial", 10, f"Modo : {mode}")
    screen.blit(stats_text, (10, screen_height - stats_text.get_height() - 10))
    
    # < end >
    pg.display.flip()
    clock.tick(FPS)