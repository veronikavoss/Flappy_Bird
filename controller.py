#%%
import pygame
from setting import *
from bird import *
from background import *
#%%
class Controller:
    def __init__(self):
        self.bird=Bird()
        self.bird_sprite=pygame.sprite.GroupSingle(self.bird)
        self.background=Background()
    
    def update(self):
        if not self.bird.action=='die':
            self.background.update()
        self.bird.update()
    
    def draw(self,display):
        self.background.draw(display)
        self.bird_sprite.draw(display)