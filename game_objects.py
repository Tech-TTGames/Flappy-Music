import pygame as pg
import random

class Pipe(pg.sprite.Sprite):
    def __init__(self, game, rectoffset, Rotation,x):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()
        if Rotation:
            self.image = game.sheet.get_image_of('pipe_down')
            self.rect = self.image.get_rect()
            self.rect.y = rectoffset + self.rect.h - self.rect.h/2
        else:
            self.image = game.sheet.get_image_of('pipe_up')
            self.rect = self.image.get_rect()
            self.rect.y = rectoffset - self.rect.h/2

        
        self.rect.x = x
        
    
    def update(self):
        self.rect.x -= 0.1*self.settings["scroll-speed"]
        if self.rect.right < self.screen_rect.left:
            self.kill()

        
        
class PipeSet(pg.sprite.Group):
    def __init__(self, game,x):
        super().__init__()
        self.settings = game.settings
        self.game = game

        self.generate(x)
    
    def generate(self,x):
        random_position = random.randint(110,260)
        pipe_up_y_rect = random_position - 150
        pipe_down_y_rect = pipe_up_y_rect + 150
        self.add(Pipe(self.game,pipe_up_y_rect,False,x))
        self.add(Pipe(self.game,pipe_down_y_rect,True,x))

class Birb(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.images = []
        self.index = 0
        self.counter = 0
        self.jumping_state = 0
        self.vel = self.settings['birb-velocity']
        self.clicked = False

        for num in range(1,4):
            image = game.sheet.get_image_of(f'birb_{num}',3)
            self.images.append(image)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.w / 2
        self.rect.y = self.screen_rect.h / 2
            
    def update(self):
        
        #gravity
        if self.settings['flying'] == 1:
            self.vel += 0.5
            if self.vel > 7:
                self.vel = 7
            if self.rect.bottom < 581:
                self.rect.y += int(self.vel)

        #jumping
        if pg.key.get_pressed()[pg.K_SPACE] == 1 or pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            self.vel = -9
        
        if pg.key.get_pressed()[pg.K_SPACE] == 0 or pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        #animation
        self.counter += 1
        flap_cooldown = 20

        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

            self.image = self.images[self.index]
        
        #rotate the birb
        self.image = pg.transform.rotate(self.images[self.index], self.vel * -2)
        
    # def jump(self):
        

    def render(self):
        self.screen.blit(self.image,self.rect)

class Floor(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.image = game.sheet.get_image_of('floor')
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x -= 0.1*self.settings["scroll-speed"]
        if self.rect.right <= self.screen_rect.left:
            self.rect.x += self.rect.w*2
