import cv2
import numpy as np
from math import pow

class PascalTriangle:
    def __init__(self, power):
        self.w = int(pow(2, power) + 1)         # largura
        self.h = int(self.w/2)                  # altura
        self.img = np.zeros((self.h, self.w), dtype='uint8') # fundo preto da imagem
        self.generateTriangle()
        
    def generateTriangle(self):
        self.img[0, int(self.w/2)] = 1          # primeiro valor do triangulo de pascal
        for i in range(1, self.h):
            for j in range(1, self.w-1):
                self.img[i,j] = self.img[i-1, j-1] + self.img[i-1, j+1]     # os outros valores sao preenchidos
        self.img = (self.img % 2) * 255         # transforma os valores do triangulo em 0's e 1's e multiplica por 255(branco)
        
    def getImage(self):
        return self.img





pascal = PascalTriangle(12)                     # instancia um objeto de largura = 2^12 e altura = largura/2
cv2.imwrite('pascal.png', pascal.getImage())
