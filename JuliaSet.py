import numpy as np
import cv2
import sys
from math import sqrt
sys.setrecursionlimit(10000)

class JuliaSet:
    def __init__(self, size, numColors, c):
        self.size = size
        self.c = c
        self.img = np.zeros((size,size,3), dtype='uint8')
        self.pallet = []
        self.generatePallet(numColors)
        self.MAX_STACK = len(self.pallet)-1
        self.generateImage()
        
    def generatePallet(self, numColors):
        step = int(255 / (numColors**0.33333333 - 1)) # cada canal deve ter n cores, onde numColors = n*n*n
        for b in range(0, 256, step):
            for g in range(0, 256, step):
                for r in range(0, 256, step):
                    self.pallet.append([g,b,r])
        self.pallet = np.array(self.pallet, dtype='uint8')        

    def f(self, z):
        return z**2 + self.c
    
    def mag(self, x):
        return sqrt((x.real**2) + (x.imag**2))
    
    def num(self, z, iterations):
        if iterations < self.MAX_STACK:
            if self.mag(self.f(z)) > 2: 
                return 1
            else:
                return self.num(self.f(z), iterations+1) + 1
        return 0
        
    def generateImage(self):
        r = np.linspace(-2, 2, self.size)       # eixo dos #'s reais
        im = np.linspace(2j, -2j, self.size)    # eixo dos #'s imaginarios
        for i in range(0, self.size):
            for j in range(0, self.size):
                z = r[j] + im[i]
                self.img[i,j] = self.pallet[self.num(z, 0)]

    def getImage(self):
        return self.img
 



# alguns valores de c para padroes diferentes
#c = -0.7269 + 0.1889j
c = -0.624 + 0.435j
#c = 0 + 0.8j
#c = -0.7 + 0.3j
#c = -0.70176 -0.3842j
#c = -1.2 + 0.75j

mbs = JuliaSet(600, 500, c)  # imagem de 600x600 e max 500 cores  
cv2.imwrite('julia.png', mbs.getImage())
