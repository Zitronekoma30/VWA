import pygame as pg
import numpy as np


pg.init()

class Node:
    def __init__(self, position, grid_size, type):
        self. position = position
        self.grid_size = grid_size
        self.type = type

        if type == "s":
            self.color = (0,0,255)
        elif type == "e":
            self.color = (0,255,0)
        else:
            self.color = (255,255,255)

        self.distance = 0
        self.rect = pg.Rect(position[0]*grid_size, position[1]*grid_size, grid_size-1, grid_size-1)
    
    def change_type(self, type):
        if type == "s":
            self.color = (0, 0, 255)
        elif type == "e":
            self.color = (0, 255, 0)
        else:
            self.color = (255, 255, 255)
        
        self.type = type

class Main:
    def __init__(self, grid_size, screen_size, caption, run):
        self.grid_size = grid_size
        self.screen_size = screen_size
        self.caption = caption
        self.run = run  

        self.clock = pg.time.Clock()


        self.screen = pg.display.set_mode([screen_size[0]*grid_size, screen_size[1]*grid_size])
        self.start_node_pos = [2, 2]
        self.end_node_pos = [45, 45]
        self.nodes = []
        pg.display.set_caption(caption)

    def grid_to_real(self, position):
        return [position[0]*self.grid_size, position[1]*self.grid_size]


    def set_start(self, position):
        for node in self.nodes:
            if node.rect.collidepoint(self.grid_to_real(position)):
                node.change_type("s")
                self.start_node = node

    def set_end(self, position):
        for node in self.nodes:
            if node.rect.collidepoint(self.grid_to_real(position)):
                node.change_type("e")
                self.end_node = node
                

    def create_nodes(self):
        for x in range(self.screen_size[0]):
            for y in range(self.screen_size[1]):
                self.nodes.append(Node([x, y], self.grid_size, "g"))

        self.set_start(self.start_node_pos)
        self.set_end(self.end_node_pos)

    def find_distance(self):
        pass


    def run_main_loop(self):
        '''starts the main loop, handles rendering as well as the logic'''
        delta_time = self.clock.tick(120)
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

            self.screen.fill((0, 0, 0))

                #set up in loop variables
            mouse_x, mouse_y = pg.mouse.get_pos()

            for node in self.nodes:
                pg.draw.rect(self.screen, node.color, node.rect)



            pg.display.update()
        
        pg.quit()

main = Main(16, [50, 50], "Pathfinding", True)

main.create_nodes()
main.run_main_loop()
