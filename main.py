import pygame as pg


class Game():
    def __init__(self) -> None:
        pg.init()

        self.disp = pg.display.set_mode((600,600))

        self.mainloop()


    def mainloop(self):
        while True:
            self.disp.fill((100,100,100))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()

            pg.display.update()


    def quit(self):
        pg.quit()
        quit()



if __name__ == '__main__':
    Game()