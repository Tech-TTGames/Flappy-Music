import pygame as pg

class ScoreCounter(pg.sprite.Group):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.screen.rect = self.screen.get_rect()
        self.settings = game.settings
        self.score = 0

        self.render_score()
    
    def rednder_score(self):
        score_digits = [int(a) for a in str(self.score)]

class Crown(pg.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.image = game.sheet.get_image('crown')
        self.rect = self.image.get_rect()

class Number(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
