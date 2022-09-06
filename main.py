from random import randint
import pygame as pg

DIM = [1000, 700]
FPS = 60
vec = pg.Vector2

class Player():
    def __init__(self) -> None:
        self.pos = vec(pg.mouse.get_pos())
        self.rays = [Ray(i) for i in range(0, 360)]
        pass

    def update(self):
        self.pos = vec(pg.mouse.get_pos())
        pass


class Ray():
    def __init__(self, angle) -> None:
        self.angle = angle

        pass

    def update(self):
        
        pass

class Boundary():
    def __init__(self, start:tuple, end:tuple) -> None:
        self.start = vec(start)
        self.end = vec(end)
        pass


def genBoundaries(n):
    return [Boundary((randint(0, DIM[0]), randint(0, DIM[1])), (randint(0, DIM[0]), randint(0, DIM[1]))) for i in range(n)]


if __name__ == '__main__':
    pg.init()
    disp = pg.display.set_mode(DIM)
    clock = pg.time.Clock()
    bounds = genBoundaries(1)

    running = 1
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = 0
            if event.type == pg.MOUSEBUTTONUP:
                bounds = genBoundaries(5)
        disp.fill((0,0,0))

        for b in bounds:
            pg.draw.line(disp, (255,255,255), b.start, b.end)

        


        pg.display.update()
        clock.tick(FPS)