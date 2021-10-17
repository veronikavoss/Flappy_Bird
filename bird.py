#%%
import pygame
from setting import *
#%%
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bird_size=self.bird_w,self.bird_h=17,12
        self.color='yellow'
        self.index_img=0
        self.add_image()
        self.image=self.images[self.color][self.index_img]
        self.image=pygame.transform.scale(self.image,(self.bird_w*3,self.bird_h*3))
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect(centerx=120,centery=screen_height/2)
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.gravity=0.8
        self.jump_speed=-15
    
    def get_image(self,x):
        sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png')).convert_alpha()
        
        self.image=pygame.Surface(self.bird_size).convert_alpha()
        self.image.blit(sheet_image,(0,0),(3+((self.bird_w+11)*x),491,self.bird_w,self.bird_h))
        return self.image
    
    def add_image(self):
        temp=[]
        for i in range(3):
            temp.append(self.get_image(i))
            
        self.images={
            'yellow':temp[0:3]
        }
    
    def set_input(self):
        self.key_input=pygame.key.get_pressed()
        if self.key_input[pygame.K_SPACE]:
            self.dy=self.jump_speed
    
    def update(self):
        self.rect.y+=self.dy
        self.dy+=self.gravity
        self.set_input()
    
    def draw(self,display):
        display.blit(self.image,self.rect)