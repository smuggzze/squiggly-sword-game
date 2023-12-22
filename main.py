import pygame as pg

from sword_handle_locator import sword_handle_locator

pg.init()

X = 600
Y = 400

screen = pg.display.set_mode((X, Y))

pg.display.set_caption("follow mouse test")

sword = pg.image.load("assets/sword_test.jpg")


while True:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            quit()

        mx, my = pg.mouse.get_pos()
        screen.fill((255, 255, 255))
        screen.blit(sword, (mx - (sword.get_width() / 2), my - (sword.get_height() - 15)))
        sx, sy = sword_handle_locator(sword, mx, my)
        pg.draw.line(screen, (0, 0, 0), (0, Y / 2), (sx, sy))
        pg.draw.line(screen, (0, 0, 0), (0, (Y / 2) + 20), (sx, sy + 5))

        pg.display.update()

