from code.Menu import Menu

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(576, 324))


    def run (self):
        menu = Menu(self.window)

        while (True):
            menu.run()

            while True:
                menu.run()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()