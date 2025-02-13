from ambiente import Ambiente


class Agente():
    def __init__(self, ambiente: Ambiente):
        # Sensor atual [É Home?, Sujo ou Limpo?, Obstáculo?]
        self.vsensor = [True, False, False]
        self.pontuacao = 0  # Guarda o histórico de pontuação
        self.pontuacao_v2 = 0  # Guarda o histórico de pontuação
        self.histmov = []  # Guarda o histórico de movimentos
        self.ambiente = ambiente  # Inicia o Ambiente
        self.head_pointer = "s"  # Inicia apontando para o Sul (Baixo)
        self.counter = 0  # Usado no agente baseado em modelo para contar ações

    def definir_acao(self):
        """ABSTRACT

        Definir stand-by, Virar (Esquerda, direita), ir para frente
        """
        pass

    def criar_modelo(self):
        """Abstract"""
        pass

    def salvar_historico(self, acao, parametro):
        # hist_iteracao = [[agente_x, agente_y], pontos, acao, parametro_da_acao]
        # ex1: hist_iteracao = [[0, 0], 0, limpar, null]
        # ex2: hist_iteracao = [[0, 0], 1, andar, s]
        # ex3: hist_iteracao = [[0, 1], 0, alterar_sentido, e]
        # e assim por diante
        # self.histmov.append(hist_iteracao)
        self.histmov.append(
            [[self.ambiente.getAgenteX(), self.ambiente.getAgenteY()], self.head_pointer, self.pontuacao, self.pontuacao_v2, acao, parametro])

    def perceber(self):
        """Buscar informação do objeto ambiente"""
        consulta_ambiente = self.ambiente.recuperar_informacao_local()
        self.vsensor[0], self.vsensor[1] = consulta_ambiente[0], consulta_ambiente[1]

    def limpar(self):
        """
        Alterar Estado do ambiete
        """
        self.ambiente.atualizar_ambiente()

    def alterar_sentido(self, direcao):
        """
        direcao = e (Esquerda)
        direcao = d (Direita)
        altera direção baseado em um parametro.
        1 = n (Norte)
        2 = s (Sul)
        3 = l (Leste)
        4 = o (Oeste)
        """
        # Uso de arrays para usar o "Contains"
        # Se o norte for 1 e meu agente estiver virado para o Norte e virar para a esquerda temos que o Oeste é 0
        # Se o norte for 1 e meu agente estiver virado para o Sul e virar para a direita temos que o Oeste é 4
        # Dessa forma, tanto o Norte quanto o Oeste tem 2 valores de estados, vindo da direta ou da esquerda.

        # CONSTANTES
        N = [1, 5]
        O = [2]
        S = [3]
        L = [0, 4]

        E = -1
        D = +1

        # AUXILIARES
        atual = 0
        virando = 0
        novo_sentido = 0

        # ALOCAR O VALOR DO SENTIDO ATUAL A PARTIR DE UMA STRING
        if self.head_pointer == "n":
            atual = 1
        elif self.head_pointer == "o":
            atual = 2
        elif self.head_pointer == "s":
            atual = 3
        elif self.head_pointer == "l":
            atual = 4

        else:
            return "head_pointer com valor errado"

        # ALOCAR O VALOR DA MOVIMENTACAO (VIRAR)
        if direcao == "e":
            virando = E
        elif direcao == "d":
            virando = D

        else:
            return "Erro, parametro errado no alterar_sentido"

        # EFETUAR CALCULO
        novo_sentido = atual + virando
        # print(novo_sentido)

        # VALIDAR NOVO SENTIDO
        # REMOVER OBSTÁCULO
        if novo_sentido in N:
            self.head_pointer = "n"
            self.vsensor[2] = False

        elif novo_sentido in S:
            self.head_pointer = "s"
            self.vsensor[2] = False

        elif novo_sentido in L:
            self.head_pointer = "l"
            self.vsensor[2] = False

        elif novo_sentido in O:
            self.head_pointer = "o"
            self.vsensor[2] = False

    def andar(self):
        if self.head_pointer == "n":
            obstaculo = self.ambiente.mover_norte()

        elif self.head_pointer == "s":
            obstaculo = self.ambiente.mover_sul()

        elif self.head_pointer == "l":
            obstaculo = self.ambiente.mover_leste()

        elif self.head_pointer == "o":
            obstaculo = self.ambiente.mover_oeste()

        self.vsensor[2] = obstaculo
