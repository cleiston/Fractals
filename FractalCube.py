import cv2
import numpy as np
import random

class FractalCube:
    def __init__(self, size):
        self.cube = np.ones((size, size, 3), dtype="uint8") * 255
        self.draw(0, 0, size)
        
    def draw(self, x, y, size):
        if(size > 8):
            l = size/3
            self.cube[x+l:x+l+l, y+l:y+l+l] = 0
            for i in range(x, x+size, l):
                for j in range(y, y+size, l):
                    self.draw(i, j, l)

    def getImage(self):
        return self.cube
        
        
cube = FractalCube(2000)
cv2.imwrite('fractalCube.png', cube.getImage())
