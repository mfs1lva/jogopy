import pygame
from pygame import Rect, Surface
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_PURPLE, MENU_OPTION, C_WHITE


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/backgrounds/nature_6/orig.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # desenha o fundo
        self.window.blit(self.surf, self.rect)

        # desenha o texto
        self.menu_text(
            50,
            "Jogo",
            (73, 73, 166),
            (WIN_WIDTH // 2, 70)
        )
        self.menu_text(
            50,
            "Python",
            (COLOR_PURPLE),
            (WIN_WIDTH // 2, 120)
        )

        for i in range(len(MENU_OPTION)):
            self.menu_text(
                20,
                MENU_OPTION[i],
                (C_WHITE),
                (WIN_WIDTH // 2, 200 + 25 * i)
            )


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(
            'Lucida Sans Typewriter',
            text_size
        )

        text_surf: Surface = text_font.render(
            text, True, text_color
        ).convert_alpha()

        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(text_surf, text_rect)