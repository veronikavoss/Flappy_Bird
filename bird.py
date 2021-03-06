#%%
from setting import *
#%%
class Bird(pygame.sprite.Sprite):
    def __init__(self,start_screen):
        super().__init__()
        self.start_screen=start_screen
        self.play_game=False
        self.crash_pipe=False
        self.game_over=False
        self.game_over_screen=False
        self.riging=False
        self.pressed=False
        
        self.bird_size=self.bird_w,self.bird_h=17,12
        self.color='yellow'
        self.action='standby'
        self.index_img=0
        self.sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png'))
        self.add_image()
        self.image=self.images[self.color][self.index_img]
        self.animation_speed=0.15
        
        self.start_pos()
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.dy=-1
        self.gravity_force=0
        self.jump_speed=-10
        
        self.limit_timer=pygame.USEREVENT+0
        pygame.time.set_timer(self.limit_timer,400)
    
    def start_pos(self):
        if self.start_screen:
            self.color='yellow'
            self.rect=self.image.get_rect(center=(screen_width/2,screen_height/2-30))
        else:
            self.color=choice(list(self.images.keys()))
            self.rect=self.image.get_rect(x=screen_width/4,y=ground_top/2)
    
    def add_image(self):
        self.images={
            'yellow':[],
            'blue':[],
            'red':[]
        }
        yellow=[[3,491,17,12],[31,491,17,12],[59,491,17,12]]
        blue=[[87,491,17,12],[115,329,17,12],[115,355,17,12]]
        red=[[115,381,17,12],[115,407,17,12],[115,433,17,12]]
        
        for pos in yellow:
            bird=pygame.Surface(self.bird_size)
            bird.blit(self.sheet_image,(0,0),pos)
            bird=pygame.transform.scale(bird,(self.bird_w*3,self.bird_h*3))
            bird.set_colorkey((0,0,0))
            self.images['yellow'].append(bird)
        for pos in blue:
            bird=pygame.Surface(self.bird_size)
            bird.blit(self.sheet_image,(0,0),pos)
            bird=pygame.transform.scale(bird,(self.bird_w*3,self.bird_h*3))
            bird.set_colorkey((0,0,0))
            self.images['blue'].append(bird)
        for pos in red:
            bird=pygame.Surface(self.bird_size)
            bird.blit(self.sheet_image,(0,0),pos)
            bird=pygame.transform.scale(bird,(self.bird_w*3,self.bird_h*3))
            bird.set_colorkey((0,0,0))
            self.images['red'].append(bird)
    
    def gravity(self):
        self.rect.y+=self.dy
        self.dy+=self.gravity_force
        
        if self.action=='start_screen' or self.action=='standby' or self.action=='die':
            self.gravity_force=0
        else:
            self.gravity_force=0.6
    
    def set_input(self,riging_sound):
        self.mouse_input=pygame.mouse.get_pressed()
        self.key_input=pygame.key.get_pressed()
        if (self.key_input[pygame.K_SPACE] or self.mouse_input[0]) and self.rect.top>-180:
            if not self.start_screen and self.action=='standby':
                self.play_game=True
            elif self.play_game and not self.game_over and not self.riging and not self.pressed:
                self.dy=self.jump_speed
                riging_sound.play()
                self.pressed=True
        else:
            self.pressed=False
    
    def collision(self,bird,pipes,crash_sound,die_sound):
        for pipe in pipes:
            if pygame.sprite.collide_mask(bird,pipe) and not self.crash_pipe:
                self.action='crash'
                crash_sound.play()
                die_sound.play()
                self.crash_pipe=True
                self.play_game=False
                self.game_over=True
    
    def set_action(self,crash_sound):
        if self.start_screen:
            self.action='start_screen'
        if self.play_game and self.dy<0:
            self.action='riging'
            self.riging=True
        elif self.play_game and self.dy>0:
            self.action='fall'
            self.riging=False
            
        if not self.start_screen and not self.play_game and not self.game_over and self.rect.top<screen_height//2:
            self.action='standby'
        elif self.play_game and self.rect.bottom>ground_top:
            self.action='die'
            crash_sound.play()
            self.play_game=False
            self.game_over=True
            
        if self.action=='crash' or self.action=='die':
            if self.rect.bottom>ground_top:
                self.dy=0
                self.rect.bottom=ground_top
                self.game_over_screen=True
    
    def animation(self):
        color=self.images[self.color]
        if not self.action=='die' and not self.action=='crash':
            self.index_img+=self.animation_speed
            if self.index_img>=len(color):
                self.index_img=0
            self.image=color[int(self.index_img)]
            if self.play_game and not self.game_over:
                self.image=pygame.transform.rotate(self.image,max(self.dy*-4,-90))
        else:
            self.image=color[2]
            self.image=pygame.transform.rotate(self.image,-90)
        self.image.set_colorkey((0,0,0))
    
    def update(self,bird,pipes,riging_sound,crash_sound,die_sound):
        self.gravity()
        self.set_input(riging_sound)
        self.collision(bird,pipes,crash_sound,die_sound)
        self.set_action(crash_sound)
        self.animation()