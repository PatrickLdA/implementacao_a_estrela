def TesteObjetivo(ponto_atual, destino):
    """
    Função que recebe o ponto atual e o ponto objetivo confere se é o objetivo

    Inputs:
    - LatLong do ponto atual
    - LatLong do objetivo

    Output: booleano TRUE caso seja o ponto final e FALSE caso não
    """
    return [True if ponto_atual == destino else False]

#if __name__ == '__main__':
