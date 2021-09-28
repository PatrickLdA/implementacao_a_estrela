import math


def distancia_euclidiana(a, b):
    return (math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2))


def CalculoEsforco(tabuleiro, loc_atual, lista_filhos, loc_fim, multiplicador_g=0.25):
    """
    Pega a posicao atual e calcula a heuristica para a borda atual em lista_filhos

    Entrada: 
    - borda atual
    - Localização do destino

    Saída: lista de f(n), que combina a distancia euclidiana até o objetivo e a variação de altura até o próximo nó
    """
    # Calculo do custo de deslocamento g(n)
    lista_g = []
    for candidato in lista_filhos:
        altura_atual = tabuleiro[loc_atual[0]][loc_atual[1]]
        altura_candidato = tabuleiro[candidato[0]][candidato[1]]

        custo_deslocamento = altura_candidato - altura_atual

        lista_g.append(custo_deslocamento)

    # Calculo da heurística h(n)
    lista_h = []
    for candidato in lista_filhos:
        distancia_fim = distancia_euclidiana(candidato, loc_fim)

        lista_h.append(distancia_fim)

    # Soma do deslocamento e da heurística
    lista_fn = []
    for g_n, h_n in zip(lista_g, lista_h):
        lista_fn.append(g_n*multiplicador_g + h_n)

    return lista_fn

# if __name__ == '__main__':
