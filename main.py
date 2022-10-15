# from object import Object
from blocks import *
from camera import Camera
from settings import *
from mapinclude import load_map
import pygame as pg


class Main:
    def __init__(self):
        pg.init()
        pg.display.set_caption(CAPTION)
        self.clk = pg.time.Clock()
        self.scr = pg.display.set_mode((WIDTH, HEIGHT), vsync=VSYNC)
        self.running = True
        self.objects = []
        startpos, self.map = load_map("maps/map.cfg")
        self.cam = Camera(startpos[0] * BLOCK_SIZE,
                          startpos[1] * BLOCK_SIZE)

    def input(self, fps):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        self.cam.input(pg.key.get_pressed(), fps, self.objects)

    def update(self):
        pass
        # for object in self.objects:
        #     object.update()

    def output(self):
        self.scr.fill(BLACK)
        self.cam.draw(self.scr, self.objects)
        pg.display.flip()

    def start(self):
        self.prework()
        self.work()

    def prework(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] in block_types:
                    exec(f"""
self.objects.append({self.map[y][x]}(x=x * BLOCK_SIZE,
                                     y=y * BLOCK_SIZE,));
""")
                # if self.map[y][x] == '#':
                #     self.objects.append(Object(x=x * BLOCK_SIZE,
                #                                y=y * BLOCK_SIZE,
                #                                image_path="img/brick.bmp"))

    def work(self):

        while self.running:
            self.clk.tick(FPS)
            fps = self.clk.get_fps()
            pg.display.set_caption(f"FPS: {int(fps)} \
PL_X: {self.cam.xpos} \
PL_Y: {self.cam.ypos}")
            self.input(fps)
            self.update()
            self.output()


def main():
    game = Main()
    game.start()


if __name__ == '__main__':
    main()
