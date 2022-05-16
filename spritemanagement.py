import pygame as pg

class SpriteSheet:

    def __init__(self, filename):
        self.images = {
            'bg':(3,0,144,256)
        } #FILL IN WITH COORDINATES TO TEXTURE NAMES!
        try:
            self.sheet = pg.image.load(filename).convert()
        except:
            raise Exception(f'Could not load texture file: {filename}!')
    
    def get_image_at(self,rectangle,colorkey = None):
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert()
        image.blit(self.sheet, (0,0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pg.RLEACCEL)
        return image
    
    def get_image_of(self,name):
        rect = self.images[name]
        return self.get_image_at(rect)