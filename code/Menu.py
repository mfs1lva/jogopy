import pygame
from pygame import Rect, Surface
from pygame.font import Font

from code.Const import (
    WIN_WIDTH,
    COLOR_PURPLE,
    MENU_OPTION,
    C_WHITE,
    C_YELLOW
)


class Menu:

    def __init__(self, window):
        self.window = window
        self.menu_option = 0

        self.surf = pygame.image.load("asset/menuback.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            # seta para baixo
            if event.key == pygame.K_DOWN:
                if self.menu_option < len(MENU_OPTION) - 1:
                    self.menu_option += 1
                else:
                    self.menu_option = 0

            # seta para cima
            elif event.key == pygame.K_UP:
                if self.menu_option > 0:
                    self.menu_option -= 1
                else:
                    self.menu_option = len(MENU_OPTION) - 1

            # Enter
            elif event.key == pygame.K_RETURN:
                return MENU_OPTION[self.menu_option]

    def run(self):

        # fundo
        self.window.blit(self.surf, self.rect)

        # título
        self.menu_text(
            50,
            "Jogo",
            (73, 73, 166),
            (WIN_WIDTH // 2, 70)
        )

        self.menu_text(
            50,
            "Python",
            COLOR_PURPLE,
            (WIN_WIDTH // 2, 120)
        )

        # opções
        for i in range(len(MENU_OPTION)):

            color = C_YELLOW if i == self.menu_option else C_WHITE

            self.menu_text(
                20,
                MENU_OPTION[i],
                color,
                (WIN_WIDTH // 2, 200 + 25 * i)
            )

    def menu_text(
            self,
            text_size: int,
            text: str,
            text_color: tuple,
            text_center_pos: tuple
    ):

        text_font: Font = pygame.font.SysFont(
            "Lucida Sans Typewriter",
            text_size
        )

        text_surf: Surface = text_font.render(
            text,
            True,
            text_color
        ).convert_alpha()

        text_rect: Rect = text_surf.get_rect(
            center=text_center_pos
        )

        self.window.blit(text_surf, text_rect)