import pygame
from pygame.locals import *
from Vector2 import vector
class Snake:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.vit = 20
        self.dir ="none"
        self.body = []
        self.bodyRect = []

    def Draw(self, ecran, color, snake_block, score):
        # On gère la longueur du corps du serpent
        self.body.insert(0, vector(-100, -100))
        while len(self.body) > score:
            del self.body[0]
        
        # Caractérisque du serpent    
        pygame.draw.rect(ecran, color, (self.x, self.y, snake_block, snake_block))
        for pos in self.body:
            pygame.draw.rect(ecran, color, (pos.x, pos.y, snake_block, snake_block))
    
    def Update(self):
        # On gère la longueur du corps du serpent
        self.bodyRect = []
        if len(self.body) >0:
            tab = []
            for i in range(len(self.body)):
                if i != 0: 
                    tab.append(vector(self.body[i-1].x, self.body[i-1].y))
                    self.bodyRect.append(Rect(self.body[i-1].x, self.body[i-1].y, 20, 20))
            self.body = tab
            self.body.insert(0, vector(self.x, self.y)) 
            
        # On gère les mouvements du serpent
        if self.dir == "up":
            self.y-=self.vit
        elif self.dir == "down":
            self.y+=self.vit
        elif self.dir == "left":
            self.x-=self.vit
        elif self.dir == "right":
            self.x+=self.vit