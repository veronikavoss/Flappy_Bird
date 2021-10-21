#%%
import pygame,os
from setting import *
#%%
class Pipe(pygame.sprite.Sprite):
    def __init__(self,midtop,img):
        super().__init__()
        self.pipe_size=self.pipe_w,self.pipe_h=26,160
        self.add_image()
        self.image=self.images[img]
        self.image=pygame.transform.scale(self.image,(self.pipe_w*3,self.pipe_h*3))
        self.rect=self.image.get_rect(midtop=midtop)
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
    
    def update(self):
        self.rect.x-=game_speed