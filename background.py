#%%
import pygame,os
from setting import *
#%%
class Background:
    def __init__(self):
        sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png')).convert_alpha()
        
        self.background_image=pygame.Surface((114,256)).convert()
        self.background_image.blit(sheet_image,(0,0),(0,0,114,256))
        self.background_image=pygame.transform.scale(self.background_image,(450,800))
        self.background_rect=self.background_image.get_rect()
        
        self.ground_image=pygame.Surface((168,56)).convert()
        self.ground_image.blit(sheet_image,(0,0),(292,0,168,56))
        self.ground_image=pygame.transform.scale(self.ground_image,(450,150))
        self.ground_rect=self.ground_image.get_rect(bottom=screen_height)
    
    def update(self):
        self.ground_rect.x-=3
        if self.ground_rect.right<=0:
            self.ground_rect.left=0
    
    def draw(self,display):
        display.blit(self.background_image,self.background_rect)
        display.blit(self.ground_image,(self.ground_rect.x,self.ground_rect.y))
        display.blit(self.ground_image,(self.ground_rect.x+screen_width,self.ground_rect.y))
        print(self.ground_rect.top)