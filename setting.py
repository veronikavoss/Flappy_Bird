#%%
import os
#%%
title='Flappy Bird'
screen_size=screen_width,screen_height=432,768

background_size=background_w,background_h=144,256
ground_size=ground_w,ground_h=168,56

FPS=60
#%%
current_path=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(current_path,'image')
sound_path=os.path.join(current_path,'sound')