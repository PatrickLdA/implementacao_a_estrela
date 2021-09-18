from IniciaMapa import IniciaMapa
from Inicio import Inicio
from TesteObjetivo import TesteObjetivo
from ExpandeNo import ExpandeNo
from CalculoEsforco import CalculoEsforco
from Movimenta import Movimenta
from PrintaEstados import PrintaEstados

rota=[] # Lista onde serão salvos os passos
nos_filhos=[] # Lista com todos os nós a serem explorados. Em outras palavras: borda.
tabuleiro=[] # Tabuleiro
DIMENSOES=[30,30] # Lista com as dimensões do tabuleiro

loc_inicio=[] # Ponto de partida
loc_fim=[] # Objetivo final

tabuleiro = IniciaMapa(dimensoes=DIMENSOES)
loc_inicio, loc_fim = Inicio(tabuleiro)
rota.append(loc_inicio)

while(not TesteObjetivo(rota[-1], loc_fim)[0]):
    print("\nAinda não chegamos lá!")

    lista_filhos = ExpandeNo(rota[-1], tabuleiro)
    nos_filhos = nos_filhos + lista_filhos

    lista_fn = CalculoEsforco(tabuleiro=tabuleiro, loc_atual=rota[-1], lista_filhos=lista_filhos, loc_fim=loc_fim)

    proximo_movimento = Movimenta(lista_fn, lista_filhos, rota, loc_fim)
    print("Caminhando para" + str(proximo_movimento))
    rota.append(proximo_movimento)

print("Chegamos ao destino!")
PrintaEstados()