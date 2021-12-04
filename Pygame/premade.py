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
    def __init__(self, surface, color, pos=[0,0], speed=[10,0,0], gravity=False, collision=False, floor=True, walls=True, bounce=True):
        self.surface = surface
        self.color = color
        self.x = pos[0]
        self.y = pos[1]
        self.speed = speed[0]
        self.x_speed = speed[1]
        self.y_speed = speed[2]
        self.gravity = gravity
        self.collision = collision
        self.floor = floor
        self.walls = walls
        self.bounce = bounce

class Square(Object):
    def __init__(self, surface, color=white, pos=[20,20], size=[20,20], speed=[10,0,0], gravity=True, collision=False, floor=True, walls=True, bounce=True):
        super().__init__(surface=surface, color=color, pos=pos, speed=speed, gravity=gravity, collision=collision, floor=floor, walls=walls, bounce=bounce)
        self.width = size[0]
        self.height = size[1]
        
    def Update(self, surface=None, postmovement=False):
        if surface == None:
            surface = self.surface
            
        if surface != self.surface:
            self.surface = surface
            
        if self.gravity == True:
            # fall if object over object height
            if self.y == surface.get_height() - self.height or self.y == surface.get_height() :
                if self.floor == False:
                    self.y = 0
                    self.y_speed = 0 if self.bounce == False else self.y_speed * -1
                else:
                    self.y = surface.get_height() - self.height
                    self.y_speed = 0 if self.bounce == False else self.y_speed * -1

                
            elif self.y > surface.get_height() - self.height:
                self.y_speed = 0 if self.bounce == False else self.y_speed * -1
                self.y = surface.get_height() - self.height
            
            elif self.y <= 0:
                self.y = 0
                self.y_speed = 0 if self.bounce == False else self.y_speed * -1
                    
        if self.floor == True:
            if self.y == surface.get_height() - self.height:
                self.y = surface.get_height() - self.height
                self.y_speed = 0 if self.bounce == False else self.y_speed * -1
                
            if self.y <= 0:
                self.y = 0
                self.y_speed = 0 if self.bounce == False else self.y_speed * -1

        if self.walls == True:
            if self.x == surface.get_width() - self.width:
                self.x = surface.get_width() - self.width
                self.x_speed = 0 if self.bounce == False else self.x_speed * -1
            if self.x <= 0:
                self.x = 0
                self.x_speed = 0 if self.bounce == False else self.x_speed * -1
        
        if postmovement == True:
            self.x += self.x_speed
            self.y += self.y_speed    
        
    def Draw(self, surface=None):
        if surface == None:
            surface = self.surface
            
        if surface != self.surface:
            self.surface = surface
                
        pg.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
       
    # comprobations
    def inborder(self, surface=None):
        if surface == None:
            surface = self.surface
            
        if surface != self.surface:
            self.surface = surface
        
        # if object is in out or touching border return True
        if self.y == surface.get_height() - self.height or self.y == surface.get_height() or self.y <= 0 or self.x == surface.get_width() - self.width or self.x == surface.get_width() or self.x <= 0:
            return True
        else:
            return False
        
    def incollision(self, obj):
        # if object is in collision return True
        if self.x <= obj.x + obj.width and self.x + self.width >= obj.x and self.y <= obj.y + obj.height and self.y + self.height >= obj.y:
            return True
        else:
            return False
                      
# < FUNCTIONS >
            
def Draw(surface, figure, pos=[10,10]):
    figure.x = pos[0]
    figure.y = pos[1]
    figure.draw(surface)
    
def Font(font, size, text, color=white):
    font = font.capitalize()
    return pg.font.SysFont(font, size).render(text, True, color)
    


# < BASEBUILT CLASSES >
class SquarePlayer(Square):
    def __init__(self, surface, color=white, pos=[10,10], speed=[0,0,0], size=[10,10], collision=False, floor=True, walls=True, bounce=False):
        super().__init__(surface=surface, color=color, pos=pos, size=size, speed=speed, gravity=True, collision=collision, floor=floor, walls=walls, bounce=bounce)
        self.started = {
            "pos" : pos,
            "speed" : speed,
            "size" : size,
            "collision" : collision,
            "floor" : floor,
            "walls" : walls,
            "bounce" : bounce
        }
        
    def Update(self, surface=None, postmovement=False):
        if surface == None:
            surface = self.surface
            
        if surface != self.surface:
            self.surface = surface
            
        if self.gravity == True:
            # fall if object over object height
            if self.y == surface.get_height() - self.height or self.y == surface.get_height() :
                if self.floor == False:
                    self.y = 0
                    self.y_speed = 0 if self.bounce == False else self.y_speed * -1
                else:
                    self.y = surface.get_height() - self.height
                    self.y_speed = 0 if self.bounce == False else self.y_speed * -1

                
            elif self.y > surface.get_height() - self.height:
                self.y_speed = 0 if self.bounce == False else self.y_speed * -1
                self.y = surface.get_height() - self.height
            
            elif self.y <= 0:
                self.y = 0
                self.y_speed = 0 if self.bounce == False else self.y_speed * -1
                    
        if self.floor == True:
            if self.y == surface.get_height() - self.height:
                self.y = surface.get_height() - self.height
                self.y_speed = 0 if self.bounce == False else self.y_speed * -1
                
            if self.y <= 0:
                self.y = 0
                self.y_speed = 0 if self.bounce == False else self.y_speed * -1

        if self.walls == True:
            if self.x == surface.get_width() - self.width:
                self.x = surface.get_width() - self.width
                self.x_speed = 0 if self.bounce == False else self.x_speed * -1
            if self.x <= 0:
                self.x = 0
                self.x_speed = 0 if self.bounce == False else self.x_speed * -1  
                
        if postmovement == True:
            self.x += self.x_speed
            self.y += self.y_speed

    def Draw(self, surface = None):
        if surface == None:
            surface = self.surface
        
        if surface != self.surface:
            self.surface = surface
            
        if self.walls == True:
            if self.x == surface.get_width() - self.width:
                self.x = surface.get_width() - self.width
                self.x_speed = 0 if self.bounce == False else self.x_speed * -1
            if self.x <= 0:
                self.x = 0
                self.x_speed = 0 if self.bounce == False else self.x_speed * -1
                
        if self.floor == True:
            if self.y >= surface.get_height() - self.height:
                self.y = surface.get_height() - self.height
                self.y_speed = 0 if self.bounce == False else self.y_speed * -1
            if self.y <= 0:
                self.y = 0
                self.y_speed = 0 if self.bounce == False else self.y_speed * -1
                
        self.x += self.x_speed
        self.y += self.y_speed    
        # draw head of snake 
        pg.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
                  
    def Reset(self):        
        self.x = self.started["pos"][0]
        self.y = self.started["pos"][1]
        self.x_speed = self.started["speed"][1]
        self.y_speed = self.started["speed"][2]
        self.speed = self.started["speed"][0]
        self.width = self.started["size"][0]
        self.height = self.started["size"][1]
        self.collision = self.started["collision"]
        self.floor = self.started["floor"]
        self.walls = self.started["walls"]
        self.bounce = self.started["bounce"]
        
    # hability
    def Slow(self):
        self.speed = 1
        self.x_speed = self.speed
        self.y_speed = self.speed
