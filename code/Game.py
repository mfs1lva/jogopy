from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
import pygame

from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Space Nave")

        self.clock = pygame.time.Clock()

        self.menu = Menu(self.window)
        self.level = None

        self.state = "MENU"
        self.player_score = [0, 0]

    def run(self):
        score = Score(self.window)


        while True:

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if self.state == "MENU":
                    menu_return = self.menu.handle_event(event)

                    if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                        self.player_score = [0, 0]  # RESET
                        self.level = Level(self.window, "Level1", menu_return, self.player_score)
                        self.state = "LEVEL"

                    # Mostra a pontuação
                    elif menu_return == MENU_OPTION[3]:
                        score.show_score()

                    # Quita
                    elif menu_return == MENU_OPTION[4]:
                        pygame.quit()
                        return

            # Desenho
            if self.state == "MENU":
                self.menu.run()

            elif self.state == "LEVEL":

                level_return = self.level.run(self.player_score)

                if level_return:

                    if self.level.name == "Level1":
                        self.level = Level(
                            self.window,
                            "Level2",
                            self.level.game_mode,
                            self.player_score
                        )

                    elif self.level.name == "Level2":
                        score.show_victory(self.player_score)
                        score.save_score(self.level.game_mode, self.player_score)
                        self.state = "MENU"

                    else:
                        self.state = "MENU"

            pygame.display.flip()
            self.clock.tick(60)