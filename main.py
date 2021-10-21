#%%
import pygame,os
from setting import *
from controller import *
#%%
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.display.set_caption(title)
        self.screen=pygame.display.set_mode(screen_size)
        self.clock=pygame.time.Clock()
        self.start_screen()
    
    def start_screen(self):
        # self.controller=Controller()
        # if not self.controller.bird.play_game:
        #     self.game_start()
        self.game_start()
    
    def game_start(self):
        self.controller=Controller()
        self.loop()
    
    def loop(self):
        self.playing=True
        while self.playing:
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
            self.fps=self.clock.tick(FPS)
    
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
            
            if event.type==self.controller.bird.limit_timer and self.controller.bird.action=='standby':
                if self.controller.bird.limit_time:
                    self.controller.bird.dy=1
                    self.controller.bird.limit_time=False 
                else:
                    self.controller.bird.dy=-1
                    self.controller.bird.limit_time=True
            if event.type==self.controller.pipe_spawn_cooldown and self.controller.bird.play_game and not self.controller.bird.game_over:
                self.controller.create_pipe()
            if event.type==self.controller.bird_pipe_crash and self.controller.bird.crash_pipe:
                print('crash')
            
            if event.type==pygame.KEYUP or event.type==pygame.MOUSEBUTTONUP:
                if self.controller.bird.game_over and self.controller.bird.rect.bottom==ground_top:
                    self.game_start()
    
    def update(self):
        self.controller.update()
    
    def draw(self):
        self.controller.draw(self.screen)

flappy_bird=Game()
pygame.quit()