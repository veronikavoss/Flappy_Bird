#%%
import pygame
from setting import *
#%%
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bird_size=self.bird_w,self.bird_h=56,40
        self.image=pygame.Surface(self.bird_size)
        self.image.fill('blue')
        self.rect=self.image.get_rect(centerx=120,centery=screen_height/2)
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.gravity=0.8
        self.jump_speed=-15
    
    def key_input(self):
        pass
    
    def update(self):
        self.rect.y+=self.dy
        self.dy+=self.gravity