from ExpandeNo import ExpandeNo
import pygame
import math
from queue import PriorityQueue
from TesteObjetivo import TesteObjetivo
from ExpandeNo import ExpandeNo
from CalculoEsforco import CalculoEsforco
from Movimenta import Movimenta
import SpotClass
from time import sleep


""" def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw() """


def reconstruct_path(rota, grid, draw):
    for nodo in rota:
        grid[nodo[0]][nodo[1]].make_path()
        draw()


def algorithm(draw, tabuleiro, grid, rota, start, end, nos_filhos, loc_fim):
    while(not TesteObjetivo(rota[-1], loc_fim)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        lista_filhos = ExpandeNo(rota[-1], tabuleiro, grid)
        nos_filhos = nos_filhos + lista_filhos
        sleep(0.1)

        lista_fn = CalculoEsforco(tabuleiro, rota[-1], lista_filhos, loc_fim)

        proximo_movimento = Movimenta(
            lista_fn, lista_filhos, rota, loc_fim, grid)
        print("\nCaminhando para" + str(proximo_movimento))
        rota.append(proximo_movimento)
        sleep(0.1)

        print(rota)
        print(2*'\n')
        draw()

        if TesteObjetivo(rota[-1], loc_fim):
            reconstruct_path(rota, grid, draw)
            start.make_start()
            end.make_end()
            print("Chegamos ao destino!")
            return True


def make_grid(tabuleiro, rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = SpotClass.Spot(i, j, gap, rows)
            spot.set_hight(tabuleiro[i, j])
            grid[i].append(spot)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, SpotClass.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, SpotClass.GREY,
                             (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col
