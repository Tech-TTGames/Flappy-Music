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
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = pg.image.load("sprites/birb.bmp")
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.jumping = False
    
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
