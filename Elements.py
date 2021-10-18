import pygame as pg
import numpy as np


class Cursor:
    def __init__(self, position: list, color: tuple, grid_size: int):
        self.position = position
        self.color = color
        self.grid_size = grid_size

        self.path = []
        self.rect = pg.Rect(self.position[0]*self.grid_size, self.position[1]*self.grid_size, self.grid_size, self.grid_size)

    def calculate_distance(self, x1, y1, x2, y2):
        dist = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return dist

    def update(self, obstacles: list, goal) -> list:
        '''runs the pathfinding logic'''
        options = []

        #vertical
        options.append(pg.Rect(self.position[0]*self.grid_size, (self.position[1]+1)*self.grid_size, self.grid_size, self.grid_size))
        options.append(pg.Rect(self.position[0]*self.grid_size, (self.position[1]-1)*self.grid_size, self.grid_size, self.grid_size))

        #horizontal
        options.append(pg.Rect((self.position[0]+1)*self.grid_size, self.position[1]*self.grid_size, self.grid_size, self.grid_size))
        options.append(pg.Rect((self.position[0]-1)*self.grid_size, self.position[1]*self.grid_size, self.grid_size, self.grid_size))

        #as is
        options.append(pg.Rect(self.position[0]*self.grid_size, self.position[1]*self.grid_size, self.grid_size, self.grid_size))

        for option in options:
            #if self.calculate_distance(option.left, option.top, goal.rect.left, goal.rect.top) > self.calculate_distance(self.rect.left, self.rect.top, goal.rect.left, goal.rect.top):
            #    options.remove(option)
            for option1 in options:
                if self.calculate_distance(option1.left, option1.top, goal.rect.left, goal.rect.top) > self.calculate_distance(option.left, option.top, goal.rect.left, goal.rect.top):
                    options.remove(option1)

        
        self.position = [options[0].left/self.grid_size, options[0].top/self.grid_size]
        self.rect = pg.Rect(self.position[0]*self.grid_size, self.position[1]*self.grid_size, self.grid_size, self.grid_size)

        self.path.append(self.rect)
        return self.path
        #print(len(options))
    
    
    def draw(self, surface):
        '''draws the cursor'''
        pg.draw.rect(surface, self.color, self.rect)


class Goal:
    def __init__(self, position: list, color: tuple, grid_size: int):
        self.position = position
        self.color = color
        self.grid_size = grid_size
        
        self.rect = pg.Rect(self.position[0]*self.grid_size, self.position[1]*self.grid_size, self.grid_size, self.grid_size)
        
    def draw(self, surface):
        '''draws the goal'''
        pg.draw.rect(surface, self.color, self.rect)


class BackgroundRenderer:
    def __init__(self, surface, width: int, height: int, grid_size: int):
        self.surface = surface
        self.width = width
        self.height = height
        self.grid_size = grid_size
    
    def draw_background(self):
        for y in range(self.height):
            for x in range(self.width):
                pg.draw.rect(self.surface, (255, 255, 255), pg.Rect(x * self.grid_size, y * self.grid_size, self.grid_size - 2, self.grid_size - 2))

class Obstacle:
    def __init__(self, surface, position: list, grid_size: int):
        self.surface = surface
        self.position = position
        self.grid_size = grid_size
        self.color = (0, 0, 0)
        self.rect = pg.Rect(np.floor(position[0]/self.grid_size)*self.grid_size, np.floor(position[1]/self.grid_size)*self.grid_size, self.grid_size, self.grid_size)

    def draw(self):
        '''draws self.rect at self.position in self.color'''
        pg.draw.rect(self.surface, self.color, self.rect)
