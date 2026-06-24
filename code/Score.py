import pygame
from pygame import Surface


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.menu_option = 0

        self.surf = pygame.image.load("asset/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save_score(self, player_score: list[int]):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.window.blit(self.surf, self.rect)

            pygame.display.flip()

    def show_score(self):
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            pygame.display.flip()
            pass

    def score_text(self, text_size: int, text: str, texte_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, texte_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)