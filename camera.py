from settings import *
from collision import Hitbox, check_collision_first


class Camera():
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        # self.physbody = Hitbox(x=x, y=y, w=BLOCK_SIZE, h=BLOCK_SIZE)

    def input(self, keys, fps, objects):
        # fps += 0.00000001
        if fps < 1:
            fps = 1

        nearobjects = []
        amx = abs(self.xpos)
        amy = abs(self.ypos)

        for object in objects:
            aox = abs(object.physbody.x)
            aoy = abs(object.physbody.x)
            if object.has_collision and \
               max(aox, amx) - min(aox, amx) < BLOCK_SIZE * 1.5 and \
               max(aoy, amy) - min(aoy, amy) < BLOCK_SIZE * 1.5:
                nearobjects.append(object)

        old_x = self.xpos
        old_y = self.ypos

        if keys[KEY_UP]:
            self.ypos -= int(PL_SPEED / fps)
        if keys[KEY_DOWN]:
            self.ypos += int(PL_SPEED / fps)
        if keys[KEY_LEFT]:
            self.xpos -= int(PL_SPEED / fps)
        if keys[KEY_RIGHT]:
            self.xpos += int(PL_SPEED / fps)

        if check_collision_first(Hitbox(self.xpos, self.ypos, 1, 1),
                                 [object.physbody for object in nearobjects]):
            self.xpos = old_x
            self.ypos = old_y

    def draw(self, surface, objects):
        offset_x = self.xpos - HALF_WIDTH
        offset_y = self.ypos - HALF_HEIGHT
        for object in objects:
            surface.blit(object.image,
                         (object.bounds.x - offset_x,
                          object.bounds.y - offset_y))
