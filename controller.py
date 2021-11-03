#%%
from setting import *
from ground import *
from bird import *
from pipe import *
#%%
class Controller:
    def __init__(self,start_screen,high_score):
        self.start_screen=start_screen
        self.high_score=high_score
        
        self.pipe_spawn=False
        
        self.sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png'))
        self.add_image()
        self.choice_element()
        self.add_sound()
        self.pipes=pygame.sprite.Group()
        self.ground=Ground()
        self.bird=Bird(self.start_screen)
        self.bird_sprite=pygame.sprite.GroupSingle(self.bird)
        self.score=0
        self.update_score=0
        
        self.tap_motion=pygame.USEREVENT+1
        pygame.time.set_timer(self.tap_motion,800)
        self.pipe_spawn_cooldown=1300
        self.pipe_spawn_update=0
    
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
    
    def get_number_image(self,num_x,size):
        num_size=num_w,num_h=12,18
        num_image=pygame.Surface(num_size)
        num_image.blit(self.sheet_image,(0,0),(292+num_x*14,160,num_w,num_h))
        num_image=pygame.transform.scale(num_image,(num_w*size,num_h*size))
        num_image.set_colorkey((0,0,0))
        return num_image
    
    def add_image(self):
        self.images={
            'background':[],
            'logo':'',
            'play_button':'',
            'score_num':[],
            'score_small_num':[],
            'ready':'',
            'tap':'',
            'game_over':'',
            'rank':'',
            'score_board':'',
            'new':'',
            'medal':[]
        }
        for i in range(2):
            background=pygame.Surface(background_size)
            background.blit(self.sheet_image,(0,0),(i*146,0,background_w,background_h))
            background=pygame.transform.scale(background,(background_w*3,background_h*3))
            self.images['background'].append(background)
        
        for num_x in range(10):
            self.images['score_num'].append(self.get_number_image(num_x,3))
        
        for num_x in range(10):
            self.images['score_small_num'].append(self.get_number_image(num_x,2))
        
        logo_img=pygame.Surface((89,24))
        logo_img.blit(self.sheet_image,(0,0),(351,91,89,24))
        logo_img=pygame.transform.scale(logo_img,(89*3,24*3))
        logo_img.set_colorkey((0,0,0))
        self.logo_img_rect=logo_img.get_rect(center=(screen_width/2,200))
        self.images['logo']=logo_img
        
        play_button_img=pygame.Surface((52,29))
        play_button_img.blit(self.sheet_image,(0,0),(354,118,52,29))
        play_button_img=pygame.transform.scale(play_button_img,(52*3,29*3))
        play_button_img.set_colorkey((0,0,0))
        self.start_play_button_img_rect=play_button_img.get_rect(center=(screen_width/2,500))
        self.game_over_play_button_img_rect=play_button_img.get_rect(center=(screen_width//4+10,500))
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
        
        rank_img=pygame.Surface((52,29))
        rank_img.blit(self.sheet_image,(0,0),(414,118,52,29))
        rank_img=pygame.transform.scale(rank_img,(52*3,29*3))
        rank_img.set_colorkey((0,0,0))
        self.rank_img_rect=rank_img.get_rect(center=(screen_width-(screen_width//4)-10,500))
        self.images['rank']=rank_img
        
        score_board_img=pygame.Surface((113,57))
        score_board_img.blit(self.sheet_image,(0,0),(3,259,113,57))
        score_board_img=pygame.transform.scale(score_board_img,(113*3,57*3))
        score_board_img.set_colorkey((0,0,0))
        self.score_board_img_rect=score_board_img.get_rect(centerx=screen_width/2,bottom=screen_height/2)
        self.images['score_board']=score_board_img
        
        new_img=pygame.Surface((16,7))
        new_img.blit(self.sheet_image,(0,0),(112,501,16,7))
        new_img=pygame.transform.scale(new_img,(16*3,7*3))
        new_img.set_colorkey((0,0,0))
        self.new_img_rect=new_img.get_rect(x=250,y=300)
        self.images['new']=new_img
        
        medal_pos=[[121,258,22,22],[121,282,22,22],[112,453,22,22],[112,477,22,22]]
        for pos in medal_pos:
            medal_img=pygame.Surface((22,22))
            medal_img.blit(self.sheet_image,(0,0),pos)
            medal_img=pygame.transform.scale(medal_img,(22*3,22*3))
            medal_img.set_colorkey((0,0,0))
            self.images['medal'].append(medal_img)
        self.medal_img_rect=medal_img.get_rect(center=(118,310))
    
    def choice_element(self):
        self.choice_background=randrange(0,len(self.images['background']))
    
    def background(self,display):
        if self.start_screen:
            display.blit(self.images['background'][0],(0,0))
        else:
            display.blit(self.images['background'][self.choice_background],(0,0))
    
    def create_pipe(self):
        if self.bird.play_game and not self.bird.game_over and not self.pipe_spawn:
            top=randrange(300,501,50)
            self.top_pipe=Pipe((screen_width+300,top-680),0)
            self.bottom_pipe=Pipe((screen_width+300,top),1)
            self.pipes.add(self.bottom_pipe,self.top_pipe)
            self.pipe_spawn=True
            self.pipe_spawn_update=pygame.time.get_ticks()
        elif self.bird.play_game and not self.bird.game_over and self.pipe_spawn:
            current_time=pygame.time.get_ticks()
            if current_time-self.pipe_spawn_update>=self.pipe_spawn_cooldown:
                self.pipe_spawn=False
    
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
        self.create_pipe()
        self.set_score()
    
    def blit_start_screen(self,display):
        display.blit(self.images['logo'],self.logo_img_rect)
        display.blit(self.images['play_button'],self.game_over_play_button_img_rect)
        display.blit(self.images['rank'],self.rank_img_rect)
    
    def blit_standby_screen(self,display):
        if self.bird.action=='standby':
            display.blit(self.images['ready'],self.ready_img_rect)
            display.blit(self.images['tap'],self.tap_img_rect)
        else:
            self.pipes.draw(display)
    
    def blit_score(self,display,y):
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
    
    def blit_small_score(self,display):
        num_x,num_y,high_num_y=330,260,324
        num_w,num_h=24,36
        score=str(self.score//2)
        score_len=len(score)
        high_score=str(max(self.high_score))
        high_score_len=len(high_score)
        
        if self.bird.game_over_screen:
            if max(self.high_score)>=self.score//2:
                if score_len==1:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,num_y))
                elif score_len==2:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,num_y))
                    display.blit(self.images['score_small_num'][int(score[-2])],(num_x-num_w,num_y))
                elif score_len==3:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,num_y))
                    display.blit(self.images['score_small_num'][int(score[-2])],(num_x-num_w,num_y))
                    display.blit(self.images['score_small_num'][int(score[-3])],(num_x-num_w*2,num_y))
                elif score_len==4:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,num_y))
                    display.blit(self.images['score_small_num'][int(score[-2])],(num_x-num_w,num_y))
                    display.blit(self.images['score_small_num'][int(score[-3])],(num_x-num_w*2,num_y))
                    display.blit(self.images['score_small_num'][int(score[-4])],(num_x-num_w*3,num_y))
                
                if high_score_len==1:
                    display.blit(self.images['score_small_num'][int(high_score[-1])],(num_x,high_num_y))
                elif high_score_len==2:
                    display.blit(self.images['score_small_num'][int(high_score[-1])],(num_x,high_num_y))
                    display.blit(self.images['score_small_num'][int(high_score[-2])],(num_x-num_w,high_num_y))
                elif high_score_len==3:
                    display.blit(self.images['score_small_num'][int(high_score[-1])],(num_x,high_num_y))
                    display.blit(self.images['score_small_num'][int(high_score[-2])],(num_x-num_w,high_num_y))
                    display.blit(self.images['score_small_num'][int(high_score[-3])],(num_x-num_w*2,high_num_y))
                elif high_score_len==4:
                    display.blit(self.images['score_small_num'][int(high_score[-1])],(num_x,high_num_y))
                    display.blit(self.images['score_small_num'][int(high_score[-2])],(num_x-num_w,high_num_y))
                    display.blit(self.images['score_small_num'][int(high_score[-3])],(num_x-num_w*2,high_num_y))
                    display.blit(self.images['score_small_num'][int(high_score[-4])],(num_x-num_w*3,high_num_y))
            else:
                display.blit(self.images['new'],self.new_img_rect)
                if score_len==1:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,num_y))
                elif score_len==2:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,num_y))
                    display.blit(self.images['score_small_num'][int(score[-2])],(num_x-num_w,num_y))
                elif score_len==3:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,num_y))
                    display.blit(self.images['score_small_num'][int(score[-2])],(num_x-num_w,num_y))
                    display.blit(self.images['score_small_num'][int(score[-3])],(num_x-num_w*2,num_y))
                elif score_len==4:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,num_y))
                    display.blit(self.images['score_small_num'][int(score[-2])],(num_x-num_w,num_y))
                    display.blit(self.images['score_small_num'][int(score[-3])],(num_x-num_w*2,num_y))
                    display.blit(self.images['score_small_num'][int(score[-4])],(num_x-num_w*3,num_y))
                
                if score_len==1:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,high_num_y))
                elif score_len==2:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,high_num_y))
                    display.blit(self.images['score_small_num'][int(score[-2])],(num_x-num_w,high_num_y))
                elif score_len==3:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,high_num_y))
                    display.blit(self.images['score_small_num'][int(score[-2])],(num_x-num_w,high_num_y))
                    display.blit(self.images['score_small_num'][int(score[-3])],(num_x-num_w*2,high_num_y))
                elif score_len==4:
                    display.blit(self.images['score_small_num'][int(score[-1])],(num_x,high_num_y))
                    display.blit(self.images['score_small_num'][int(score[-2])],(num_x-num_w,high_num_y))
                    display.blit(self.images['score_small_num'][int(score[-3])],(num_x-num_w*2,high_num_y))
                    display.blit(self.images['score_small_num'][int(score[-4])],(num_x-num_w*3,high_num_y))
    
    def blit_game_over_screen(self,display):
        if self.bird.game_over_screen:
            display.blit(self.images['game_over'],self.game_over_img_rect)
            display.blit(self.images['play_button'],self.game_over_play_button_img_rect)
            display.blit(self.images['rank'],self.rank_img_rect)
            display.blit(self.images['score_board'],self.score_board_img_rect)
            self.blit_small_score(display)
            if self.score//2>=40:
                display.blit(self.images['medal'][0],self.medal_img_rect)
            elif self.score//2>=30:
                display.blit(self.images['medal'][1],self.medal_img_rect)
            elif self.score//2>=20:
                display.blit(self.images['medal'][2],self.medal_img_rect)
            elif self.score//2>=10:
                display.blit(self.images['medal'][3],self.medal_img_rect)
        else:
            self.blit_score(display,50)
    
    def draw(self,display):
        if self.start_screen:
            self.background(display)
            self.ground.draw(display)
            self.bird_sprite.draw(display)
            self.blit_start_screen(display)
        else:
            self.background(display)
            self.blit_standby_screen(display)
            self.ground.draw(display)
            self.bird_sprite.draw(display)
            self.blit_game_over_screen(display)