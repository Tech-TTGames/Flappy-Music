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
            if len(self.sprites()) == 1:
                self.add(self.crow)
            self.crow.update(crown_no[0])
    
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
        self.sheet = game.sheet
        self.image_def = game.sheet.get_image_of('crown',3)
        self.image = self.image_def.copy()
        self.rect = self.image.get_rect()
        self.rect.x = 25
        self.rect.y = 25

    def update(self,crowns):
        self.image = self.image_def.copy()
        no = self.sheet.get_image_of(f's{crowns}',3)
        no_rect = no.get_rect()
        no_rect.center = (self.rect.w/2,self.rect.h/2)
        self.image.blit(no,no_rect)

class Number(pg.sprite.Sprite):
    def __init__(self,game,score):
        super().__init__()
        self.image = pg.Surface((36,55), pg.SRCALPHA, 32).convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()
        self.rect.x = self.screen_rect.w/2-self.rect.w/2
        self.rect.y = 50
        self.sheet = game.sheet
        self.update(score)

    def update(self,score):
        self.image = pg.Surface((len(score)*36+6,55), pg.SRCALPHA, 32).convert_alpha()
        for no in range(len(score)):
            self.image.blit(self.sheet.get_image_of(score[no],3),(39*no,1))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.w/2-self.rect.w/2

class MenuOverlay:
    def __init__(self,game):
        self.game = game
        self.screen = self.game.screen
        self.screen_rect = self.screen.get_rect()
        self.sheet = self.game.sheet
        self.tap_img = self.sheet.get_image_of('tap',3)
        self.tap_rect =self.tap_img.get_rect()
        self.title = self.sheet.get_image_of('flappy',3)
        self.title_rect = self.title.get_rect()
        self.score_result = self.sheet.get_image_of('score',3)
        self.score_rect = self.score_result.get_rect()
    
    def gen_menu(self,type):
        if type == 'menu':
            self.title = self.sheet.get_image_of('ready',3)

        elif type == 'dead':
            self.title = self.sheet.get_image_of('over',3)
            self.score_result = self.sheet.get_image_of('score',3)
            self.score_rect = self.score_result.get_rect()
            score = [int(a) for a in str(self.game.score.score)]
            best_score = [int(a) for a in str(self.game.best[1])]
            no_surf = pg.Surface((len(score)*24,21), pg.SRCALPHA, 32).convert_alpha()
            for no in range(len(score)):
                no_surf.blit(self.sheet.get_image_of(f's{score[no]}',3),(24*no,0))
            no_surf.convert_alpha()
            no_rect = no_surf.get_rect()
            no_rect.topright = (120,57)
            self.score_result.blit(no_surf,no_rect)
            if self.game.best[0]:
                self.score_result.blit(self.sheet.get_image_of('new',3),(12,87))
            else:
                no_surf = pg.Surface((len(best_score)*24,21), pg.SRCALPHA, 32).convert_alpha()
                for no in range(len(best_score)):
                    no_surf.blit(self.sheet.get_image_of(f's{best_score[no]}',3),(24*no,0))
                no_surf.convert_alpha()
            no_rect = no_surf.get_rect()
            no_rect.topright = (120,123)
            self.score_result.blit(no_surf,no_rect)

        else:
            self.title = self.sheet.get_image_of('flappy',3)
        self.title_rect = self.title.get_rect()


    def draw_menu(self,type):
        self.screen.blit(self.title,(self.screen_rect.w/2-self.title_rect.w/2,150))
        self.screen.blit(self.tap_img,(self.screen_rect.w/2-self.tap_rect.w/2,self.screen_rect.h/2+100))
        if type == 'dead':
            self.screen.blit(self.score_result,(self.screen_rect.w/2-self.score_rect.w/2,self.screen_rect.h/2-self.score_rect.h/2))

if __name__ == "__main__":
    from main_game import MusiBirb
    MusiInstance = MusiBirb()
    MusiInstance.run_game()
