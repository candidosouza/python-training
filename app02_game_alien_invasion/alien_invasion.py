#!/usr/bin/python3
# -*- coding: utf-8 -*
import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    """
    Inicializa o jogo e cria um obj na tela
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria uma espaçonave
    ship = Ship(screen)

    # Inicia o laço principal do jogo
    while True:

        # Observar os eventos do mouse e teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Desenha a tela a cada passagem do laço
        screen.fill(ai_settings.bg_color)

        ship.blitme()

        # Deixa a tela mais recente visivel
        pygame.display.flip()


run_game()
