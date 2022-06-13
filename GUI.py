import pygame as pg

class ScoreCounter(pg.sprite.Group):
    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.game = game
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.score = 0

        self.init_score()
    
    def init_score(self):
        self.no = Number(self.game,[0])
        self.crow = Crown(self.game)
        self.add(self.no)
        self.update_score()
    
    def update_score(self):
        score_digits = [int(a) for a in str(self.score)]
        clean_score = score_digits[-3:]
        crown_no = score_digits[:-3]
        self.no.update(clean_score)
        if crown_no:
            self.add(self.crow)
            self.crow.update(crown_no)
    
    def up_score(self):
        self.score += 1
        self.update_score()
    
    def clear(self):
        self.score = 0
        for sprite in self.sprites():
            sprite.kill()
        self.init_score()

class Crown(pg.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.image = game.sheet.get_image_of('crown')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0        

class Number(pg.sprite.Sprite):
    def __init__(self,game,score):
        super().__init__()
        self.image = pg.Surface((40,36), pg.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()
        self.rect.x = self.screen_rect.w/2-self.rect.w/2
        self.rect.y = 10
        self.sheet = game.sheet
        self.update(score)

    def update(self,score):
        self.image = pg.Surface((len(score)*40,36), pg.SRCALPHA, 32).convert_alpha()
        for no in range(len(score)):
            self.image.blit(self.sheet.get_image_of(score[no]),(40*no,1))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.w/2-self.rect.w/2

class MenuOverlay:
    def __init__(self,game):
        self.game = game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()
        self.sheet = self.game.sheet
    
    def draw_menu(self,type):
        if type == 'menu':
            title = self.sheet.get_image_of('ready',3)
        elif type == 'dead':
            title = self.sheet.get_image_of('over',3)
        else:
            title = self.sheet.get_image_of('flappy',3)
        tap = self.sheet.get_image_of('tap',3)
        title_rect = title.get_rect()
        tap_rect = tap.get_rect()
        self.screen.blit(title,(self.screen_rect.w/2-title_rect.w/2,150))
        self.screen.blit(tap,(self.screen_rect.w/2-tap_rect.w/2,self.screen_rect.h/2+100))

