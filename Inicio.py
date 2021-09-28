def Inicio(tabuleiro):
    """
    Função que printa instruções do código e recebe o ponto de partida e o ponto final
    Input:
    - Tabuleiro

    Outputs:
    - LatLong início (lista)
    - LatLong fim (lista)
    """
    loc_inicio = [tabuleiro.shape[0]+1, tabuleiro.shape[1]+1]
    loc_fim = [tabuleiro.shape[0]+1, tabuleiro.shape[1]+1]

    print("\n\n\n")
    print("Agora, vamos selecionar os pontos inicial e final do problema")

    """ while loc_inicio[0] > tabuleiro.shape[0] and loc_inicio[1] > tabuleiro.shape[1]: # Teste para evitar values errados
        print("\nEscolha as coordenadas de partida")
        loc_inicio[0]=int(input("Eixo X: "))
        loc_inicio[1]=int(input("Eixo Y: ")) """

    # Teste para evitar values errados
    while loc_fim[0] > tabuleiro.shape[0] and loc_fim[1] > tabuleiro.shape[1]:
        print("\nEscolha as coordenadas de chegada")
        loc_fim[0] = int(input("Eixo X: "))
        loc_fim[1] = int(input("Eixo Y: "))

    print("\n")
    print("Valores escolhidos:")
    print("Partida: " + str(loc_inicio))
    print("Chegada: " + str(loc_fim))

    return loc_inicio, loc_fim

# if __name__ == '__main__':
