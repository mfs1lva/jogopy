from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.menu = Menu(self.window)

    def run(self):

        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.menu.run()

            pygame.display.flip()