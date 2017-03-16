import cv2
import numpy as np
from math import sin, cos, pi

# Fractal Tree
# Autor: Cleiston Rodrigues
# Testado no Opencv 3.1.0-dev e Python 2.7.12

class FractalTree:
    def __init__(self, rootLength):                     # tamanho do primeiro galho definido por rootLength
        n = rootLength*12                               # imagem(largura e altura) eh 12 vezes maior que o primeiro tronco
        self.img = np.zeros((n,n, 3), dtype="uint8")    # fundo preto
        self.color = np.array([100, 255, 100])          # cor da arvore
        start = tuple([int(n/2), int(n)])               # inicio da arvore
        self.step = pi/10                               # inclinacao do ramo com relacao ao tronco anterior
        self.draw(start, rootLength, -pi/2, 15)
        
        
        
    def draw(self, start, branchSize, angle, thickness):
        if(branchSize > 10):
            troncoX = int(start[0] + branchSize*cos(angle))
            troncoY = int(start[1] + branchSize*sin(angle))
            tronco = (troncoX, troncoY)                 # endpoint
            cv2.line(self.img, start, tronco, self.color, thickness, cv2.LINE_AA)   #desenha o tronco
            
            # agora os ramos
            if thickness > 1:
                thickness -= 2
            
            branchSize = int(branchSize*0.8)            # reduz o tamanho dos novos troncos/ramos
            
            angleL = angle-self.step
            branchLx = int(tronco[0] + branchSize*cos(angleL))
            branchLy = int(tronco[1] + branchSize*sin(angleL))
            branchL = (branchLx, branchLy)
            cv2.line(self.img, tronco, branchL, self.color, thickness, cv2.LINE_AA) #desenha o ramo esquerdo
            
            angleR = angle+self.step
            branchRx = int(tronco[0] + branchSize*cos(angleR))
            branchRy = int(tronco[1] + branchSize*sin(angleR))
            branchR = (branchRx, branchRy)          
            cv2.line(self.img, tronco, branchR, self.color, thickness, cv2.LINE_AA) #desenha o ramo direito
            
            
            self.draw(branchL, branchSize, angleL, thickness)
            self.draw(branchR, branchSize, angleR, thickness)
            
    def getImage(self):
        return self.img




      
im = FractalTree(250) # instancia um objeto com tronco inicial de 250px

cv2.imwrite('teste.png', im.getImage())

