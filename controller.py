#%%
import pygame
from random import *
from setting import *
from ground import *
from bird import *
from pipe import *
#%%
class Controller:
    def __init__(self):
        self.background()
        self.pipes=pygame.sprite.Group()
        self.ground=Ground()
        self.bird=Bird()
        self.bird_sprite=pygame.sprite.GroupSingle(self.bird)
        self.score=0
        self.update_score=0
        
        self.pipe_spawn_cooldown=pygame.USEREVENT+2
        pygame.time.set_timer(self.pipe_spawn_cooldown,1200)
        self.bird_pipe_crash=pygame.USEREVENT+3
        pygame.time.set_timer(self.bird_pipe_crash,1000)
    
    def background(self):
        sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png')).convert_alpha()
        self.background_image=pygame.Surface(background_size).convert()
        self.background_image.blit(sheet_image,(0,0),(0,0,background_w,background_h))
        self.background_image=pygame.transform.scale(self.background_image,screen_size)
        self.background_rect=self.background_image.get_rect()
    
    def create_pipe(self):
        top=randrange(300,501,50)
        self.top_pipe=Pipe((screen_width,top-680),0)
        self.bottom_pipe=Pipe((screen_width,top),1)
        self.pipes.add(self.bottom_pipe,self.top_pipe)
    
    def set_score(self):
        for pipe in self.pipes:
            if pipe.rect.right<0:
                self.pipes.remove(pipe)
            if self.bird.play_game:
                if self.bird.rect.centerx>pipe.rect.centerx>self.bird.rect.centerx-2:
                    self.score+=1
                    self.update_score=pipe.rect.left
    
    def update(self):
        if self.bird.play_game and not self.bird.game_over:
            self.pipes.update()
        if not self.bird.action=='die' and not self.bird.action=='crash':
            self.ground.update()
        self.bird_sprite.update(*self.bird_sprite,self.pipes)
        self.set_score()
    
    def text(self,display):
        font=pygame.font.SysFont(None,80)
        text=font.render(str(self.score//2),True,'white')
        text_rect=text.get_rect(center=(screen_width//2,100))
        blit=display.blit(text,text_rect)
        return blit
    
    def draw(self,display):
        display.blit(self.background_image,self.background_rect)
        
        if not self.bird.action=='standby':
            self.pipes.draw(display)
        self.ground.draw(display)
        self.bird_sprite.draw(display)
        self.text(display)