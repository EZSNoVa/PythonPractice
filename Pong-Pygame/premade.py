import pygame as pg

# difine basic colors for pygame    
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)   
green = (0, 255, 0)
blue = (0, 0, 255)  
yellow = (255, 255, 0)  
orange = (255, 128, 0)
purple = (128, 0, 128)
pink = (255, 0, 255)    
light_blue = (0, 255, 255)  
light_green = (0, 255, 0)
light_red = (255, 0, 0)
light_yellow = (255, 255, 0)
light_orange = (255, 128, 0)
light_purple = (128, 0, 128)    
dark_blue = (0, 0, 128) 
dark_green = (0, 128, 0)    
dark_red = (128, 0, 0)
dark_yellow = (128, 128, 0)
dark_orange = (128, 64, 0)
dark_purple = (128, 0, 128)


# class for objects
# figures should be childrem of Object class
class Object:
    def __init__(self, surface, color, pos, speed=0, gravity=False, collision=False, floor=False):
        self.surface = surface
        self.color = color
        self.pos = pos
        self.speed = speed
        self.gravity = gravity
        self.collision = collision
        self.floor = floor

class Square(Object):
    def __init__(self, surface, color=white, pos=[20,20], size=[20,20], speed=0, gravity=True, collision=False, floor=True):
        super().__init__(surface, color, pos, speed, gravity, collision, floor)
        self.width = size[0]
        self.height = size[1]
        self.x = pos[0]
        self.y = pos[1]
        self.m = 0.1
        
    def draw(self, surface):
        if surface == None:
            surface = self.surface
        
        if self.gravity == True:
            # fall if object over object height
            if self.y == surface.get_height() - self.height or self.y == surface.get_height() :
                if self.floor == False:
                    self.y = 0
                else:
                    self.speed = 0
                
            elif self.y > surface.get_height() - self.height:
                self.speed = -1 + self.m
            
            elif self.y <= 0:
                self.speed = 1 + self.m
                    
        self.y += self.speed
        pg.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
             
class Circle(Object):
    def __init__(self, surface, color=white, pos=[20,20], radius=10, speed=0, gravity=True, collision=False, floor=True):
        super().__init__(surface, color, pos, speed, gravity, collision, floor)
        self.radius = radius
        self.x = pos[0]
        self.y = pos[1]
        self.m = speed
        self.height = self.radius * 2
        self.width = self.radius * 2
        
    def draw(self, surface):
        if surface == None:
            surface = self.surface
            
        if self.gravity == True:
            if self.y == surface.get_height() - self.height or self.y == surface.get_height() or self.y == surface.get_height() - self.radius:
                if self.floor == False:
                    self.y = 0
                else:
                    self.speed = 0
                
            elif self.y > surface.get_height() - self.height:
                self.speed = -1 + self.m
            
            elif self.y <= 0:
                self.speed = 1 + self.m
        
        else:
            self.speed = 0
        
        self.y += self.speed
        pg.draw.circle(surface, self.color, (self.x, self.y), self.radius)
            
def Draw(surface, figure, pos=[10,10]):
    figure.x = pos[0]
    figure.y = pos[1]
    figure.draw(surface)
    
def Font(font, size, text, color=white):
    return pg.font.SysFont(font, size).render(text, True, color)
        