#%%
import pygame
from setting import *
from bird import *
from background import *
#%%
class Controller:
    def __init__(self):
        self.bird=pygame.sprite.GroupSingle(Bird())
        self.background=Background()
    
    def update(self):
        self.bird.update()
    
    def draw(self,display):
        self.background.draw(display)
        self.bird.draw(display)