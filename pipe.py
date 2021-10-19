#%%
import pygame,os
from setting import *
#%%
class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.pipe_size=self.pipe_w,self.pipe_h=26,160
        self.add_image()
        self.image=self.images[0]
        self.ground_size=self.ground_w,self.ground_h=168,56
        self.image=pygame.transform.scale(self.image,(self.pipe_w*3,self.pipe_h*3))
        self.rect=self.image.get_rect(right=screen_width)
        self.image.set_colorkey((0,0,0))
    
    def get_image(self,blit_x):
        sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png')).convert_alpha()
        
        self.image=pygame.Surface(self.pipe_size).convert_alpha()
        self.image.blit(sheet_image,(0,0),(56+(28*blit_x),323,self.pipe_w,self.pipe_h))
        return self.image
    
    def add_image(self):
        self.images=[]
        for i in range(2):
            self.images.append(self.get_image(i))