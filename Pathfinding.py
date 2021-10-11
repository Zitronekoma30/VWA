import pygame as pg


#globals
SCREEN_DIMENSIONS = [500, 500]
CAPTION = "Pathfinding Algorithm"

#render setup
pg.init()

screen = pg.display.set_mode(SCREEN_DIMENSIONS);
pg.display.set_caption(CAPTION)

#classes
class BackgroundRenderer():
    def __init__(self, surface, width, height, grid_size):
        self.surface = surface
        self.width = width
        self.height = height
        self.grid_size = grid_size
    
    def draw_background(self):
        for y in range(self.height):
            for x in range(self.width):
                pg.draw.rect(self.surface, (255, 255, 255), pg.Rect(x * self.grid_size, y * self.grid_size, self.grid_size - 2, self.grid_size - 2))

class Pathfinder:
    def __init__(self, running, screen, grid_size):
        self.running = running
        self.screen = screen
        self.clock = pg.time.Clock()
        self.grid_size = grid_size

        #Instances
        self.bg_renderer = BackgroundRenderer(self.screen, 500, 500, self.grid_size)
    
    def run_main_loop(self):
        '''runs the main loop, handles rendering as well as the logic'''
        delta_time = self.clock.tick(120)
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            screen.fill((0, 0, 0))
            
            #rendering
            self.bg_renderer.draw_background()

            #All the logic

            pg.display.update()
        
        pg.quit()

pathfinder = Pathfinder(True, screen, 16)
pathfinder.run_main_loop()






