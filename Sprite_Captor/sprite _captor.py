import pygame,sys
from pygame.locals import *


BLACK=pygame.color.THECOLORS["black"]
WHITE=pygame.color.THECOLORS["white"]
RED=pygame.color.THECOLORS["red"]
GREEN=pygame.color.THECOLORS["green"]
BLUE=pygame.color.THECOLORS["blue"]
YELLOW=pygame.color.THECOLORS["yellow"]
SCREEN_WIDTH=640
SCREEN_HEIGHT=480
HALF_SCREEN_WIDTH=int(SCREEN_WIDTH/2)
HALF_SCREEN_HEIGHT=int(SCREEN_HEIGHT/2)


    
def scale_image(image, scale):
    return pygame.transform.scale(image, (image.get_width()*scale, image.get_height()*scale)).convert()


def scale_rect(rect, scale):
    rect.x *= scale
    rect.y *= scale
    rect.width *= scale
    rect.height *= scale

def center_rect(rect, center):
    sprite_pos = [0,0]
    sprite_pos[0] = center[0] - int(rect.width / 2)
    sprite_pos[1] = center[1] - int(rect.height / 2)
    return sprite_pos

def sprite_editor(screen, sprites, original_image):
    image = original_image.copy()
    sprites_leght = len(sprites)
    sprites_index = 0
    sprite_pos = [0,0]
    sprite_center =[HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT]
    sprite_original_move_speed = 5
    sprite_move_speed = sprite_original_move_speed
    sprite_rect = Rect([0, 0, 0, 0])
    if sprites_leght > sprites_index:
       sprite_rect = Rect(sprites[sprites_index]) 
       sprite_pos = center_rect(sprite_rect, sprite_center)
    scale = 1
    scale_max = 7
    clock=pygame.time.Clock()
    font=pygame.font.SysFont('Arial', 30)
    message = "Sprite Editor "
    message_time = 50
    text=font.render(message, True, YELLOW)
    text_pos = [0,0]
    text_pos[0] = HALF_SCREEN_WIDTH - int(text.get_width() / 2)
    text_pos[1] = HALF_SCREEN_HEIGHT - int(text.get_height() / 2)
    
    
    pygame.key.set_repeat(400, 30)

    while True:
        #loop speed limitation
        #30 frames per second is enought
        clock.tick(30)
        
        for event in pygame.event.get():    #wait for events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #keyboard commands    
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                   sprites_index += 1
                   if sprites_index >= sprites_leght:
                      sprites_index = sprites_leght-1
                   if sprites_leght > sprites_index:
                      sprite_rect = Rect(sprites[sprites_index])
                      scale_rect(sprite_rect, scale)
                      sprite_pos = center_rect(sprite_rect, sprite_center)
                elif event.key == K_LEFT:
                   sprites_index -= 1              
                   if sprites_index < 0:
                      sprites_index = 0
                   if sprites_leght > sprites_index:
                      sprite_rect = Rect(sprites[sprites_index])
                      scale_rect(sprite_rect, scale)
                      sprite_pos = center_rect(sprite_rect, sprite_center)
                elif event.key == K_UP:
                   #scale up the sprite 
                   if scale <  scale_max:
                      scale+=1
                   else:
                      scale = scale_max
                   #sprite_move_speed = sprite_original_move_speed * scale
                   image = scale_image(original_image, scale)
                   sprite_rect = Rect(sprites[sprites_index])
                   scale_rect(sprite_rect, scale)
                   sprite_pos = center_rect(sprite_rect, sprite_center)
                elif event.key == K_DOWN:
                   #scale down the sprite 
                   if scale >  1:
                      scale -= 1
                   else:
                      scale = 1
                   #sprite_move_speed = sprite_original_move_speed * scale
                   image = scale_image(original_image, scale)
                   sprite_rect = Rect(sprites[sprites_index])
                   scale_rect(sprite_rect, scale)
                   sprite_pos = center_rect(sprite_rect, sprite_center)
                elif event.key == K_o:
                   #set the sprite's position to origin
                   sprite_center[0] = int(sprite_rect[2] / 2)
                   sprite_center[1] = int(sprite_rect[3] / 2)
                   sprite_pos = center_rect(sprite_rect, sprite_center)
                elif event.key == K_c:
                   #center the sprite
                   sprite_center =[HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT]
                   sprite_pos = center_rect(sprite_rect, sprite_center)
                elif event.key == K_d:
                   #delete the current sprite
                   if sprites_leght > 0: 
                      del(sprites[sprites_index])
                      sprites_leght = len(sprites)
                      if sprites_index > sprites_leght-1:
                         sprites_index = sprites_leght-1
                      if sprites_leght > 0:
                         sprite_rect = Rect(sprites[sprites_index])
                         scale_rect(sprite_rect, scale)
                         sprite_pos = center_rect(sprite_rect, sprite_center)
                      message = "sprite deleted " +  str(sprites_leght) + " remained"
                      message_time = 50
                      text=font.render(message, True, YELLOW)
                      text_pos[0] = HALF_SCREEN_WIDTH - int(text.get_width() / 2)
                      text_pos[1] = HALF_SCREEN_HEIGHT - int(text.get_height() / 2)
                elif event.key == K_s:
                   #exit the sprite editor
                   return

                                 
        #move the sprite
        keys = pygame.key.get_pressed()
        if keys[K_u]:
           sprite_center[1] -= sprite_move_speed
           sprite_pos = center_rect(sprite_rect, sprite_center)
        elif keys[K_j]:
           sprite_center[1] += sprite_move_speed
           sprite_pos = center_rect(sprite_rect, sprite_center)
        if keys[K_h]:
           sprite_center[0] -= sprite_move_speed
           sprite_pos = center_rect(sprite_rect, sprite_center)
        elif keys[K_k]:
           sprite_center[0] += sprite_move_speed
           sprite_pos = center_rect(sprite_rect, sprite_center)
              
                    
        #draw everything
        screen.fill(BLACK)
        if sprites_leght > 0:
           screen.blit(image, sprite_pos, sprite_rect)
        if message_time > 0:
           message_time -= 1
           if message_time < 0:
              message_time = 0
           text=font.render(message, True, YELLOW)
           screen.blit(text, text_pos)           
        pygame.display.flip()

    
