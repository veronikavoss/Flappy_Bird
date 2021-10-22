#%%
from random import *

from setting import *
from ground import *
from bird import *
from pipe import *
#%%
class Controller:
    def __init__(self):
        self.add_image()
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
    
    def get_image(self,num_x):
        sheet_image=pygame.image.load(os.path.join(image_path,'flappy_bird_sheet_1.png'))
        num_size=num_w,num_h=12,18
        num_image=pygame.Surface(num_size)
        num_image.blit(sheet_image,(0,0),(292+num_x*14,160,num_w,num_h))
        return num_image
    
    def add_image(self):
        temp=[]
        for num_x in range(10):
            temp.append(self.get_image(num_x))
        self.images={
            'score_num':temp[0:10]
        }
    
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
    
    def number(self,display):
        pos_x=len(str(self.score//2))
        if pos_x==1:
            number1=self.images['score_num'][int(str(self.score//2)[-1])]
            number1=pygame.transform.scale(number1,(12*3,18*3))
            number1_rect=number1.get_rect(x=(((screen_width//2)-36)+(18*pos_x)),y=100)
            number1.set_colorkey((0,0,0))
            display.blit(number1,number1_rect)
        elif pos_x==2:
            number1=self.images['score_num'][int(str(self.score//2)[-1])]
            number1=pygame.transform.scale(number1,(12*3,18*3))
            number1_rect=number1.get_rect(x=(((screen_width//2)-36)+(18*pos_x)),y=100)
            number1.set_colorkey((0,0,0))
            number2=self.images['score_num'][int(str(self.score//2)[-2])]
            number2=pygame.transform.scale(number2,(12*3,18*3))
            number2_rect=number2.get_rect(x=(((screen_width//2)-72)+(18*pos_x)),y=100)
            number2.set_colorkey((0,0,0))
            display.blit(number1,number1_rect)
            display.blit(number2,number2_rect)
        elif pos_x==3:
            number1=self.images['score_num'][int(str(self.score//2)[-1])]
            number1=pygame.transform.scale(number1,(12*3,18*3))
            number1_rect=number1.get_rect(x=(((screen_width//2)-36)+(18*pos_x)),y=100)
            number1.set_colorkey((0,0,0))
            number2=self.images['score_num'][int(str(self.score//2)[-2])]
            number2=pygame.transform.scale(number2,(12*3,18*3))
            number2_rect=number2.get_rect(x=(((screen_width//2)-72)+(18*pos_x)),y=100)
            number2.set_colorkey((0,0,0))
            number3=self.images['score_num'][int(str(self.score//2)[-3])]
            number3=pygame.transform.scale(number3,(12*3,18*3))
            number3_rect=number3.get_rect(x=(((screen_width//2)-108)+(18*pos_x)),y=100)
            number3.set_colorkey((0,0,0))
            display.blit(number1,number1_rect)
            display.blit(number2,number2_rect)
            display.blit(number3,number3_rect)
        elif pos_x==4:
            number1=self.images['score_num'][int(str(self.score//2)[-1])]
            number1=pygame.transform.scale(number1,(12*3,18*3))
            number1_rect=number1.get_rect(x=(((screen_width//2)-36)+(18*pos_x)),y=100)
            number1.set_colorkey((0,0,0))
            number2=self.images['score_num'][int(str(self.score//2)[-2])]
            number2=pygame.transform.scale(number2,(12*3,18*3))
            number2_rect=number2.get_rect(x=(((screen_width//2)-72)+(18*pos_x)),y=100)
            number2.set_colorkey((0,0,0))
            number3=self.images['score_num'][int(str(self.score//2)[-3])]
            number3=pygame.transform.scale(number3,(12*3,18*3))
            number3_rect=number3.get_rect(x=(((screen_width//2)-108)+(18*pos_x)),y=100)
            number3.set_colorkey((0,0,0))
            number4=self.images['score_num'][int(str(self.score//2)[-4])]
            number4=pygame.transform.scale(number4,(12*3,18*3))
            number4_rect=number4.get_rect(x=(((screen_width//2)-144)+(18*pos_x)),y=100)
            number4.set_colorkey((0,0,0))
            display.blit(number1,number1_rect)
            display.blit(number2,number2_rect)
            display.blit(number3,number3_rect)
            display.blit(number4,number4_rect)
            
        print(len(str(self.score//2)),(((screen_width//2)-12)+(6*pos_x)))
    
    def draw(self,display):
        display.blit(self.background_image,self.background_rect)
        
        if not self.bird.action=='standby':
            self.pipes.draw(display)
        self.ground.draw(display)
        self.bird_sprite.draw(display)
        # self.text(display)
        self.number(display)
            