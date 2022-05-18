import pygame as pg
import random
import spritemanagement

class Pipe(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.pipe_image_up = game.sheet.get_image_of('pipe_up')
        self.pipe_image_down = game.sheet.get_image_of('pipe_down')

        self.rect = self.image.get_rect()


        self.offset = self.settings['screen-height']/3
        y2 = self.offset + random.randrange(0, int(['screen-height'] - self.images['floor'].self.screen.get_rect() - 1.2 * self.offset))

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

