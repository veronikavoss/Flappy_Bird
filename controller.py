#%%
import pygame
from setting import *
from background import *
from bird import *
from pipe import *
#%%
class Controller:
    def __init__(self):
        self.background=Background()
        self.bird=Bird()
        self.bird_sprite=pygame.sprite.GroupSingle(self.bird)
        self.pipes=pygame.sprite.Group(Pipe())
    
    def update(self):
        if not self.bird.action=='die':
            self.background.update()
        self.bird.update()
    
    def draw(self,display):
        self.background.draw(display)
        self.bird_sprite.draw(display)
        self.pipes.draw(display)