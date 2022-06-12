import pygame as pg

class SpriteSheet:

    def __init__(self, game, filename):
        self.resolution = game.resolution
        self.images = {
            'bg':(3,0,144,256),
            'pipe_up':(152,3,26,160),
            'pipe_down':(180,3,26,160),
            'floor':(215,10,167,55),
            'birb_1':(381,187,17,12),
            'birb_2':(381,213,17,12),
            'birb_3':(381,239,17,12),
            'crown':(251,122,21,9),
            'ready':(254,71,92,25),
            'over':(152,173,96,21),
            'tap':(370,73,57,19),
            'flappy':(152,200,89,24),

            0:(254,98,12,18),
            1:(236,80,12,18),
            2:(325,148,12,18),
            3:(339,148,12,18),
            4:(353,148,12,18),
            5:(367,148,12,18),
            6:(325,172,12,18),
            7:(339,172,12,18),
            8:(353,172,12,18),
            9:(367,172,12,18),

        } #FILL IN WITH COORDINATES TO TEXTURE NAMES!
        try:
            self.sheet = pg.image.load(filename).convert_alpha()
        except:
            raise Exception(f'Could not load texture file: {filename}!')
    
    def get_image_at(self,rectangle,adjust,colorkey = None):
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size).convert_alpha()
        image.blit(self.sheet, (0,0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pg.RLEACCEL)
        if adjust == 'R':
            temp_res = ((rect.w*2)*1.66,rect.h*2)
        elif adjust == 3:
            temp_res = (rect.w*3,rect.h*3)
        else:
            temp_res = (rect.w*2,rect.h*2)
        return pg.transform.scale(image,temp_res).convert_alpha()
    
    def get_image_of(self,name,adjust = 'R'):
        rect = self.images[name]
        return self.get_image_at(rect,adjust,(0,0,0))