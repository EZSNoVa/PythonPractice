import pygame as pg, random, sys, asyncio

# < BASE >
WIDTH, HEIGHT = 640, 480
screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
clock = pg.time.Clock()

# < PRE-LOAD, Vars & Funcions >
pg.init()
FPS = 60

# < START >
    
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
   # < LOGIC >
        
   # < DRAW >  
    screen.fill((0, 0, 0))
    
   # < END >
    pg.display.flip()
    clock.tick(FPS)
    