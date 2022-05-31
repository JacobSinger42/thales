import thales as th 
import pygame 
from pygame.locals import * 

def newComplex (z, g): 
    return Complex(z.real, z.imag, g)

def oldComplex (z): 
    return complex(*z.c())

class Complex(complex): 
    def __new__(self, r, i, g): 
        return complex.__new__(self, r, i) 

    def __init__(self, r, i, g): 
        complex.__init__(r, i)
        self.g = g 

    def r(self): 
        return self.real 

    def i(self): 
        return self.imag 

    def c(self): 
        return (self.r(), self.i()) 

    # built-in operator definitions (add pow) 
    def conjugate(self): 
        return newComplex(super().conjugate(), self.g) 

    def __add__(self, _x): 
        return Complex(self.r() + _x.real, self.i() + _x.imag, self.g)

    def __sub__(self, _x): 
        return Complex(self.r() - _x.real, self.i() - _x.imag, self.g) 

    def __mul__(self, _x): 
        return Complex(self.r() * _x.real, self.i() * _x.imag, self.g) 

    def __truediv__(self, _x): 
        return Complex(self.r() / _x.real, self.i() / _x.imag, self.g) 

    def __radd__(self, _x): 
        return self + _x 

    def __rsub__(self, _x): 
        return Complex(_x.real - self.r(), _x.imag - self.i(), self.g) 

    def __rmul__(self, _x): 
        return self * _x 

    def __rtruediv__(self, _x): 
        return Complex(_x.real / self.r(), _x.imag / self.i(), self.g) 

    def draw(self, r=10, fColor=(255,255,255), oColor=(255,0,0), oWidth=4): 
        th.Point(self.g.surface, self.g, self.c(), r, fColor, oColor, oWidth).draw() 

if __name__ == '__main__': 
    SW, SH = 800, 600 
    surface = pygame.display.set_mode((SW,SH)) 
    pygame.display.set_caption('Complex Example') 

    g = th.Grid(surface, (SW/2,SH/2), (40,40), (SW, SH), cColor=(0,0,255))

    z1 = Complex(-3, 1, g) 
    z2 = Complex(2, 1, g) 

    print(type(z1.conjugate()))

    while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                pygame.quit() 
                exit(0) 

        surface.fill((255,255,255))

        g.draw() 
        z1.draw() 
        z2.draw() 
        z1.conjugate().draw() 
        z2.conjugate().draw() 
        (z1+z2).draw() 
        (z1.conjugate() + z2.conjugate()).draw() 

        pygame.display.update() 