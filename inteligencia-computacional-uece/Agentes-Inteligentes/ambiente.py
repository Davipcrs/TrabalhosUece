class Ambiente():
    def __init__(self, x, y, caminho_ambiente):
        self.x = x
        self.y = y
        self.caminho_ambiente = caminho_ambiente
        self.local = []
        self.__agente_x = 0
        self.__agente_y = 0
        self.carregar_ambiente()

    def getAgenteX(self):
        return self.__agente_x

    def getAgenteY(self):
        return self.__agente_y

    def carregar_ambiente(self):
        """Carrega o ambiente de um arquivo para a variavel local"""
        with open(self.caminho_ambiente, 'r') as ambiente:
            for linha in ambiente:
                aux = []
                for data in linha.split(" "):
                    aux.append(data.replace("\n", ""))
                self.local.append(aux)

        print("Ambiente original: ")
        print(self.local)

    def atualizar_ambiente(self):
        """Limpa o ambiente"""
        self.local[self.__agente_x][self.__agente_y] = 0

    def mover_norte(self):
        if self.__agente_x == 0:
            return True

        self.__agente_x -= 1

        return False

    def mover_sul(self):
        if self.__agente_x == self.x - 1:
            return True

        self.__agente_x += 1

        return False

    def mover_leste(self):
        if self.__agente_y == 0:
            return True

        self.__agente_y -= 1

        return False

    def mover_oeste(self):
        if self.__agente_y == self.y - 1:
            return True

        self.__agente_y += 1

        return False

    def recuperar_informacao_local(self):
        if int(self.local[self.getAgenteX()][self.getAgenteY()]) == 1:
            dirt = True
        else:
            dirt = False
        if self.__agente_x == 0 and self.__agente_y == 0:
            home = True

        else:
            home = False
        return [home, dirt]
