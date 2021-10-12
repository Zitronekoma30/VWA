import pygame as pg
import numpy as np


#globals
SCREEN_DIMENSIONS = [500, 500]
GRID_SIZE = 16
CAPTION = "Pathfinding Algorithm"

#render setup
pg.init()

screen = pg.display.set_mode(SCREEN_DIMENSIONS);
pg.display.set_caption(CAPTION)

#classes

class BackgroundRenderer:
    def __init__(self, surface, width, height, grid_size):
        self.surface = surface
        self.width = width
        self.height = height
        self.grid_size = grid_size
    
    def draw_background(self):
        for y in range(self.height):
            for x in range(self.width):
                pg.draw.rect(self.surface, (255, 255, 255), pg.Rect(x * self.grid_size, y * self.grid_size, self.grid_size - 2, self.grid_size - 2))

class Obstacle:
    def __init__(self, surface, position, grid_size):
        self.surface = surface
        self.position = position
        self.grid_size = grid_size
        self.color = (0, 0, 0)
        self.rect = pg.Rect(position[0]*self.grid_size, position[1]*self.grid_size, self.grid_size, self.grid_size)
    
    def draw_self(self):
        '''draws self.rect at self.position in self.color'''
        pg.draw.rect(self.surface, self.color, self.rect)

class Pathfinder:
    def __init__(self, running, screen, grid_size, screen_dimensions):
        self.running = running
        self.screen = screen
        self.clock = pg.time.Clock()
        self.grid_size = grid_size

        self.obstacles = []

        #Instances
        self.bg_renderer = BackgroundRenderer(self.screen, int(np.floor(screen_dimensions[0]/self.grid_size)), int(np.floor(screen_dimensions[1]/self.grid_size)), self.grid_size)
    
    def run_main_loop(self):
        '''starts the main loop, handles rendering as well as the logic'''
        delta_time = self.clock.tick(120)
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            screen.fill((0, 0, 0))
            
            #rendering
            self.bg_renderer.draw_background()

            #set up in loop variables
            mouse_x, mouse_y = pg.mouse.get_pos()

            #All the logic
            
            #set obstacles in grid
            if pg.mouse.get_pressed()[0]:
                current_obstacle = Obstacle(self.screen, (mouse_x, mouse_y), self.grid_size)
                print
                for obstacle in self.obstacles:
                    if current_obstacle.rect.colliderect(obstacle.rect):
                        pass
                    else:
                        self.obstacles.append(current_obstacle)



            #set goal

            #set cursor position
            






            pg.display.update()
        
        pg.quit()

pathfinder = Pathfinder(True, screen, GRID_SIZE, SCREEN_DIMENSIONS)
pathfinder.run_main_loop()






