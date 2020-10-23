import numpy as np
import pygame as pg
from random import randint, gauss

pg.init()
pg.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_SIZE = (800, 600)


class Gun():

    pass    
class Table():
    pass
    
class Ball():
    pass

class Manager():

    def __init__(self):
        self.gun = Gun()
        self.score_t = Table()
        
    def draw(self, screen):
        screen.fill(BLACK)
        
    def process(self, events, screen):
        done = self.handle_events(events)
        self.draw(screen)
        return done
        
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
        return done


        
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("The gun of Kolganov")

done = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(15)
    screen.fill(BLACK)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()


pg.quit()