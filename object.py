from settings import *
from pygame.rect import Rect
from collision import Hitbox
import pygame as pg


class Object:
    def __init__(self,
                 x, y,
                 image_path="img/brick.bmp",
                 speed=(0, 0),
                 has_texture=True):
        self.image = \
            pg.image.load(image_path)
        self.image = \
            pg.transform.scale(self.image,
                               (BLOCK_SIZE,
                                BLOCK_SIZE))

        self.bounds = self.image.get_rect()
        self.bounds = Rect(x,
                           y,
                           *self.image.get_rect().size)
        self.speed = speed
        self.has_texture = has_texture
        self.physbody = Hitbox(x=x, y=y, w=BLOCK_SIZE, h=BLOCK_SIZE)

    @property
    def left(self):
        return self.bounds.left

    @property
    def right(self):
        return self.bounds.right

    @property
    def top(self):
        return self.bounds.top

    @property
    def bottom(self):
        return self.bounds.bottom

    @property
    def width(self):
        return self.bounds.width

    @property
    def height(self):
        return self.bounds.height

    @property
    def center(self):
        return self.bounds.center

    @property
    def centerx(self):
        return self.bounds.centerx

    @property
    def centery(self):
        return self.bounds.centery

    def draw(self, surface):
        surface.blit(self.image, (self.bounds.x, self.bounds.y))

    def move(self, dx, dy):
        self.bounds = self.bounds.move(dx, dy)

    def update(self):
        pass
        # if self.speed == [0, 0]:
        #     return

        # self.move(*self.speed)


class Trigger(Object):
    def __init__(self,
                 x, y,
                 has_collision=False,
                 speed=(0, 0)):
        self.bounds = Rect(x,
                           y,
                           BLOCK_SIZE,
                           BLOCK_SIZE)
        self.speed = speed
        self.has_texture = False
        self.has_collision
        self.physbody = Hitbox(x=x, y=y, w=BLOCK_SIZE, h=BLOCK_SIZE)


class Block(Object):
    def __init__(self,
                 x, y,
                 image_path="img/brick.bmp",
                 has_collision=True,
                 speed=(0, 0)):
        self.image = \
            pg.image.load(image_path)
        self.image = \
            pg.transform.scale(self.image,
                               (BLOCK_SIZE,
                                BLOCK_SIZE))

        self.bounds = self.image.get_rect()
        self.bounds = Rect(x,
                           y,
                           *self.image.get_rect().size)
        self.speed = speed
        self.has_texture = True
        self.has_collision = has_collision
        self.physbody = Hitbox(x=x, y=y, w=BLOCK_SIZE, h=BLOCK_SIZE)
