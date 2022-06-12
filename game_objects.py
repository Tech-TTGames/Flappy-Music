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
        p1, p2 = Pipe(self.game,pipe_up_y_rect,False,x), Pipe(self.game,pipe_down_y_rect,True,x)
        self.add(p1)
        self.add(p2)
        self.game.collsprites.add(self)
        self.point_torch = True
    
    def update(self):
        super().update()
        if self.point_torch and self.sprites()[0].rect.x < self.settings["screen-width"]/2:
            self.game.score.up_score()
            self.point_torch = False
    
    def reset(self,x):
        for sprite in self.sprites():
            sprite.kill()
        self.point_torch = True
        self.generate(x)



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
        self.grav = False

        for num in range(1,4):
            image = game.sheet.get_image_of(f'birb_{num}',3)
            self.images.append(image)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.w / 2
        self.rect.centery = self.screen_rect.h / 2
            
    def update(self):
        
        #gravity
        if self.grav:
            if self.vel < 7:
                self.vel += 0.1
            if self.rect.top < 0:
                self.vel += 1
            self.rect.y += int(self.vel)
        
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
        
    def jump(self):
        self.vel = -4.5
        
    def render(self):
        self.screen.blit(self.image,self.rect)
    
    def reset(self):
        self.index = 0
        self.counter = 0
        self.jumping_state = 0
        self.vel = self.settings['birb-velocity']
        self.grav = False
        self.rect.centerx = self.screen_rect.w / 2
        self.rect.centery = self.screen_rect.h / 2


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
