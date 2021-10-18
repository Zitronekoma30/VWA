import pygame as pg
import numpy as np
from Elements import BackgroundRenderer, Goal, Cursor, Obstacle


#globals
SCREEN_DIMENSIONS= [500, 500]
GRID_SIZE = 16
CAPTION = "Pathfinding Algorithm"

#render setup
pg.init()

screen = pg.display.set_mode(SCREEN_DIMENSIONS);
pg.display.set_caption(CAPTION)

#classes



class Pathfinder:
    def __init__(self, running: bool, screen, grid_size: int, screen_dimensions: list):
        self.running = running
        self.screen = screen
        self.clock = pg.time.Clock()
        self.grid_size = grid_size

        self.obstacles = []

        #Instances
        self.goal = Goal([400, 380], [self.grid_size, self.grid_size], (30, 30, 255), self.grid_size)
        self.cursor = Cursor([20, 20], [self.grid_size, self.grid_size], (255, 255, 0), self.grid_size)
        self.bg_renderer = BackgroundRenderer(self.screen, int(np.floor(screen_dimensions[0]/self.grid_size)), int(np.floor(screen_dimensions[1]/self.grid_size)), self.grid_size)
    
    def calculate_distance(start: list, end: list):
        return [end[0] - start[0], end[1] - start[1]]

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

            #set obstacles in grid
            if pg.mouse.get_pressed()[0]:
                current_obstacle = Obstacle(self.screen, (mouse_x, mouse_y), self.grid_size)
                self.obstacles.append(current_obstacle)
            
            if pg.mouse.get_pressed()[2]:
                for obstacle in self.obstacles:
                    if obstacle.rect.collidepoint(mouse_x, mouse_y):
                        self.obstacles.remove(obstacle)
                
            for obstacle in self.obstacles:
                obstacle.draw_self()
                for obstacle_1 in self.obstacles:
                    if obstacle.rect.colliderect(obstacle_1.rect) and obstacle_1 != obstacle:
                         self.obstacles.remove(obstacle_1)
                

            print(len(self.obstacles))
                


            #draw goal
            self.goal.draw(self.screen)

            #set cursor position
            






            pg.display.update()
        
        pg.quit()

pathfinder = Pathfinder(True, screen, GRID_SIZE, SCREEN_DIMENSIONS)
pathfinder.run_main_loop()






