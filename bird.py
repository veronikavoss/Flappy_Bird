#%%
import pygame
from setting import *
#%%
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.play_game=False
        self.crash_pipe=False
        self.game_over=False
        
        self.bird_size=self.bird_w,self.bird_h=17,12
        self.color='yellow'
        self.action='standby'
        self.index_img=0
        self.add_image()
        self.image=self.images[self.color][self.index_img]
        self.image=pygame.transform.scale(self.image,(self.bird_w*3,self.bird_h*3))
        self.image.set_colorkey((0,0,0))
        self.animation_speed=0.15
        
        self.rect=self.image.get_rect(x=screen_width/4,y=(ground_top/2))
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.dy=-1
        self.gravity_force=0
        self.jump_speed=-6
        
        self.limit_time=True
        self.limit_timer=pygame.USEREVENT+1
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
            'yellow':temp[0:4],
            # 'blue':temp[4:9],
            # 'red':temp[9:13]
        }
    
    def gravity(self):
        self.rect.y+=self.dy
        self.dy+=self.gravity_force
        
        if self.action=='standby' or self.action=='die':
            self.gravity_force=0
        else:
            self.gravity_force=0.6
    
    def set_input(self):
        self.mouse_input=pygame.mouse.get_pressed()
        self.key_input=pygame.key.get_pressed()
        if (self.key_input[pygame.K_SPACE] or self.mouse_input[0]) and self.rect.top>-180:
            if self.action=='standby':
                self.play_game=True
            elif self.play_game and not self.game_over:
                self.dy=self.jump_speed
    
    def collision(self,bird,pipes):
        for pipe in pipes:
            if pygame.sprite.collide_mask(bird,pipe):
                self.action='crash'
                self.play_game=False
                self.game_over=True
                self.crash_pipe=True
    
    def set_action(self):
        if self.play_game and self.dy<0:
            self.action='riging'
        elif self.play_game and self.dy>0:
            self.action='fall'
            
        if not self.play_game and not self.game_over and self.rect.top<screen_height//2:
            self.action='standby'
        elif self.play_game and self.rect.bottom>ground_top:
            self.action='die'
            self.play_game=False
            self.game_over=True
            
        if self.action=='crash' or self.action=='die':
            if self.rect.bottom>ground_top:
                self.dy=0
                self.rect.bottom=ground_top
    
    def animation(self):
        color=self.images[self.color]
        if not self.action=='die' and not self.action=='crash':
            self.index_img+=self.animation_speed
            if self.index_img>=len(color):
                self.index_img=0
            self.image=color[int(self.index_img)]
            self.image=pygame.transform.scale(self.image,(self.bird_w*3,self.bird_h*3))
            if self.play_game and not self.game_over:
                self.image=pygame.transform.rotozoom(self.image,max(self.dy*-4,-90),1)
        else:
            self.image=color[2]
            self.image=pygame.transform.scale(self.image,(self.bird_w*3,self.bird_h*3))
            self.image=pygame.transform.rotozoom(self.image,-90,1)
            # pygame.time.delay(2000)
        self.image.set_colorkey((0,0,0))
    
    def update(self,bird,pipes):
        self.gravity()
        self.set_input()
        self.collision(bird,pipes)
        self.set_action()
        self.animation()