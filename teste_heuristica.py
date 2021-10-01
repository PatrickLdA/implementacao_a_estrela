# %%
from IniciaMapa import IniciaMapa
from TesteObjetivo import TesteObjetivo
from ExpandeNo import ExpandeNo
from CalculoEsforco import CalculoEsforco
from Movimenta import Movimenta

from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
lista_multip_g= [round(i,1) for i in np.arange(0, 3.1, .1)] #[0, 0.25, 0.5, 0.75, 1, 2, 3]
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
# %%
# Plotagem da variação do número de passos com o incremento de multip_g
#ax = df[['multip_g', 'numero_passos']].dropna().boxplot(by='multip_g', showfliers=False, figsize=[23,12])

ax = df[['multip_g', 'numero_passos']].dropna().groupby('multip_g').mean().plot(figsize=[25,10])
plt.savefig('resultados_teste_heuristica/variacao_passos_medios.png')
plt.show()

# %%
# Plotagem da variação de altura com o incremento de multip_g
#ax = df[['multip_g', 'variacao_altura']].dropna().boxplot(by='multip_g', showfliers=False, figsize=[23,12])

ax = df[['multip_g', 'variacao_altura']].dropna().groupby('multip_g').mean().plot(figsize=[25,10])
plt.savefig('resultados_teste_heuristica/variacao_altura_media.png')
plt.show()

# %%
# Plotagem de percentual de testes não convergentes
null_plot = df[['multip_g', 'variacao_altura']].drop('multip_g', 1).isna().groupby(df['multip_g']).sum()*2

null_plot.plot.bar(figsize=[25,10])
plt.savefig('resultados_teste_heuristica/convergencia_percentual.png')

# %%
ax = null_plot.reset_index().plot(x='multip_g', figsize=[25,10], use_index=False, kind='bar')#, kind='bar')

df[['multip_g', 'variacao_altura']].dropna().groupby('multip_g').mean().plot(color='r', ax=ax, use_index=False)

df[['multip_g', 'numero_passos']].dropna().groupby('multip_g').mean().plot(color='g', ax=ax, use_index=False)


plt.show()

# %%
fig, ax1 = plt.subplots(figsize=[25,10])

color = 'tab:red'
ax1.set_xlabel('')
ax1.set_ylabel('', color=color)
ax1.bar(x=null_plot.index, height=null_plot['variacao_altura'], 
            color=color, width=.03, alpha=.5,
            label='Percentagem de não convergência')
ax1.tick_params(axis='y', labelcolor=color)

ax1.plot(df[['multip_g', 'numero_passos']].dropna().groupby('multip_g').mean().index,
            df[['multip_g', 'numero_passos']].dropna().groupby('multip_g').mean()['numero_passos'].tolist(),
            color = color,
            label='Número de passos médios')

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('', color=color)  # we already handled the x-label with ax1
ax2.plot(df[['multip_g', 'variacao_altura']].dropna().groupby('multip_g').mean().index, df[['multip_g', 'variacao_altura']].dropna().groupby('multip_g').mean().values,
            color=color, label='Variação da altura')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped

# ask matplotlib for the plotted objects and their labels
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0)


plt.xticks(null_plot['variacao_altura'].index)
ax1.tick_params(axis='both', which='major', labelsize=20)
ax2.tick_params(axis='both', which='major', labelsize=20)

plt.savefig('resultados_teste_heuristica/compilado.png')
plt.show()

# %%
