# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *

from main_menu import main_menu
from jogo import game
from jogo_gru import partitura
from selecao_musica import cardapio


#======= inicialização =======#
pygame.init()
pygame.font.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Guitar Hero')

state = INIT
while state != QUIT:
    if state == INIT:
        state = main_menu(window)
    if state == MUSICA:
        state = cardapio(window)
    if state == GAME:
        state = game(window)
    if state == GAME_DESENHADO:
        state = partitura(window)
   # else:
    #    state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

