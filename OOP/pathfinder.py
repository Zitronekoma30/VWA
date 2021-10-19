import pygame as pg
import numpy as np
from enum import Enum


pg.init()

class NodeType(Enum):
    EMPTY = 0
    OBSTACLE = 1
    START = 2
    END = 3

class Node:
    def __init__(self, position, grid_size, type):
        self. position = position
        self.grid_size = grid_size
        self.type = type

        self.change_type(type)

        self.distance = 0
        self.rect = pg.Rect(position[0]*grid_size, position[1]*grid_size, grid_size-1, grid_size-1)
    
    def change_type(self, type):
        if type == NodeType.START:
            self.color = (0, 0, 255)
        elif type == NodeType.END:
            self.color = (0, 255, 0)
        elif type == NodeType.EMPTY:
            self.color = (255, 255, 255)
        elif type == NodeType.OBSTACLE:
            self.color = (0, 0, 0)
        else:
            print("Invalid NodeType")
        
        self.type = type

class Main:
    def __init__(self, grid_size, screen_size, caption, run):
        self.grid_size = grid_size
        self.screen_size = screen_size
        self.caption = caption
        self.run = run  

        self.clock = pg.time.Clock()


        self.screen = pg.display.set_mode([screen_size[0]*grid_size, screen_size[1]*grid_size])
        self.start_node_pos = [5, 5]
        self.end_node_pos = [18, 18]
        self.nodes = []
        pg.display.set_caption(caption)

    def grid_to_real(self, position):
        return [position[0]*self.grid_size, position[1]*self.grid_size]

    def create_rect(self, position):
        return pg.Rect(position[0]*self.grid_size, position[1]*self.grid_size, self.grid_size-1, self.grid_size-1)
    
    def create_large_point(self, position):
        return (position[0]*self.grid_size, position[1]*self.grid_size)
    
    def create_small_point(self, position):
        return [np.floor(position[0]/self.grid_size), np.floor(position[1]/self.grid_size)]


    def set_start(self, position):
        for node in self.nodes:
            if node.rect.collidepoint(self.grid_to_real(position)):
                node.change_type(NodeType.START)
                node.distance = 0
                self.start_node = node

    def set_end(self, position):
        for node in self.nodes:
            if node.rect.collidepoint(self.grid_to_real(position)):
                node.change_type(NodeType.END)
                self.end_node = node
                

    def create_nodes(self):
        for x in range(self.screen_size[0]):
            for y in range(self.screen_size[1]):
                self.nodes.append(Node([x, y], self.grid_size, NodeType.EMPTY))

        self.set_start(self.start_node_pos)
        self.set_end(self.end_node_pos)

    def find_distance(self):
        directions  = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        closed_nodes = []
        closed_nodes.append(self.start_node)
        print(len(closed_nodes))
        
        for closed_node in closed_nodes:
            for node in self.nodes:
                for direction in directions:
                    if node.rect.colliderect(self.create_rect([closed_node.position[0]+direction[0], closed_node.position[1]+direction[1]])):
                        if closed_nodes.count(node) == 0 and node.type != NodeType.OBSTACLE:
                            #print("foundone")
                            closed_nodes.append(node)
                            node.distance = closed_node.distance+1
                            node.color=[255, 255-node.distance*5, 255-node.distance*5]

            print("{} out of {}".format(len(closed_nodes), len(self.nodes)))

        closed_nodes[0].color=(0,0,255)
        closed_nodes[closed_nodes.index(self.end_node)].color = (0, 255, 0)





    def run_main_loop(self):
        '''starts the main loop, handles rendering as well as the logic'''
        delta_time = self.clock.tick(120)
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False

            mouse_x, mouse_y = pg.mouse.get_pos()

            if pg.mouse.get_pressed()[0]:
                #print(self.create_small_point((mouse_x, mouse_y)))
                for node in self.nodes:
                    if node.position == self.create_small_point((mouse_x, mouse_y)):
                        node.change_type(NodeType.OBSTACLE)
            
            if pg.mouse.get_pressed()[1]:
                self.find_distance()

            if pg.mouse.get_pressed()[2]:
                pass

            self.screen.fill((0, 0, 0))

                #set up in loop variables
            mouse_x, mouse_y = pg.mouse.get_pos()

            for node in self.nodes:
                pg.draw.rect(self.screen, node.color, node.rect)

            pg.display.update()
        
        pg.quit()

main = Main(16, [20, 20], "Pathfinding", True)

main.create_nodes()
main.run_main_loop()
