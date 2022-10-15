from object import Block, Trigger
from settings import *
# from pygame.rect import Rect


block_types = []

block_types.append("Wall")
block_types.append("Win")


class Wall(Block):
    image = \
        pg.image.load("img/brick.bmp")
    image = \
        pg.transform.scale(image,
                           (BLOCK_SIZE,
                            BLOCK_SIZE))


class Space(Trigger):
    pass


class Win(Block):
    def __init__(self,
                 x, y,
                 speed=(0, 0)):
        Block.__init__(self, x, y,
                       image_path="img/win.bmp",
                       has_collision=False)
