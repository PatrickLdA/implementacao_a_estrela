# %%
from IniciaMapa import IniciaMapa
from TesteObjetivo import TesteObjetivo
from ExpandeNo import ExpandeNo
from CalculoEsforco import CalculoEsforco
from Movimenta import Movimenta
from random import randint
import pandas as pd
import numpy as np

# %%
def sorteio_pontos_aleatorios(numero_sorteios):
    sorteados = []
    for i in range(numero_sorteios):
        x = randint(0, 29)
        y = randint(0, 29)

        sorteados.append([x,y])

    return sorteados

def salva_lista(lista, caminho):
    txtfile = open(caminho, 'w')
    for element in lista:
        txtfile.write(str(element) + '\n')
    txtfile.close()

# %%
lista_multip_g=[0, 0.25, 0.5, 0.75, 1, 2, 3]
salva_lista(lista_multip_g, 'resultados_teste_heuristica/lista_multip_g.txt')

lista_inicio=sorteio_pontos_aleatorios(50)
salva_lista(lista_inicio, 'resultados_teste_heuristica/lista_inicio.txt')

lista_fim=sorteio_pontos_aleatorios(50)
salva_lista(lista_fim, 'resultados_teste_heuristica/lista_fim.txt')

# %%
result_list = []
DIMENSOES=[30,30] # Lista com as dimensões do tabuleiro

tabuleiro = IniciaMapa(dimensoes=DIMENSOES)

for multiplicador_g in lista_multip_g:
    print(f"\n\n\nTESTE COM MULTIPLICADOR_G={multiplicador_g}")
    for loc_inicio, loc_fim in zip(lista_inicio, lista_fim):
        try:
            rota=[] # Lista onde serão salvos os passos
            nos_filhos=[] # Lista com todos os nós a serem explorados. Em outras palavras: borda.
            variacao_altura=0 # Variação da altura ao longo do percurso

            print(f"Posição inicial:{loc_inicio}; Posição final:{loc_fim}")

            rota.append(loc_inicio)

            while(not TesteObjetivo(ponto_atual=rota[-1], destino=loc_fim)[0]):
                lista_filhos = ExpandeNo(posicao_atual=rota[-1], tabuleiro=tabuleiro)
                nos_filhos = nos_filhos + lista_filhos

                lista_fn = CalculoEsforco(tabuleiro=tabuleiro, loc_atual=rota[-1], lista_filhos=lista_filhos, loc_fim=loc_fim,
                                            multiplicador_g=multiplicador_g)

                proximo_movimento = Movimenta(lista_fn, lista_filhos, rota, loc_fim)

                variacao_altura_atual = tabuleiro.item(rota[-1][0], rota[-1][1]) - tabuleiro.item(proximo_movimento[0], proximo_movimento[1])
                variacao_altura += variacao_altura_atual 

                rota.append(proximo_movimento)

            print("Fim do experimento")
            print(f"Quantidade de movimentos: {len(rota)-1}\n")

            result_list.append([loc_inicio, loc_fim, multiplicador_g, len(rota)-1, variacao_altura])

        except Exception:
            result_list.append([loc_inicio, loc_fim, multiplicador_g, np.nan, np.nan])

# %%
df = pd.DataFrame(result_list, columns=["loc_inicio", "loc_fim", "multip_g", "numero_passos", "variacao_altura"])

# %%
df.to_csv("resultados_teste_heuristica/compilado_resultados.csv")