import pygame as pg


#globals
SCREEN_DIMENSIONS = [500, 500]
CAPTION = "Pathfinding Algorithm"

#render setup
pg.init()

screen = pg.display.set_mode(SCREEN_DIMENSIONS);
pg.display.set_caption(CAPTION)

#classes
class Pathfinder:
    def __init__(self, running, screen):
        self.running = running
        self.screen = screen
    
    def run_main_loop(self):
        '''runs the main loop, handles rendering as well as the logic'''
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            screen.fill((0, 0, 0))

            #All the logic

            pg.display.update()
        
        pg.quit()

pathfinder = Pathfinder(True, screen)
pathfinder.run_main_loop()