class Sprite_Captor():
    def __init__(self):
        self.rect = Rect([0, 0, 0, 0])
        self.line_thickness = 5
        self.scale = 1
        self.colors = [WHITE, GREEN, BLACK]
        self.colors_lenght = len(self.colors)-1
        self.color = self.colors[1]
        self.color_index = 0
        self.color_max_time = 15
        self.timer = 0
        self.increment = 1
        self.gripping = False
        
    def update(self, event, image, image_pos):
        if event.type == MOUSEBUTTONDOWN:
           if event.button == 1:
              self.rect.x, self.rect.y = event.pos
              self.rect.width = 0
              self.rect.height = 0
              self.gripping = True
        elif event.type == MOUSEBUTTONUP:
           if event.button == 1: 
             self.gripping = False
             if self.rect.width < 0:
                self.rect.width *= -1
                self.rect.x -= self.rect.width
             if self.rect.height < 0:
                self.rect.height *= -1
                self.rect.y -= self.rect.height
             image_rect = image.get_rect()
             image_rect.topleft = image_pos
             #check for overflow
             if self.rect.right > image_rect.right \
             or self.rect.left < image_rect.left \
             or self.rect.bottom > image_rect.bottom \
             or self.rect.top < image_rect.top:
                self.rect.topleft = image_rect.topleft
                self.rect.size = (0,0)
             self.rect.x -= image_pos[0]
             self.rect.y -= image_pos[1]
             """#capture the whole image if we get nothing
             if not self.capture_sprite(image):
                self.rect.topleft = (0,0)
                self.rect.width = image.get_width() - 1
                self.rect.height = image.get_height() - 1
                self.capture_sprite(image)"""
             self.capture_sprite(image)
             self.rect.x += image_pos[0]
             self.rect.y += image_pos[1]
        if event.type == MOUSEMOTION:
           if self.gripping:
              self.rect.width = event.pos[0]-self.rect.x
              self.rect.height = event.pos[1]-self.rect.y

    def capture_sprite(self, image):
        
        capturing_rect = Rect([0, 0, 0, 0])
        alpha_color = image.get_at(self.rect.topleft)
        other_color = False
        
        old_x = self.rect.x + self.rect.width
        for y in range(self.rect.y, self.rect.y + self.rect.height, 1):
            for x in range(self.rect.x, self.rect.x + self.rect.width, 1):
                if image.get_at((x,y)) != alpha_color:
                   other_color = True
                   if x < old_x:
                      old_x = x
                      capturing_rect.x = x
                      break
                    
        if other_color:
           old_x = self.rect.x
           for y in range(self.rect.y, self.rect.y + self.rect.height, 1):
               for x in range(self.rect.x + self.rect.width, self.rect.x-1, -1):
                   if image.get_at((x,y)) != alpha_color:
                      if x > old_x :
                         old_x = x 
                         if x > self.rect.x:
                            capturing_rect.width = (x+1) - capturing_rect.x
                         break
                        
           old_y = self.rect.y + self.rect.height             
           for x in range(self.rect.x, self.rect.x + self.rect.width, 1):
               for y in range(self.rect.y, self.rect.y + self.rect.height, 1):
                   if image.get_at((x,y)) != alpha_color:
                      if y < old_y:
                         old_y = y
                         capturing_rect.y = y
                         break
                        
           old_y = self.rect.y             
           for x in range(self.rect.x, self.rect.x + self.rect.width, 1):
               for y in range(self.rect.y + self.rect.height, self.rect.y-1, -1):
                   if image.get_at((x,y)) != alpha_color:
                      if y > old_y :
                         old_y = y 
                         if y > self.rect.y:
                            capturing_rect.height = (y+1) - capturing_rect.y
                         break
                        
           self.rect = capturing_rect
        #return other_color
    
    def reset_to_origin(self, image_pos):
        x = self.rect.x - image_pos[0]
        y = self.rect.y - image_pos[1]
        x = x / self.scale
        y = y / self.scale
        width = self.rect.width / self.scale
        height = self.rect.height / self.scale
        return Rect([x, y, width, height])

    def scale_rect(self, scale, image_pos):
        self.rect.x -= image_pos[0]
        self.rect.y -= image_pos[1]
        self.rect.x = self.rect.x/self.scale
        self.rect.y = self.rect.y/self.scale
        self.rect.width=self.rect.width/self.scale
        self.rect.height=self.rect.height/self.scale
        self.rect.x = self.rect.x*scale
        self.rect.y = self.rect.y*scale
        self.rect.width=self.rect.width*scale
        self.rect.height=self.rect.height*scale
        self.rect.x += image_pos[0]
        self.rect.y += image_pos[1]
        self.scale = scale

    def cycle_colors(self):
        self.timer += 1
        if self.timer >= self.color_max_time:
           self.timer = 0 
           self.color_index += self.increment
           if self.color_index >= self.colors_lenght:
              self.color_index = self.colors_lenght
              self.increment *= -1
           elif self.color_index <= 0:
              self.color_index = 0
              self.increment *= -1              
           self.color = self.colors[self.color_index]
        
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, self.line_thickness)


