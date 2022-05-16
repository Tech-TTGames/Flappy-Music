import pygame as pg
from spritemanagement import SpriteSheet
import game_objects
import json

class MusiBirb:
    def __init__(self):
        with open('config.json') as config_file:
            self.settings = json.load(config_file)
        self.clock = pg.time.Clock()
        pg.init()
        pg.display.set_caption("Flappy Music!")
        
        resolution = (self.settings["screen-height"],self.settings["screen-width"])
        self.screen = pg.display.set_mode(resolution)
        bg_img = SpriteSheet.get_image_of('bg')
        self.birb = game_objects.Birb()