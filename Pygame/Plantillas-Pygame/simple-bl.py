import pygame as pg, random, sys, asyncio

# < BASE >
WIDTH, HEIGHT = 640, 480
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
clock = pg.time.Clock()

# < PRE-LOAD, Vars & Funcions >
pg.init()
FPS = 60
BACK_LOAD = True
BACK_LOAD_VALUE = 5

# < START >
if BACK_LOAD:
    seconds_passed = 0
    
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
   # < LOGIC >
    
   # < BACKLOAD-LOGIC > 
    if BACK_LOAD:
        if int(seconds_passed) == BACK_LOAD_VALUE:
            # code for backload here                      
            seconds_passed = 0
    
   # < DRAW >  
    screen.fill((0, 0, 0))
    
   # < END >
    pg.display.flip()
    clock.tick(FPS)
    if BACK_LOAD:
        seconds_passed += FPS / 1000 * 0.2345
        seconds_passed = round(seconds_passed, 2)
    