def main():
    
    pygame.init()

    #Open Pygame window
    screen = pygame.display.set_mode((640, 480),) #add RESIZABLE or FULLSCREEN
    #Title
    pygame.display.set_caption("Sprite Captor")
    #clock
    clock=pygame.time.Clock()
    #font
    font=pygame.font.SysFont('Arial', 30)

    #images
    original_image=pygame.image.load("image/flappy_bird_sheet_1.png").convert()
    image=original_image.copy()
    #variables
    image_pos=[0,0]
    image_original_move_speed = 5
    image_move_speed = image_original_move_speed
    scale=1
    scale_max=7
    sprite_captor=Sprite_Captor()
    sprites = []
    message = " "
    message_time = 0
    text=font.render(message, True, YELLOW)
    text_pos = [0,0]
       
    #pygame.key.set_repeat(400, 30)

    while True:
        #loop speed limitation
        #30 frames per second is enought
        clock.tick(30)
        
        for event in pygame.event.get():    #wait for events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #keyboard commands    
            if event.type == KEYDOWN:
                if event.key == K_i:
                   #scale up the image and the sprite captor 
                   if scale <  scale_max:
                      scale+=1
                   else:
                      scale = scale_max
                   image_move_speed = image_original_move_speed * scale
                   image = scale_image(original_image, scale)
                   sprite_captor.scale_rect(scale, image_pos)
                elif event.key == K_j:
                   #scale down the image and the sprite captor 
                   if scale >  1:
                      scale -= 1
                   else:
                      scale = 1
                   image_move_speed = image_original_move_speed * scale
                   image = scale_image(original_image, scale)
                   sprite_captor.scale_rect(scale, image_pos)
                elif event.key == K_o:
                    #reset the image's and the sprite captor's positions to origin
                    sprite_captor.rect.x-=image_pos[0]
                    sprite_captor.rect.y-=image_pos[1]
                    image_pos[0]=0
                    image_pos[1]=0
                elif event.key == K_r:
                    #reset the image's and the sprite captor's positions and sizes to origin
                    sprite_captor.rect = sprite_captor.reset_to_origin(image_pos)
                    sprite_captor.scale = 1
                    image_pos[0]=0
                    image_pos[1]=0
                    image = scale_image(original_image, 1)
                    scale = 1
                    image_move_speed = image_original_move_speed
                elif event.key == K_c:
                    #center the captured sprite
                    move_x = HALF_SCREEN_WIDTH-sprite_captor.rect.centerx
                    move_y = HALF_SCREEN_HEIGHT-sprite_captor.rect.centery
                    sprite_captor.rect.x += move_x
                    sprite_captor.rect.y += move_y
                    image_pos[0] += move_x
                    image_pos[1] += move_y
                elif event.key == K_e:
                    #add the captured sprite's position and size to the list
                    x, y, w, h = sprite_captor.reset_to_origin(image_pos)
                    sprites.append([x, y, w, h])
                    message = str(len(sprites))+" sprite added to the list"
                    message_time = 50
                    text=font.render(message, True, YELLOW)
                    text_pos[0] = HALF_SCREEN_WIDTH - int(text.get_width() / 2)
                    text_pos[1] = HALF_SCREEN_HEIGHT - int(text.get_height() / 2)
                elif event.key == K_s:
                    #enter the sprite editor
                    sprite_editor(screen, sprites, original_image)
                    message = "Sprite Captor"
                    text=font.render(message, True, YELLOW)
                    text_pos[0] = HALF_SCREEN_WIDTH - int(text.get_width() / 2)
                    text_pos[1] = HALF_SCREEN_HEIGHT - int(text.get_height() / 2)
                    message_time = 50
                    

            #update the sprite captor        
            sprite_captor.update(event, image, image_pos)
        sprite_captor.cycle_colors()  

                   
        #move the image and the sprite captor
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
           image_pos[1]-=image_move_speed
           sprite_captor.rect.y-=image_move_speed
        elif keys[K_DOWN]:
           image_pos[1]+=image_move_speed
           sprite_captor.rect.y+=image_move_speed
        if keys[K_LEFT]:
           image_pos[0]-=image_move_speed
           sprite_captor.rect.x-=image_move_speed
        elif keys[K_RIGHT]:
           image_pos[0]+=image_move_speed
           sprite_captor.rect.x+=image_move_speed


        #draw everything
        screen.fill(BLACK)
        screen.blit(image, image_pos)
        sprite_captor.draw(screen)
        if message_time > 0:
           message_time -= 1
           if message_time < 0:
              message_time = 0
           text=font.render(message, True, YELLOW)
           screen.blit(text, text_pos)           
        pygame.display.flip()

if __name__ == "__main__":
    main()
