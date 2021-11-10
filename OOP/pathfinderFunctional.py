import pygame as pg
import numpy as np
from enum import Enum
from operator import attrgetter

pg.init()

GRID_SIZE = 16
SCREEN_SIZE = [20, 20]
TITLE = "Pathfinding"



def render(grid_size, screen, nodes, clock):
    '''renders the map'''
    dt = clock.tick(120) # delta time
    while True:
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    quit()

        mouse_x, mouse_y = pg.mouse.get_pos()

        if pg.mouse.get_pressed()[1]:
            #find_distance()
            #find_path()
            pass

        screen.fill((0, 0, 0))

        for row in nodes:
            for node in row:
                pg.draw.rect(screen, node.get("color"), node.get("rect"))

        pg.display.update()

def set_up_nodes(grid_size, screen_size):
    #nodes design
    # [
    # [{}, {}, {}, {}],
    # [{}, {}, {}, {}],
    # [{}, {}, {}, {}],
    # [{}, {}, {}, {}],
    # [{}, {}, {}, {}]
    # ]
    nodes = []
    for y in range(screen_size[1]):
        row = []
        for x in range(screen_size[0]):
            row.append({"color": (255, 255, 255),
            "type":"floor", 
            "rect": pg.Rect(y*grid_size, x*grid_size, grid_size-1, grid_size-1),
            "distance": 0})
        nodes.append(row)
    return nodes




def start_pathdinding(grid_size, screen_size, caption):
    '''launches all other functions in their respective order and sets up some values for them'''
    clock = pg.time.Clock()
    screen = pg.display.set_mode([screen_size[0]*grid_size, screen_size[1]*grid_size])
    start_node_pos = [5, 5]
    end_node_pos = [18, 18]
    pg.display.set_caption(caption)

    render(grid_size, screen, set_up_nodes(grid_size, screen_size), clock)

    
start_pathdinding(GRID_SIZE, SCREEN_SIZE, TITLE)
