#%%
import pygame,os
from setting import *
#%%
class Pipe(pygame.sprite.Sprite):
    def __init__(self,left,top):
        super().__init__()
        self.spawn_pipe=False
        
        self.pipe_size=self.pipe_w,self.pipe_h=26,160
        self.add_image()
        self.image1=self.images[1]
        self.image2=self.images[0]
        self.image1=pygame.transform.scale(self.image1,(self.pipe_w*3,self.pipe_h*3))
        self.image2=pygame.transform.scale(self.image2,(self.pipe_w*3,self.pipe_h*3))
        self.rect1=self.image1.get_rect(left=left,top=top)
        self.rect2=self.image2.get_rect(left=left,y=self.rect1.top-self.rect1.h-200)
        # self.rect=self.image2.get_rect(right=screen_width,top=512)
        self.image1.set_colorkey((0,0,0))
        self.image2.set_colorkey((0,0,0))
    
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
        self.rect1.x-=3
        self.rect2.x-=3
    
    def draw(self,display):
        self.image1=pygame.transform.scale(self.image1,(self.pipe_w*3,self.pipe_h*3))
        self.image1.set_colorkey((0,0,0))
        display.blit(self.image1,self.rect1)
        
        self.image2=pygame.transform.scale(self.image2,(self.pipe_w*3,self.pipe_h*3))
        self.image2.set_colorkey((0,0,0))
        display.blit(self.image2,self.rect2)