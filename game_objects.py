import pygame as pg
import random
import spritemanagement
import random

class Pipe(pg.sprite.Sprite):
    def __init__(self, game, image):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.pipe_image_up = game.sheet.get_image_of('pipe_up')
        self.pipe_image_down = game.sheet.get_image_of('pipe_down')

        self.rect = self.image.get_rect()

        
        
class PipeSet(pg.sprite.Group):
    def __init__(self, game):
        super().__init__()
        
        random_position = random.randint(100, -100)
        pipe_up.rect.y = 0 + random_position
        pipe_down.rect.y = pipe_up.rect.y + 697

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
