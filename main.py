class a_estrela():
	def __init__(self):
		self.rota=[] # Lista onde serão salvos os passos
		self.nos_filhos=[] # Lista com todos os nós a serem explorados. Em outras palavras: borda.
		self.tabuleiro=[] # Tabuleiro
        
        self.inicio=[] # Ponto de partida
        self.fim=[] # Objetivo final

        self.inicia_mapa()
        self.inicio()

        # while(self.teste_objetivo):
            # self.expande_no()
            # lista_fn = self.calculo_esforco()
            # self.movimenta(lista_fn)

        # self.printa_estados()

	
    def inicio(self):
    """
    Função que printa instruções do código e recebe o ponto de partida e o ponto final
    """

	def inicia_mapa(self):
	"""
    Carrega randomicamente um tabuleiro 30x30 com valores aleatórios

    Saída:
    - Matriz 30x30 com valores aleatórios em self.tabuleiro
	"""
		
    def expande_no(self, posicao_atual):
    """
    Função que lista os possíveis próximos movimentos (em outras palavras, olha ao redor e demarca a borda atual) e dá append em self.nos_filhos

    Entrada: posicao atual
    """

    def calculo_esforco(self):
    """
    Pega a posicao atual em self.rota[-1] e calcula a heuristica para a borda atual em self.nos_filhos[-1]

    Entrada: objetos da classe self.rota e self.nos_filhos
    Saída: lista de f(n), que combina a distancia euclidiana até o objetivo e a variação de altura até o próximo nó
    """


    def movimenta(self, lista_fn):
    """
    Função que recebe a lista de esforço, faz o movimento para o melhor nó e atualiza self.rota
    """

    def teste_objetivo(self):
    """
    Função que recebe o ponto atual e confere se é o objetivo
    """

    def printa_estados(self):
    """
    Função que pega as listas self.rota e self.nos_filhos e self.tabuleiro e plota graficamente o algoritmo
    """