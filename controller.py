#%%
import pygame
from setting import *
from ground import *
from bird import *
from pipe import *
#%%
class Controller:
    def __init__(self):
        self.background()
        self.ground=Ground()
        self.pipe=Pipe(screen_width,212)
        self.pipes=pygame.sprite.Group()
        self.bird=Bird()
        self.bird_sprite=pygame.sprite.GroupSingle(self.bird)
        
        self.pipe_spawn_cooldown=pygame.USEREVENT+2
        pygame.time.set_timer(self.pipe_spawn_cooldown,1500)
    
    def background(self):
        sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png')).convert_alpha()
        self.background_image=pygame.Surface(background_size).convert()
        self.background_image.blit(sheet_image,(0,0),(0,0,background_w,background_h))
        self.background_image=pygame.transform.scale(self.background_image,screen_size)
        self.background_rect=self.background_image.get_rect()
    
    def create_pipe(self):
        self.pipe=Pipe(512)
    
    def collision(self):
        for pipe in self.pipes:
            if pygame.collide_mask(self.bird_sprite,pipe):
                print('collide')
    
    def update(self):
        self.pipe.update()
        self.pipes.update()
        if not self.bird.action=='die':
            self.ground.update()
        self.bird_sprite.update()
    
    def draw(self,display):
        display.blit(self.background_image,self.background_rect)
        
        self.pipe.draw(display)
        self.pipes.draw(display)
        self.ground.draw(display)
        self.bird_sprite.draw(display)
        
        print(self.pipe.rect1)
        print(self.pipe.rect2)