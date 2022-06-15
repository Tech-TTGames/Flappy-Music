import pygame as pg
from sys import exit
from spritemanagement import SpriteSheet
from GUI import ScoreCounter, MenuOverlay
import game_objects
import json
from time import time

class MusiBirb:
    def __init__(self):
        with open('settings.json') as config_file:
            self.settings = json.load(config_file)
        self.clock = pg.time.Clock()
        pg.init()
        pg.display.set_caption("Flappy Music!")
        self.resolution = (self.settings["screen-width"],self.settings["screen-height"])
        self.screen = pg.display.set_mode(self.resolution)
        self.collsprites = pg.sprite.Group()

        self.sheet = SpriteSheet(self,'sprites/FlappyBirdSprites.png')
        pg.display.set_icon(self.sheet.get_image_of('birb_1',1))
        self.bg_img = self.sheet.get_image_of('bg')
        self.bg_img = pg.transform.scale(self.bg_img,self.resolution)
        self.bg_offset = 0
        self.floors = pg.sprite.Group()
        self._init_floor()
        self.overlay = MenuOverlay(self)
        self.initialize_field()
        self.state_change_time = time()
        self.best = (0,0)
        self.skip_death = True
        self.mode = False
    
    def _render_background(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg_img,(self.bg_offset,0))
        self.screen.blit(self.bg_img,(self.resolution[0]+self.bg_offset,0))
        if self.mode != 3:
            if self.bg_offset <=-self.resolution[0]:
                self.screen.blit(self.bg_img,(self.resolution[0]+self.bg_offset,0))
                self.bg_offset = 0
            self.bg_offset-=0.05*self.settings["scroll-speed"]
    
    def _init_floor(self):
        floor = game_objects.Floor(self)
        screen_rect = self.screen.get_rect()
        floor.rect.y = screen_rect.bottom - floor.rect.h
        floor.rect.x = screen_rect.left
        self.floors.add(floor)
        self.collsprites.add(floor)
        floor = game_objects.Floor(self)
        floor.rect.y = screen_rect.bottom - floor.rect.h
        floor.rect.x = screen_rect.left + floor.rect.w
        self.floors.add(floor)
        self.collsprites.add(floor)

    def _init_pipes(self):
        for pid in range(self.settings["pipegen-length"]):
            x = 440 + pid*252
            pipe_set = game_objects.PipeSet(self,x)
            self.pipes.append(pipe_set)
    
    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if self.mode == 2 and self.state_change_time < time()-0.5:
                if (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN):
                    self.birb.grav = True
                    self.birb.jump()
                    return True
            elif self.mode == 3 and self.state_change_time < time()-0.5:
                if (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN):
                    return True
            else:    
                if (event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN):
                    self.birb.jump()
    
    def _death_check(self):
        return pg.sprite.spritecollideany(self.birb,self.collsprites,collided=pg.sprite.collide_mask)
    
    def _update_sprites(self):
        if self.mode != 3:
            self.birb.update()
            self.floors.update()
        if self.mode != 2 and self.mode != 3:
            for set in range(len(self.pipes)):
                self.pipes[set].update()
                if not self.pipes[set]:
                    self.pipes[set].generate(self.settings["pipegen-length"]*252-26)

    
    def _draw_sprites(self):
        for set in self.pipes:
            set.draw(self.screen)
        if self.mode != 2 and self.mode != 3:
            self.score.draw(self.screen)
        self.floors.draw(self.screen)
        self.birb.render()

    def check_best(self):
        try:
            with open('data.sav','r') as f:
                try:
                    self.best = (False,int(f.readline()))
                except ValueError:
                    print('Save file corrupted!')
        except FileNotFoundError:
            pass
        finally:
            if self.score.score > self.best[1]:
                with open('data.sav','w') as f:
                    f.write(str(self.score.score))
                self.best = (True,self.score.score)

    def initialize_field(self):
        self.birb = game_objects.Birb(self)
        self.pipes = []
        self._init_pipes()
        self.score = ScoreCounter(self)
    
    def re_initialize(self):
        self.birb.reset()
        self.score.clear()
        for pid in range(self.settings["pipegen-length"]):
            x = 440 + pid*252
            self.pipes[pid].reset(x)

    def menu(self):
        self.state_change_time = time()
        self.mode = 2
        self.overlay.gen_menu()
        while True:
            self._render_background()
            if self._check_events():
                break
            self._update_sprites()
            self._draw_sprites()
            self.overlay.draw_menu()
            pg.display.update()
            self.clock.tick(120)

    def death_screen(self):
        if self.skip_death:
            self.skip_death = False
            return True
        self.state_change_time = time()
        self.mode = 3
        self.overlay.gen_menu()
        while True:
            self._render_background()
            if self._check_events():
                break
            self._update_sprites()
            self._draw_sprites()
            self.overlay.draw_menu()
            pg.display.update()
            self.clock.tick(120)
        self.re_initialize()
        return True
    
    def game_loop(self):
        self.mode = False
        while not self._death_check():
            self._render_background()
            self._check_events()
            self._update_sprites()
            self._draw_sprites()
            pg.display.update()
            self.clock.tick(120)

    def run_game(self):
        while self.death_screen():
            self.menu()
            self.game_loop()
            self.check_best()

if __name__ == "__main__":
    MusiInstance = MusiBirb()
    MusiInstance.run_game()
