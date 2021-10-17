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
        self.current_dir=os.path.dirname(os.path.abspath(__file__))
        self.image=os.path.join(self.current_dir,'image','flappy_bird_sheet_1.png')
        self.start_screen()
    
    def start_screen(self):
        self.game_start()
    
    def game_start(self):
        self.controller=Controller()
        self.loop()
    
    def loop(self):
        self.playing=True
        while self.playing:
            self.fps=self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
    
    def event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.playing=False
    
    def update(self):
        self.controller.update()
    
    def draw(self):
        self.screen.fill('black')
        self.screen.blit(pygame.image.load(self.image),(0,0),(0,0,114,256))
        # self.image=pygame.transform.scale(self.image,(450,800))
        self.controller.draw(self.screen)

flappy_bird=Game()
pygame.quit()