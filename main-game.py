import pygame as pg
from spritemanagement import SpriteSheet
from GUI import ScoreCounter
import game_objects
import json
from pygame.locals import *

class MusiBirb:
    def __init__(self):
        with open('settings.json') as config_file:
            self.settings = json.load(config_file)
        self.clock = pg.time.Clock()
        pg.init()
        pg.display.set_caption("Flappy Music!")
        self.resolution = (self.settings["screen-width"],self.settings["screen-height"])
        self.screen = pg.display.set_mode(self.resolution)
        self.running = False

        self.sheet = SpriteSheet(self,'sprites/FlappyBirdSprites.png')
        self.bg_img = self.sheet.get_image_of('bg')
        self.bg_img = pg.transform.scale(self.bg_img,self.resolution)
        self.bg_offset = 0
        self.birb = game_objects.Birb(self)
        self.floors = pg.sprite.Group()
        self._init_floor()
        self.pipes = []
        self._init_pipes()
        self.score = ScoreCounter(self)

        #TEST ZONE
    
    def _render_background(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg_img,(self.bg_offset,0))
        self.screen.blit(self.bg_img,(self.resolution[0]+self.bg_offset,0))
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
        floor = game_objects.Floor(self)
        floor.rect.y = screen_rect.bottom - floor.rect.h
        floor.rect.x = screen_rect.left + floor.rect.w
        self.floors.add(floor)
    
    def _init_pipes(self):
        for pid in range(self.settings["pipegen-length"]):
            x = 200 + pid*252
            pipe_set = game_objects.PipeSet(self,x)
            self.pipes.append(pipe_set)
    
    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.type == pg.K_SPACE and self.settings['flying'] == 0:
                    self.settings['flying'] = 1
            elif event.type == pg.MOUSEBUTTONDOWN and self.settings['flying'] == 0:
                self.settings['flying'] = 1


            # elif event.type == pg.KEYDOWN:
            #     if event.key == pg.K_SPACE and not self.birb.jumping:
            #         self.birb.jump()
    
    def _update_sprites(self):
        self.birb.update()
        self.floors.update()
        self.score.update_score()
        for set in range(len(self.pipes)):
            self.pipes[set].update()
            if not self.pipes[set]:
                self.pipes[set].generate(self.settings["pipegen-length"]*252-26)

    
    def _draw_sprites(self):
        for set in self.pipes:
            set.draw(self.screen)
        self.score.draw(self.screen)
        self.birb.render()
        self.floors.draw(self.screen) #This HAS to be last.

    def run_game(self):
        self.running = True
        while self.running:
            self._render_background()
            self._check_events()
            self._update_sprites()
            self._draw_sprites()
            pg.display.update()
            self.clock.tick(120)
        pg.quit()

if __name__ == "__main__":
    MusiInstance = MusiBirb()
    MusiInstance.run_game()