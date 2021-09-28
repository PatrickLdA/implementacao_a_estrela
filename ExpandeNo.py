
def ExpandeNo(posicao_atual, tabuleiro, grid):
    """
    Função que lista os possíveis próximos movimentos (em outras palavras, olha ao redor e demarca a borda atual) 
    e dá append em self.nos_filhos

    Entrada: posicao atual

    Saída: lista de nós filhos para o nó atual
    """

    x_var_list = [0, 1, -1]
    y_var_list = [0, 1, -1]

    lista_bruta_candidatos = []

    for x_var in x_var_list:
        for y_var in y_var_list:
            candidato = [posicao_atual[0]+x_var, posicao_atual[1]+y_var]
            lista_bruta_candidatos.append(candidato)

    lista_filhos = []

    for valor in lista_bruta_candidatos:
        # Testa se não é o mesmo valor e se não excede as dimensoes do tabuleiro
        if (valor != posicao_atual) and (valor[0] <= len(tabuleiro)-1) and (valor[1] <= len(tabuleiro[0])-1) and (valor[0] >= 0) and (valor[1] >= 0):
            lista_filhos.append(valor)

    """ for filho in lista_filhos:
        grid[filho[0]][filho[1]].make_closed() """

    return lista_filhos


if __name__ == '__main__':
    print('hey')
