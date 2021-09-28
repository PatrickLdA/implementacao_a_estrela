from ExpandeNo import ExpandeNo
import pygame
import math
from queue import PriorityQueue
import TesteObjetivo
import ExpandeNo
import CalculoEsforco
import Movimenta
import SpotClass


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def algorithm(draw, tabuleiro, rota, start, end, nos_filhos):
    loc_fim = (end.x, end.y)
    while(not TesteObjetivo.TesteObjetivo(rota[-1], loc_fim)[0]):
        print("\nAinda não chegamos lá!")
        lista_filhos = ExpandeNo.ExpandeNo(rota[-1], tabuleiro)
        nos_filhos = nos_filhos + lista_filhos

        lista_fn = CalculoEsforco.CalculoEsforco(
            tabuleiro=tabuleiro, loc_atual=rota[-1], lista_filhos=lista_filhos, loc_fim=loc_fim)

        proximo_movimento = Movimenta.Movimenta(
            lista_fn, lista_filhos, rota, loc_fim)
        print("Caminhando para" + str(proximo_movimento))
        rota.append(proximo_movimento)

        print("Chegamos ao destino!")

    return False


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
    win.fill(SpotClass.WHITE)

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
