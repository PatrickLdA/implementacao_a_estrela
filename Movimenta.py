def Movimenta(lista_fn, lista_filhos, rota, loc_fim, grid):
    """
    Função que recebe a lista de esforço, faz o movimento para o melhor nó e atualiza self.rota

    Input:
    - lista de f_n do nó atual
    - Lista de nós da borda atual

    Output: LatLong do próximo movimento
    """
    if loc_fim in lista_filhos:
        return loc_fim

    i = 0
    while True:
        lista_ordenada = sorted(lista_fn)
        min_f = lista_ordenada[i]

        min_index = lista_fn.index(min_f)

        proximo_movimento = lista_filhos[min_index]

        if proximo_movimento not in rota:
            grid[proximo_movimento[0]][proximo_movimento[1]].make_open()
            return proximo_movimento

        i += 1

    """ for i in range(len(lista_fn)):
        lista_ordenada = sorted(lista_fn)
        min_f = lista_ordenada[i]

        min_index = lista_fn.index(min_f)

        proximo_movimento = lista_filhos[min_index]

        if proximo_movimento not in rota:
            return proximo_movimento """


if __name__ == '__main__':
    print('Hey')
