#%%
import pygame
from setting import *
from bird import *
#%%
class Controller:
    def __init__(self):
        self.bird=pygame.sprite.GroupSingle(Bird())
    
    def update(self):
        self.bird.update()
    
    def draw(self,display):
        self.bird.draw(display)