from numpy import equal


def TesteObjetivo(ponto_atual, destino):
    """
    Função que recebe o ponto atual e o ponto objetivo confere se é o objetivo

    Inputs:
    - LatLong do ponto atual
    - LatLong do objetivo

    Output: booleano TRUE caso seja o ponto final e FALSE caso não
    """

    if ponto_atual[0] == destino[0] and ponto_atual[1] == destino[1]:
        return True
    else:
        return False

# if __name__ == '__main__':
