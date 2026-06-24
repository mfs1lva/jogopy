import random
import sys
from random import choice

import pygame.display

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory

from pygame import Rect
from pygame import Surface
from pygame.font import Font


class Level:

    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('levelb'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 4000 #4s
        self.clock = pygame.time.Clock()

        if game_mode in [MENU_OPTION[0], MENU_OPTION[1]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        pygame.time.set_timer(EVENT_ENEMY,SPAWN_TIME)



    def run (self, ):
        # Musica:
        # pygame.mixer_music.load()
        # pygame.mixer_music.play(-1)
        # clock = pygame.time.Clock()

        while True:
            self.clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # sei lá
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000} : .1f', C_WHITE, (10,5))
            self.level_text(14, f'fps: {self.clock.get_fps() : .0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)} ', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, texte_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, texte_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)