import pygame as pg
import random

class Pipe(pg.sprite.Sprite):
    def __init__(self, game, rectoffset, Rotation,x):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        if Rotation:
            self.image = game.sheet.get_image_of('pipe_down')
            self.rect = self.image.get_rect()
            self.rect.y = rectoffset + self.rect.h - self.rect.h/2
        else:
            self.image = game.sheet.get_image_of('pipe_up')
            self.rect = self.image.get_rect()
            self.rect.y = rectoffset - self.rect.h/2

        
        self.rect.x = x
        
    
    def update(self):
        self.rect.x -= 0.1*self.settings["scroll-speed"]
        if self.rect.right < self.screen_rect.left:
            self.kill()

        
        
class PipeSet(pg.sprite.Group):
    def __init__(self, game,x):
        super().__init__()
        self.settings = game.settings
        self.game = game

        self.generate(x)
    
    def generate(self,x):
        random_position = random.randint(110,260)
        pipe_up_y_rect = random_position - 110
        pipe_down_y_rect = pipe_up_y_rect + 110
        self.add(Pipe(self.game,pipe_up_y_rect,False,x))
        self.add(Pipe(self.game,pipe_down_y_rect,True,x))

class Birb(pg.sprite.Sprite):
    def __init__(self, x, y, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        self.screen_height = self.settings["screen-height"]

        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1,4):
            image = game.sheet.get_image_of(f'birb_{num}')
            self.images.append(image)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.jumping = False
        flappy = Birb(self.settings["birb-position-x"], self.screen_height / 2)
        birb_group = pg.sprite.Group()
        birb_group.add(flappy)

    
    
    

        
            
    def update(self):

        #handle the animation
        self.counter += 1
        flap_cooldown = 5

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        
    
    def jump(self):
        
        
        
        
        
        
        
        pass #IMPLEMENT JUMP

class Floor(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = game.sheet.get_image_of('floor')
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x -= 0.1*self.settings["scroll-speed"]
        if self.rect.right <= self.screen_rect.left:
            self.rect.x += self.rect.w*2
