# coding: utf-8

import pygame as pg
from solar_draw import *
from solar_physics import *
from solar_IO import *

pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

SCREEN_SIZE = (800, 600)

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

time_step = None
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []
"""Список космических объектов."""


class Manager():

    def __init__(self):
        pass

        
    def process(self, events, screen):
        done = self.handle_events(events)
        return done
             
    def draw(self, screen):
        pass
        
    def move(self):
        pass
    
    def handle_events(self, events):
        done = False
        for event in events:
            if event.type == pg.QUIT:
                done = True
        return done

        
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption("Solar")

done = False
clock = pg.time.Clock()

mgr = Manager()

while not done:
    clock.tick(20)

    done = mgr.process(pg.event.get(), screen)

    pg.display.flip()



pg.quit()
