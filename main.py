from copy import deepcopy
from math import cos, radians, sin
from random import randint
import pygame as pg

DIM = [1000, 700]
vec = pg.Vector2

FPS = 60
CIR_RES = 2
TURN_SPEED = 3
FOV = 70

class Player():
    def __init__(self) -> None:
        self.pos = vec(pg.mouse.get_pos())
        self.rot = 0
        self.rays = [Ray(self, radians(i/CIR_RES)) for i in range(0, int(FOV*CIR_RES))]
        pass

    def update(self):
        self.pos = vec(pg.mouse.get_pos())
        try:
            list(map(lambda x: x.update(), self.rays))
        except: pass

class Ray():
    def __init__(self, player, angle) -> None:
        self.angle = angle
        self.player = player
        self.epos = self.dir()*10
        
        pass

    def dir(self):
        return vec(cos(self.angle+self.player.rot), sin(self.angle+self.player.rot))
        
    def calcIntersect(self):
        results = []

        x3 = self.player.pos.x
        y3 = self.player.pos.y
        x4 = self.player.pos.x + self.dir().x
        y4 = self.player.pos.y + self.dir().y

        for w in bounds:
            x1 = w.start.x
            y1 = w.start.y
            x2 = w.end.x
            y2 = w.end.y

            den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
            if den == 0: continue

            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

            if t > 0 and t < 1 and u > 0:
                results.append(
                    vec(
                        x1 + t * (x2 - x1),
                        y1 + t * (y2 - y1)
                    )
                )
            else: pass

        results.sort(key = lambda x: ((x.x-self.player.pos.x)**2+(x.y-self.player.pos.y)**2)**0.5)

        return results[0]

    def update(self):
        self.epos = self.calcIntersect()
        pass


class Boundary():
    def __init__(self, start:tuple, end:tuple) -> None:
        self.start = vec(start)
        self.end = vec(end)
        pass


def genBoundaries(n, walls = True):
    ret= [Boundary((randint(0, DIM[0]), randint(0, DIM[1])), (randint(0, DIM[0]), randint(0, DIM[1]))) for i in range(n)]
    if walls:
        ret.append(Boundary((-1, -1), (0, DIM[1])))
        ret.append(Boundary((-1, -1), (DIM[0], -1)))
        ret.append(Boundary(DIM, (-1, DIM[1])))
        ret.append(Boundary(DIM, (DIM[0], -1)))
    return ret

if __name__ == '__main__':
    pg.init()
    disp = pg.display.set_mode(DIM)
    clock = pg.time.Clock()
    bounds = genBoundaries(1)
    player = Player()

    running = 1
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = 0
            if e.type == pg.MOUSEBUTTONDOWN:
                if e.button == 1:
                    bounds = genBoundaries(5)
                if e.button == 4:
                    player.rot-= radians(TURN_SPEED)
                if e.button == 5:
                    player.rot+= radians(TURN_SPEED)
            if e.type == pg.TEXTINPUT:
                if e.text == 'a':
                    player.rot-= radians(TURN_SPEED)
                elif e.text == 'd':
                    player.rot+= radians(TURN_SPEED)

            
        disp.fill((0,0,0))

        player.update()

        for r in player.rays:
            pg.draw.line(disp, (100,100,100), player.pos, r.epos)

        for b in bounds:
            pg.draw.line(disp, (255,255,255), b.start, b.end)

        pg.display.update()
        clock.tick(FPS)