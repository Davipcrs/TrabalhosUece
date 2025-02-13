from random import randint
from agente import Agente


class AgenteReativo1(Agente):
    def definir_acao(self):
        self.perceber()
        # self.salvar_historico("perceber", None)

        if self.vsensor[1] == True:
            self.limpar()
            self.pontuacao = self.pontuacao + 1
            self.pontuacao_v2 = self.pontuacao_v2 + 1
            self.salvar_historico("limpar", None)

        if self.vsensor[1] == False:
            rand = randint(0, 100)

            if self.vsensor[2] == True:
                if rand < 45:
                    self.pontuacao_v2 = self.pontuacao_v2 - 1
                    self.alterar_sentido("e")
                    self.salvar_historico("alterar sentido", "e")

                if rand >= 45 and rand <= 90:
                    self.pontuacao_v2 = self.pontuacao_v2 - 1
                    self.alterar_sentido("e")
                    self.salvar_historico("alterar sentido", "d")

                if rand > 90 and rand <= 100:
                    if self.vsensor[0] == True:
                        self.salvar_historico("Retornar a HOME", None)
                        return 'HOME'

            elif rand <= 20:
                self.pontuacao_v2 = self.pontuacao_v2 - 1
                self.alterar_sentido("e")
                self.salvar_historico("alterar sentido", "e")

            elif rand > 20 and rand <= 40:
                self.pontuacao_v2 = self.pontuacao_v2 - 1
                self.alterar_sentido("d")
                self.salvar_historico("alterar sentido", "d")

            elif rand > 40 and rand <= 90:
                self.pontuacao_v2 = self.pontuacao_v2 - 1
                self.andar()
                self.salvar_historico("andar", None)

            elif rand > 90 and rand <= 100:
                if self.vsensor[0] == True:
                    self.salvar_historico("Retornar a HOME", None)
                    return 'HOME'

        return super().definir_acao()
