

from random import randint
from agente import Agente


class AgenteModelo1(Agente):
    def definir_acao(self):
        self.perceber()
        r = self.criar_modelo()

        if self.vsensor[1] == True:
            self.limpar()
            self.pontuacao = self.pontuacao + 1
            self.pontuacao_v2 = self.pontuacao_v2 + 1
            self.salvar_historico("limpar", None)

        if self.vsensor[0] == True and self.counter != 0:
            self.salvar_historico("Retornar a HOME", None)
            return 'HOME'

        if self.vsensor[1] == False:

            if r == 1:
                self.pontuacao_v2 = self.pontuacao_v2 - 1
                self.andar()
                self.salvar_historico("andar", None)

            elif r == 'e':
                self.pontuacao_v2 = self.pontuacao_v2 - 1
                self.alterar_sentido("e")
                self.salvar_historico("alterar sentido", "e")

            elif r == 'd':
                self.pontuacao_v2 = self.pontuacao_v2 - 1
                self.alterar_sentido("d")
                self.salvar_historico("alterar sentido", "d")

    def criar_modelo(self):
        """Responsável por criar o modelo"""
        # Tentativa de criar um modelo circular, sem aprendizado.
        check_vsensor_index_2 = self.vsensor[2]
        if check_vsensor_index_2 == False:
            return 1
        else:
            if self.counter % 2 == 0 and self.head_pointer == 's':
                self.counter = self.counter + 1
                return 'e'
            elif self.head_pointer == 'o':
                self.counter = self.counter + 1
                return 'e'
            elif self.counter % 2:
                self.counter = self.counter + 1
                return 'd'
            else:
                self.counter = self.counter + 1
                return 'e'
