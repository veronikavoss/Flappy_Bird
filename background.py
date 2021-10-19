#%%
import pygame,os
from setting import *
#%%
class Background:
    def __init__(self):
        sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png')).convert_alpha()
        
        # background_size=background_w,background_h=144,256
        self.background_image=pygame.Surface(background_size).convert()
        self.background_image.blit(sheet_image,(0,0),(0,0,background_w,background_h))
        self.background_image=pygame.transform.scale(self.background_image,screen_size)
        self.background_rect=self.background_image.get_rect()
        
        # ground_size=ground_w,ground_h=168,56
        self.ground_image=pygame.Surface(ground_size).convert()
        self.ground_image.blit(sheet_image,(0,0),(292,0,ground_w,ground_h))
        self.ground_image=pygame.transform.scale(self.ground_image,(screen_width,ground_h*3))
        self.ground_rect=self.ground_image.get_rect(bottom=screen_height)
    
    def update(self):
        self.ground_rect.x-=3
        if self.ground_rect.right<=0:
            self.ground_rect.left=0
    
    def draw(self,display):
        display.blit(self.background_image,self.background_rect)
        display.blit(self.ground_image,(self.ground_rect.x,self.ground_rect.y))
        display.blit(self.ground_image,(self.ground_rect.x+screen_width,self.ground_rect.y))