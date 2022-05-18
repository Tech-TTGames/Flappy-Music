import pygame as pg

class Pipe(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = pg.image.load("sprites/pipe.bmp")
        self.rect = self.image.get_rect()

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