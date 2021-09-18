import matplotlib.pyplot as plt
import numpy as np
import random

def IniciaMapa(dimensoes=[30,30]):
    """
    Carrega randomicamente um tabuleiro com valores aleatórios (por padrão, [30,30])

    Entrada:
    - Dimensões desejadas para o tabuleiro (lista)

    Saída:
    - Matriz x por y com valores aleatórios
    """
    print(5*"*")
    print("TRABALHO DE INTELIGÊNCIA ARTIFICIAL - IMPLEMENTAÇÃO A*")
    print(5*"*")
    print("Neste trabalho, um tabuleiro 2D representando um mapa é gerado e, com a entrada dos pontos de origem e destino, o problema busca encontrar o deslocamento ótimo com o algoritmo A*")

    tabuleiro = np.random.randint(20, size=(dimensoes[0], dimensoes[1]))

    print("Seu mapa pode ser visto em uma janela em suspensão")

    plt.imshow(tabuleiro, cmap="Reds")
    plt.colorbar()
    plt.show(block=False)

    input("Pressione enter para continuar")

    return tabuleiro

#if __name__ == '__main__':
