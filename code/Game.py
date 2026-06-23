from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Jogo Python")

        self.clock = pygame.time.Clock()

        self.menu = Menu(self.window)
        self.level = None

        self.state = "MENU"

    def run(self):

        while True:

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if self.state == "MENU":
                    menu_return = self.menu.handle_event(event)

                    if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                        self.level = Level(self.window, "Level1", menu_return)
                        self.state = "LEVEL"

                    elif menu_return == MENU_OPTION[4]:
                        pygame.quit()
                        return

            # Desenho
            if self.state == "MENU":
                self.menu.run()

            elif self.state == "LEVEL":
                self.level.run()

            pygame.display.flip()
            self.clock.tick(60)