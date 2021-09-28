from IniciaMapa import IniciaMapa
from Inicio import Inicio
from TesteObjetivo import TesteObjetivo
from ExpandeNo import ExpandeNo
from CalculoEsforco import CalculoEsforco
from Movimenta import Movimenta
from PrintaEstados import PrintaEstados
import InterfaceGrafica as IG
import pygame
from SpotClass import Spot

rota = []  # Lista onde serão salvos os passos
# Lista com todos os nós a serem explorados. Em outras palavras: borda.
nos_filhos = []
tabuleiro = []  # Tabuleiro

# Largura da janela do display
LARGURA = 800

# Número de linhas que a janela conterá
LINHAS = 40

# Espaço ocupado por cada nó no tabuleiro
GAP = LARGURA / LINHAS

# Lista com as dimensões do tabuleiro (tabuleiro quadrado)
DIMENSOES = [LINHAS, LINHAS]

loc_inicio = []  # Ponto de partida
loc_fim = []  # Objetivo final

# tabuleiro = IniciaMapa(dimensoes=DIMENSOES)
tabuleiro = IniciaMapa((LINHAS, LINHAS))
grid = IG.make_grid(tabuleiro, LINHAS, LARGURA)

WIN = pygame.display.set_mode((LARGURA, LARGURA))
pygame.display.set_caption("A* Path Finding Algorithm")
start = None
end = None
run = True

while run:
    IG.draw(WIN, grid, LINHAS, LARGURA)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:  # LEFT
            pos = pygame.mouse.get_pos()
            linha, coluna = IG.get_clicked_pos(pos, LINHAS, LARGURA)
            spot = grid[linha][coluna]
            if not start and spot != end:
                start = spot
                start.make_start()
                loc_inicio = (round(start.x/GAP), round(start.y/GAP))
                rota.append((start.x, start.y))
                print(f'Ponto inicial: {loc_inicio}')

            elif not end and spot != start:
                end = spot
                end.make_end()
                loc_fim = (round(end.x/GAP), round(end.y/GAP))
                print(f'Ponto final: {loc_fim}')

            elif spot != end and spot != start:
                spot.make_barrier()
                print(
                    f'Barreira no ponto: ({round(spot.x/GAP)},{round(spot.y/GAP)})')

        elif pygame.mouse.get_pressed()[2]:  # RIGHT
            pos = pygame.mouse.get_pos()
            linha, coluna = IG.get_clicked_pos(pos, LINHAS, LARGURA)
            spot = grid[linha][coluna]
            spot.reset(tabuleiro[linha, coluna])
            if spot == start:
                start = None
            elif spot == end:
                end = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start and end:
                for linha in grid:
                    for spot in linha:
                        spot.update_neighbors(grid)

                IG.algorithm(lambda: IG.draw(WIN, grid, LINHAS, LARGURA),
                             grid, rota, start, end, nos_filhos)

            if event.key == pygame.K_c:
                start = None
                end = None
                grid = IG.make_grid(tabuleiro, LINHAS, LARGURA)
                print('Tabuleiro resetado.')

pygame.quit()
