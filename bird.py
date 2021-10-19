#%%
import pygame
from setting import *
#%%
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.play_game=False
        
        self.bird_size=self.bird_w,self.bird_h=17,12
        self.color='yellow'
        self.action='standby'
        self.index_img=0
        self.add_image()
        self.image=self.images[self.color][self.index_img]
        self.image=pygame.transform.scale(self.image,(self.bird_w*3,self.bird_h*3))
        self.image.set_colorkey((0,0,0))
        self.animation_speed=0.15
        
        self.rect=self.image.get_rect(x=screen_width/4,y=(screen_height-(ground_h*3))/2)
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.dy=-1
        self.gravity_force=0
        self.jump_speed=-6
        
        self.limit_time=True
        self.limit_timer=pygame.USEREVENT
        pygame.time.set_timer(self.limit_timer,400)
    
    def get_image(self,x):
        sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png')).convert_alpha()
        
        self.image=pygame.Surface(self.bird_size).convert_alpha()
        self.image.blit(sheet_image,(0,0),(3+((self.bird_w+11)*x),491,self.bird_w,self.bird_h))
        return self.image
    
    def add_image(self):
        temp=[]
        for i in range(3):
            temp.append(self.get_image(i))
        temp.append(temp[1])
        
        self.images={
            'yellow':temp[0:len(temp)]
        }
    
    def gravity(self):
        self.rect.y+=self.dy
        self.dy+=self.gravity_force
        
        if self.action=='standby':
            self.gravity_force=0
        else:
            self.gravity_force=0.5
    
    def set_input(self):
        self.key_input=pygame.key.get_pressed()
        if self.key_input[pygame.K_SPACE]:
            self.play_game=True
            self.dy=self.jump_speed
    
    def set_action(self):
        if self.play_game and self.dy<0:
            self.action='riging'
        else:
            self.action='fall'
            
        if not self.play_game and self.rect.bottom<screen_height-ground_h*3:
            self.action='standby'
        elif self.play_game and self.rect.bottom<screen_height-ground_h*3:
            self.action='playing'
        else:
            self.action='die'
            self.dy=0
            self.gravity_force=0
            self.rect.bottom=screen_height-ground_h*3
            self.play_game=True
    
    def animation(self):
        color=self.images[self.color]
        self.index_img+=self.animation_speed
        if not self.action=='die':
            if self.index_img>=len(color):
                self.index_img=0
            self.image=color[int(self.index_img)]
            self.image=pygame.transform.scale(self.image,(self.bird_w*3,self.bird_h*3))
            if self.action=='playing':
                self.image=pygame.transform.rotozoom(self.image,max(self.dy*-4,-90),1)
            # elif self.action=='die':
            #     self.image=pygame.transform.rotozoom(self.image,-90,1)
        self.image.set_colorkey((0,0,0))
    
    def update(self):
        self.gravity()
        self.set_input()
        self.set_action()
        self.animation()
    
    # def draw(self,display):
    #     display.blit(self.image,self.rect)
        # print(self.action,self.rect.y,self.dy,self.gravity_force)
        print(self.dy*-4)