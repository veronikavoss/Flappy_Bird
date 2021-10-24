#%%
from random import *
from setting import *
from ground import *
from bird import *
from pipe import *
#%%
class Controller:
    def __init__(self):
        self.start_screen=True
        
        self.add_image()
        self.add_sound()
        self.background()
        self.pipes=pygame.sprite.Group()
        self.ground=Ground()
        self.bird=Bird()
        self.bird_sprite=pygame.sprite.GroupSingle(self.bird)
        self.score=0
        self.update_score=0
        
        self.pipe_spawn_cooldown=pygame.USEREVENT+2
        pygame.time.set_timer(self.pipe_spawn_cooldown,1200)
        self.tap_motion=pygame.USEREVENT+3
        pygame.time.set_timer(self.tap_motion,1000)
    
    def add_sound(self):
        self.sfx_die=pygame.mixer.Sound(os.path.join(sound_path,'sfx_die.wav'))
        self.sfx_die.set_volume(0.5)
        self.sfx_hit=pygame.mixer.Sound(os.path.join(sound_path,'sfx_hit.wav'))
        self.sfx_hit.set_volume(0.5)
        self.sfx_point=pygame.mixer.Sound(os.path.join(sound_path,'sfx_point.wav'))
        self.sfx_point.set_volume(0.5)
        self.sfx_swooshing=pygame.mixer.Sound(os.path.join(sound_path,'sfx_swooshing.wav'))
        self.sfx_swooshing.set_volume(0.5)
        self.sfx_wing=pygame.mixer.Sound(os.path.join(sound_path,'sfx_wing.wav'))
        self.sfx_wing.set_volume(0.5)
    
    def get_number_image(self,num_x):
        self.sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png'))
        num_size=num_w,num_h=12,18
        num_image=pygame.Surface(num_size)
        num_image.blit(self.sheet_image,(0,0),(292+num_x*14,160,num_w,num_h))
        num_image=pygame.transform.scale(num_image,(num_w*3,num_h*3))
        num_image.set_colorkey((0,0,0))
        return num_image
    
    def add_image(self):
        self.images={
            'logo':'',
            'play_button':'',
            'score_num':[],
            'ready':'',
            'tap':'',
            'game_over':'',
            'score_board':'',
            'rank':'',
            'medal':[]
        }
        for num_x in range(10):
            self.images['score_num'].append(self.get_number_image(num_x))
        
        logo_img=pygame.Surface((89,24))
        logo_img.blit(self.sheet_image,(0,0),(351,91,89,24))
        logo_img=pygame.transform.scale(logo_img,(89*3,24*3))
        logo_img.set_colorkey((0,0,0))
        self.logo_img_rect=logo_img.get_rect(center=(screen_width/2,300))
        self.images['logo']=logo_img
        
        play_button_img=pygame.Surface((52,29))
        play_button_img.blit(self.sheet_image,(0,0),(354,118,52,29))
        play_button_img=pygame.transform.scale(play_button_img,(52*3,29*3))
        play_button_img.set_colorkey((0,0,0))
        self.start_play_button_img_rect=play_button_img.get_rect(center=(screen_width/2,500))
        self.game_over_play_button_img_rect=play_button_img.get_rect(center=(screen_width/4,500))
        self.images['play_button']=play_button_img
        
        ready_img=pygame.Surface((92,25))
        ready_img.blit(self.sheet_image,(0,0),(295,59,92,25))
        ready_img=pygame.transform.scale(ready_img,(92*3,25*3))
        ready_img.set_colorkey((0,0,0))
        self.ready_img_rect=ready_img.get_rect(center=(screen_width/2,200))
        self.images['ready']=ready_img
        
        tap_img=pygame.Surface((57,49))
        tap_img.blit(self.sheet_image,(0,0),(292,91,57,49))
        tap_img=pygame.transform.scale(tap_img,(57*3,49*3))
        tap_img.set_colorkey((0,0,0))
        self.tap_img_rect=tap_img.get_rect(center=(screen_width/2,500))
        self.images['tap']=tap_img
        
        game_over_img=pygame.Surface((96,21))
        game_over_img.blit(self.sheet_image,(0,0),(395,59,96,21))
        game_over_img=pygame.transform.scale(game_over_img,(96*3,21*3))
        game_over_img.set_colorkey((0,0,0))
        self.game_over_img_rect=game_over_img.get_rect(center=(screen_width/2,100))
        self.images['game_over']=game_over_img
        
        score_board_img=pygame.Surface((113,57))
        score_board_img.blit(self.sheet_image,(0,0),(3,259,113,57))
        score_board_img=pygame.transform.scale(score_board_img,(113*3,57*3))
        score_board_img.set_colorkey((0,0,0))
        self.score_board_img_rect=score_board_img.get_rect(centerx=screen_width/2,bottom=screen_height/2)
        self.images['score_board']=score_board_img
        
        rank_img=pygame.Surface((52,29))
        rank_img.blit(self.sheet_image,(0,0),(414,118,52,29))
        rank_img=pygame.transform.scale(rank_img,(52*3,29*3))
        rank_img.set_colorkey((0,0,0))
        self.rank_img_rect=rank_img.get_rect(center=(screen_width-(screen_width/4),500))
        self.images['rank']=rank_img
        
        medal_pos=[[121,258,22,22],[121,282,22,22],[112,453,22,22],[112,477,22,22]]
        for pos in medal_pos:
            medal_img=pygame.Surface((22,22))
            medal_img.blit(self.sheet_image,(0,0),pos)
            medal_img=pygame.transform.scale(medal_img,(22*3,22*3))
            medal_img.set_colorkey((0,0,0))
            self.images['medal'].append(medal_img)
        self.medal_img_rect=medal_img.get_rect(center=(118,310))
    
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
                    self.sfx_point.play()
                    self.update_score=pipe.rect.left
    
    def update(self):
        if self.bird.play_game and not self.bird.game_over:
            self.pipes.update()
        if not self.bird.action=='die' and not self.bird.action=='crash':
            self.ground.update()
        self.bird_sprite.update(*self.bird_sprite,self.pipes,self.sfx_wing,self.sfx_hit,self.sfx_die)
        self.set_score()
    
    def text(self,display):
        font=pygame.font.SysFont(None,80)
        text=font.render(str(self.score//2),True,'white')
        text_rect=text.get_rect(center=(screen_width//2,100))
        blit=display.blit(text,text_rect)
        return blit
    
    def blit_start_screen(self,display):
        if self.start_screen:
            display.blit(self.images['logo'],self.logo_img_rect)
            display.blit(self.images['score_board'],self.score_board_img_rect)
            display.blit(self.images['play_button'],self.game_over_play_button_img_rect)
    
    def blit_standby_screen(self,display):
        if self.bird.action=='standby':
            display.blit(self.images['ready'],self.ready_img_rect)
            display.blit(self.images['tap'],self.tap_img_rect)
        else:
            self.pipes.draw(display)
    
    def blit_number(self,display,y):
        pos_x=len(str(self.score//2))
        if pos_x==1:
            number1=self.images['score_num'][int(str(self.score//2)[-1])]
            number1_rect=number1.get_rect(x=(((screen_width//2)-36)+(18*pos_x)),y=y)
            display.blit(number1,number1_rect)
        elif pos_x==2:
            number1=self.images['score_num'][int(str(self.score//2)[-1])]
            number1_rect=number1.get_rect(x=(((screen_width//2)-36)+(18*pos_x)),y=y)
            number2=self.images['score_num'][int(str(self.score//2)[-2])]
            number2_rect=number2.get_rect(x=(((screen_width//2)-72)+(18*pos_x)),y=y)
            display.blit(number1,number1_rect)
            display.blit(number2,number2_rect)
        elif pos_x==3:
            number1=self.images['score_num'][int(str(self.score//2)[-1])]
            number1_rect=number1.get_rect(x=(((screen_width//2)-36)+(18*pos_x)),y=y)
            number2=self.images['score_num'][int(str(self.score//2)[-2])]
            number2_rect=number2.get_rect(x=(((screen_width//2)-72)+(18*pos_x)),y=y)
            number3=self.images['score_num'][int(str(self.score//2)[-3])]
            number3_rect=number3.get_rect(x=(((screen_width//2)-108)+(18*pos_x)),y=y)
            display.blit(number1,number1_rect)
            display.blit(number2,number2_rect)
            display.blit(number3,number3_rect)
        elif pos_x==4:
            number1=self.images['score_num'][int(str(self.score//2)[-1])]
            number1_rect=number1.get_rect(x=(((screen_width//2)-36)+(18*pos_x)),y=y)
            number2=self.images['score_num'][int(str(self.score//2)[-2])]
            number2_rect=number2.get_rect(x=(((screen_width//2)-72)+(18*pos_x)),y=y)
            number3=self.images['score_num'][int(str(self.score//2)[-3])]
            number3_rect=number3.get_rect(x=(((screen_width//2)-108)+(18*pos_x)),y=y)
            number4=self.images['score_num'][int(str(self.score//2)[-4])]
            number4_rect=number4.get_rect(x=(((screen_width//2)-144)+(18*pos_x)),y=y)
            display.blit(number1,number1_rect)
            display.blit(number2,number2_rect)
            display.blit(number3,number3_rect)
            display.blit(number4,number4_rect)
    
    def blit_game_over_screen(self,display):
        if self.bird.game_over_screen:
            display.blit(self.images['game_over'],self.game_over_img_rect)
            display.blit(self.images['score_board'],self.score_board_img_rect)
            display.blit(self.images['play_button'],self.game_over_play_button_img_rect)
            display.blit(self.images['rank'],self.rank_img_rect)
            if self.score//2>=40:
                display.blit(self.images['medal'][0],self.medal_img_rect)
            elif self.score//2>=30:
                display.blit(self.images['medal'][1],self.medal_img_rect)
            elif self.score//2>=20:
                display.blit(self.images['medal'][2],self.medal_img_rect)
            elif self.score//2>=10:
                display.blit(self.images['medal'][3],self.medal_img_rect)
        else:
            self.blit_number(display,50)
    
    def draw(self,display):
        display.blit(self.background_image,self.background_rect)
        self.ground.draw(display)
        # self.blit_start_screen(display)
        self.blit_standby_screen(display)
        self.bird_sprite.draw(display)
        self.blit_game_over_screen(display)
        # self.text(display)