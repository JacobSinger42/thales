import math
import thales as th 
import pygame 
from pygame.locals import *

# TODO: Add ICircle, IEllipse, IParabola, IHyperbola (interactive versions)    
# TODO: Make Polymorphic and simpler by adding a parent Conic class (create find dx/dy method, then another method to automate point drawing) 

class Circle: 
    def __init__(self, surface, g, c, r, color=(255,0,0), showCenter=False): 
        self.surface, self.g, self.c, self.r, self.color, self.showCenter = surface, g, c, r, color, showCenter

    def draw(self): 
        for x in range (self.g.px(self.c[0] - self.r), self.g.px(self.c[0] + self.r)): 
            dy = math.sqrt(self.r**2 - (self.g.gx(x) - self.c[0])**2) 
            th.Point(self.surface, self.g, (g.gx(x), self.c[1] + dy), radius=5, fColor=self.color).draw() 
            th.Point(self.surface, self.g, (g.gx(x), self.c[1] - dy), radius=5, fColor=self.color).draw() 
        for y in range (self.g.py(self.c[1] + self.r), self.g.py(self.c[1] - self.r)): 
            dx = math.sqrt(self.r**2 - (self.g.gy(y) - self.c[1])**2)
            th.Point(self.surface, self.g, (self.c[0] + dx, self.g.gy(y)), radius=5, fColor=self.color).draw() 
            th.Point(self.surface, self.g, (self.c[0] - dx, self.g.gy(y)), radius=5, fColor=self.color).draw() 
        if self.showCenter: 
            th.Point(self.surface, self.g, self.c, fColor=(255,255,255), oColor=self.color).draw() 

class Ellipse: 
    def __init__(self, surface, g, c, xR, yR, color=(255,0,0), showCenter=False): 
        self.surface, self.g, self.c, self.xR, self.yR, self.color, self.showCenter = surface, g, c, xR, yR, color, showCenter
    
    def draw(self): 
        for x in range (self.g.px(self.c[0] - self.xR), self.g.px(self.c[0] + self.xR)): 
            dy = self.yR * math.sqrt(1 - ((self.g.gx(x) - self.c[0])/self.xR)**2) 
            th.Point(self.surface, self.g, (self.g.gx(x), self.c[1] + dy), radius=5, fColor=self.color).draw() 
            th.Point(self.surface, self.g, (self.g.gx(x), self.c[1] - dy), radius=5, fColor=self.color).draw() 
        for y in range (self.g.py(self.c[1] + self.yR), self.g.py(self.c[1] - self.yR)): 
            dx = self.xR * math.sqrt(1 - ((self.g.gy(y) - self.c[1])/self.yR)**2) 
            th.Point(self.surface, self.g, (self.c[0] + dx, self.g.gy(y)), radius=5, fColor=self.color).draw() 
            th.Point(self.surface, self.g, (self.c[0] - dx, self.g.gy(y)), radius=5, fColor=self.color).draw() 
        if self.showCenter: 
            th.Point(self.surface, self.g, self.c, fColor=(255,255,255), oColor=self.color).draw() 

class Parabola: 
    ...

class Hyperbola: 
    ...
    
if __name__ == '__main__': 
    pygame.init() 
    
    SW, SH = 800, 600 
    surface = pygame.display.set_mode((SW,SH)) 
    pygame.display.set_caption('Conic Sections Example') 

    g = th.Grid(surface, (SW/2, SH/2), (40,40), (SW,SH), cColor=(100,100,100))

    c = Circle(surface, g, (0,0), 5)
    e = Ellipse(surface, g, (0, 0), 2, 5) 

    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit() 
                exit(0) 
    
        surface.fill((255,255,255)) 

        g.draw() 
        c.draw() 
        e.draw() 

        pygame.display.update() 