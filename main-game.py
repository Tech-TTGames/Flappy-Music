import pygame as pg
from spritemanagement import SpriteSheet
import game_objects
import json

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

        self.sheet = SpriteSheet('sprites/FlappyBirdSprites.png')
        self.bg_img = self.sheet.get_image_of('bg')
        self.bg_img = pg.transform.scale(self.bg_img,self.resolution)
        self.bg_offset = 0
    
    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
    
    def _render_background(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.bg_img,(self.bg_offset,0))
        self.screen.blit(self.bg_img,(self.resolution[0]+self.bg_offset,0))
        if self.bg_offset <=-self.resolution[0]:
            self.screen.blit(self.bg_img,(self.resolution[0]+self.bg_offset,0))
            self.bg_offset = 0
        self.bg_offset-=0.05

    def run_game(self):
        self.running = True
        while self.running:
            self._check_events()
            self._render_background()
            pg.display.update()
        pg.quit()

if __name__ == "__main__":
    MusiInstance = MusiBirb()
    MusiInstance.run_game()