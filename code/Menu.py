import pygame.image


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('asset/backgrounds/nature_6/orig.png') # carrega a imagem
        self.rect = self.surf.get_rect(left=0, top=0) # cria o retangulo para armazenar a imagem


    def run (self, ):
        self.window.blit(source=self.surf, dest=self.rect) # pede pra colocar a imagem dentro do retangulo
        pygame.display.flip() # atualiza a tela
        pass
