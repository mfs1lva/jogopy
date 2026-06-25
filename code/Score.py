import pygame
from pygame import Surface, K_RETURN, K_BACKSPACE, KEYDOWN, K_ESCAPE
from pygame import Rect
from pygame.font import Font
from datetime import datetime

from code.Const import C_YELLOW, SCORE_POS, MENU_OPTION, C_WHITE
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.menu_option = 0

        self.surf = pygame.image.load("asset/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save_score(self, game_mode, player_score: list[int]):
        db_proxy = DBProxy('DBScore')
        name = ''

        # Define score e texto
        if game_mode == MENU_OPTION[0]:
            score = player_score[0]
            text = 'Entre com seu nome (4 caracteres):'

        elif game_mode == MENU_OPTION[1]:
            score = int((player_score[0] + player_score[1]) / 2)
            text = 'Entre com o nome do time (4 caracteres):'

        elif game_mode == MENU_OPTION[2]:
            if player_score[0] >= player_score[1]:
                score = player_score[0]
                text = '[Player 1] Entre com seu nome:'
            else:
                score = player_score[1]
                text = '[Player 2] Entre com seu nome:'

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                elif event.type == pygame.KEYDOWN:

                    if event.key == K_RETURN and len(name) == 4:

                        db_proxy.save({
                            'name': name,
                            'score': score,
                            'date': get_formatted_date()
                        })

                        db_proxy.close()

                        self.show_score()
                        return

                    elif event.key == K_BACKSPACE:
                        name = name[:-1]

                    else:
                        if len(name) < 4 and event.unicode.isprintable():
                            name += event.unicode.upper()

            self.window.blit(self.surf, self.rect)

            self.score_text(
                40,
                'VOCÊ GANHOU!!',
                C_YELLOW,
                SCORE_POS['Title']
            )

            self.score_text(
                20,
                text,
                C_WHITE,
                SCORE_POS['EnterName']
            )

            self.score_text(
                20,
                name,
                C_WHITE,
                SCORE_POS['Name']
            )

            pygame.display.flip()

    def show_score(self):

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            self.window.blit(self.surf, self.rect)

            self.score_text(
                48,
                'TOP 10 SCORE',
                C_YELLOW,
                SCORE_POS['Title']
            )

            self.score_text(
                20,
                'NOME        SCORE        DATA',
                C_YELLOW,
                SCORE_POS['Label']
            )

            for i, player_score in enumerate(list_score):
                id_, name, score, date = player_score

                self.score_text(
                    20,
                    f'{name:<4}   {score:05d}   {date}',
                    C_WHITE,
                    SCORE_POS[i]
                )

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, texte_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, texte_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H.%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
