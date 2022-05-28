import math 
import thales as th 
import pygame 
from pygame.locals import *

# TODO: Add ICircle, IEllipse, IParabola, IHyperbola (interactive versions)    

class Circle: 
    ... 

class Ellipse: 
    ...

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

    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit() 
                exit(0) 
    
        surface.fill((255,255,255)) 

        g.draw() 

        pygame.display.update() 