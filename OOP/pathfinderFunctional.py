from os import close
import pygame as pg
import numpy as np
from enum import Enum
from operator import attrgetter


GRID_SIZE = 16
SCREEN_SIZE = (20, 20)
TITLE = "Pathfinding"

pg.init()



#Setup
def set_up_nodes(grid_size: int, screen_size: tuple) -> list:
    '''creates a list of lists of dicts representing a 2D grid of nodes'''
    #nodes design
    # [
    # [{}, {}, {}, {}],
    # [{}, {}, {}, {}],
    # [{}, {}, {}, {}],
    # [{}, {}, {}, {}],
    # [{}, {}, {}, {}]
    # ]
    # to get type of a node at position X5 Y2: nodes[2][5]["type"] or nodes[2][5].get("type")
    nodes = []
    for y in range(screen_size[1]):
        row = []
        for x in range(screen_size[0]):
            row.append({
            "color": (255, 255, 255),
            "position": (y, x),
            "type":"floor", 
            "rect": pg.Rect(y*grid_size, x*grid_size, grid_size-1, grid_size-1),
            "distance": 0
            })
        nodes.append(row)
        
    nodes = change_node_type(nodes, (2, 2), "start")
    nodes = change_node_type(nodes, (15, 15), "end")

    return nodes

def start_pathdinding(grid_size: int, screen_size:tuple, caption:str) -> None:
    '''launches all other functions in their respective order and sets up some values for them'''
    clock = pg.time.Clock()
    screen = pg.display.set_mode(
        [screen_size[0]*grid_size, screen_size[1]*grid_size])
    start_node_pos = [5, 5]
    end_node_pos = [18, 18]
    pg.display.set_caption(caption)

    render(grid_size, screen, set_up_nodes(grid_size, screen_size), clock, screen_size)


#Processing
def change_node_type(nodes: list, position: tuple, type: str) -> list:
    '''changes the type of a node by taking a nodes structure and a position and changing it to the given type by returning a new node structure'''
    
    if type == "floor":
        nodes[position[1]][position[0]]["color"] = (255, 255, 255)
    elif type == "start":
        nodes[position[1]][position[0]]["color"] = (0, 0, 255)
    elif type == "end":
        nodes[position[1]][position[0]]["color"] = (0, 255, 0)
    elif type == "wall":
        nodes[position[1]][position[0]]["color"] = (0, 0, 0)
    
    nodes[position[1]][position[0]]["type"] = type
    return nodes


def find_distance(nodes: list, screen_size: tuple) -> list:
    '''find the distance of all node from the start node'''
    #find start and end node
    for row in nodes:
        for node in row:
            if node["type"] == "start":
                start_node = node
            if node["type"] == "end":
                end_node = "node"
    #declare the list of already visited/known nodes
    closed_nodes = [start_node]
    #declare possible directions to look for neigbours
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    #go over all nodes and find the distance (add them to closed nodes)
    for node in closed_nodes:
        for direction in directions:
            if 0 < node["position"][0]+direction[0] < screen_size[0] and 0 < node["position"][1]+direction[1] < screen_size[1]:
                current_node = nodes[node["position"][0]+direction[0]][node["position"][1]+direction[1]]
                if current_node not in closed_nodes and current_node["type"] != "wall":
                    current_node["distance"] = node["distance"] + 1
                    current_node["color"] = (255, 255-(node["distance"]+1)*5, 255-(node["distance"]+1)*5)
                    if current_node["type"] == "end":
                        current_node["color"] = (0, 255, 0)
                    closed_nodes.append(current_node)
                    
    return nodes
        
def find_path(nodes: list, screen_size: tuple) -> list:
    path = []
    surround = []
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    def find_next_node(node: dict):
        if node["type"] == "start":
            return
        for direction in directions:
            current = nodes[node["position"][0] + direction[0]][node["position"][1] + direction[1]]
            
            if current["distance"] < node["distance"] and current["type"] != "wall":
                find_next_node(current)
                node["color"] = (50, 50, 50)
                print(node["distance"])
                break
    
    for row in nodes:
        for node in row:
            if node["type"] == "end":
                find_next_node(node)
    


    #for node in path:

        
    return nodes

def render(grid_size, screen, nodes, clock, screen_size: tuple):
    '''renders the map and handles input as needed'''
    dt = clock.tick(120)  # delta time
    started = False
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

        mouse_x, mouse_y = pg.mouse.get_pos()

        if pg.mouse.get_pressed()[0] and not started:
            for row in nodes:
                for node in row:
                    if node["rect"].collidepoint(mouse_y, mouse_x):
                        change_node_type(nodes, node["position"], "wall")

        if pg.mouse.get_pressed()[1] and not started:
            nodes = find_distance(nodes, screen_size)
            find_path(nodes, screen_size)
            started = True

        screen.fill((0, 0, 0))

        for row in nodes:
            for node in row:
                pg.draw.rect(screen, node.get("color"), node.get("rect"))

        pg.display.update()



start_pathdinding(GRID_SIZE, SCREEN_SIZE, TITLE)
