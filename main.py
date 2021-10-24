#%%
from controller import *
#%%
class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.mixer.pre_init(44100,-16,2,512)
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
        self.bird_move_count=0
        self.tap_count=0
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
                quit()
            
            if event.type==self.controller.bird.limit_timer and self.controller.bird.action=='standby':
                self.bird_move_count+=1
                if self.bird_move_count%2==0:
                    self.controller.bird.dy=-1
                else:
                    self.controller.bird.dy=1
            if event.type==self.controller.tap_motion and self.controller.bird.action=='standby':
                self.tap_count+=1
                if self.tap_count%2==0:
                    self.controller.tap_img_rect.y+=10
                else:
                    self.controller.tap_img_rect.y-=10
            if event.type==self.controller.pipe_spawn_cooldown and self.controller.bird.play_game and not self.controller.bird.game_over:
                self.controller.create_pipe()
            
            if self.controller.bird.game_over:
                mouse_pos=pygame.mouse.get_pos()
                if  event.type==pygame.MOUSEBUTTONUP and self.controller.game_over_play_button_img_rect.collidepoint(mouse_pos):
                    self.controller.sfx_swooshing.play()
                    self.game_start()
    
    def update(self):
        self.controller.update()
    
    def draw(self):
        self.controller.draw(self.screen)

flappy_bird=Game()
pygame.quit()