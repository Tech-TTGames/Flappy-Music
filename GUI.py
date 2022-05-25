import pygame as pg

class ScoreCounter():
    def __init__(self,game):
        self.screen = game.screen
        self.screen.rect = self.screen.get_rect()
        self.settings = game.settings

