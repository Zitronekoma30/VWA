import pygame as pg
import numpy as np


class Cursor:
    def __init__(self, position: list, size: list, color: tuple, grid_size: int):
        self.position = position
        self.size = size
        self.color = color
        self.grid_size = grid_size

        self.rect = pg.Rect(np.floor(position[0]/self.grid_size)*self.grid_size, np.floor(position[1]/self.grid_size) * self.grid_size, size[0], size[1])
    
    def update(self, surface):
        self.rect = pg.Rect(np.floor(self.position[0]/self.grid_size)*self.grid_size, np.floor(self.position[1]/self.grid_size) * self.grid_size, self.size[0], self.size[1])
        pg.draw(surface, self.color, self.rect)


class Goal:
    def __init__(self, position: list, size: list, color: tuple, grid_size: int):
        self.position = position
        self.size = size
        self.color = color
        self.grid_size = grid_size
        
        self.rect = pg.Rect(np.floor(position[0]/self.grid_size)*self.grid_size, np.floor(position[1]/self.grid_size)*self.grid_size, size[0], size[1])
    
    def draw(self, surface):
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
    
    def draw_self(self):
        '''draws self.rect at self.position in self.color'''
        pg.draw.rect(self.surface, self.color, self.rect)