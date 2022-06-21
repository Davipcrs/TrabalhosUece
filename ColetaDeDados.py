import freq
import numpy as np
import intclasses
import mdvardes
import MonteCarlo as mc

sis1 = [12, 33, 8, 18, 27, 32, 28, 5, 11, 13,
        15, 5, 9, 23, 21, 5, 23, 12, 18, 21,
        9, 17, 9, 11, 14, 32, 15, 19, 30, 26,
        34, 22, 15, 10, 9, 29, 22, 6, 9, 31,
        19, 22, 34, 33, 32, 23, 27, 17, 7, 17,
        31, 12, 23, 6, 34, 26, 26, 30, 7, 32,
        30, 33, 30, 24, 17, 20, 8, 35, 15, 7,
        20, 13, 20, 23, 17, 24, 9, 7, 10, 8,
        8, 28, 19, 7, 23, 31, 22, 20, 10, 24,
        32, 10, 23, 27, 17, 31, 11, 26, 28, 30]

sis2 = [5, 10, 30, 30, 31, 31, 30, 6, 24, 34,
        20, 27, 7, 23, 23, 14, 26, 35, 18, 30,
        22, 32, 12, 34, 25, 7, 22, 30, 14, 22,
        26, 5, 34, 30, 13, 33, 34, 10, 11, 34,
        24, 24, 9, 10, 22, 22, 27, 34, 25, 20,
        22, 10, 34, 34, 5, 15, 6, 17, 23, 19,
        30, 22, 12, 31, 10, 15, 9, 25, 16, 32,
        13, 20, 13, 29, 27, 34, 16, 29, 28, 6,
        34, 12, 9, 23, 18, 31, 20, 6, 8, 27,
        18, 24, 12, 31, 27, 23, 17, 27, 25, 21]

print("================================================================")
print("Tabela Sistema 1 sem estar ordenado\n", sis1)
print("================================================================")
print("Tabela Sistema 2 sem estar ordenado\n", sis2)
print("================================================================")
print("\n")



sis1.sort()
sis2.sort()

print("================================================================")
print("Tabela Sistema 1 ordenada\n", sis1)
print("================================================================")
print("Tabela Sistema 2 ordenada\n", sis2)
print("================================================================")
print("\n")


##descobrir a frequencia:
sis1Aux = sis1
sis2Aux = sis2
sis1freq = []
sis2freq = []

##dependendo da frequencia
sis1Aux, sis1freq = freq.tableclass(sis1)
sis2Aux, sis2freq = freq.tableclass(sis2)




print("================================================================")
print("Tabela Sistema 1 sem repetição\n", sis1Aux)
print("Frequência Tabela 1\n", sis1freq)
print("================================================================")
print("Tabela Sistema 2 sem repetição\n", sis2Aux)
print("Frequência Tabela 2\n", sis2freq)
print("================================================================")
print("\n")


##Com a funcao temos ambas as tabelas
##Sem repeticao e de frequencia
##Calcular a quantidade de classes e os intervalos
##o N da formula é igual a 100

k = 1 + np.log2(100)
k = np.ceil(k)
print("================================================================")
print("Nosso número de classes máximo será", k)
print("================================================================")
print("\n")

##Temos o valor de k
##k = 8
##Vamos agora calcular os intervalos:


print("================================================================")
intSis1 = (sis1Aux[sis1Aux.__len__()-1] - sis1Aux[0])/k
print("Intervalo de classes do sistema 1: ", intSis1)
print("================================================================")
intSis2 = (sis2Aux[sis2Aux.__len__()-1] - sis2Aux[0])/k
print("Intervalo de classes do sistema 2: ", intSis2)
print("================================================================")
print("\n")

##Agora vamos montar a tabela com o intervalo de classes

sis1Inter = intclasses.intclasses(intSis1, sis1Aux)
sis2Inter = intclasses.intclasses(intSis2, sis2Aux)

sis1modf = intclasses.modfreq(sis1freq, sis1Aux, sis1Inter)
sis2modf = intclasses.modfreq(sis2freq, sis2Aux, sis2Inter)

print("----------------------------------------------------------------")
print("RESPOSTA ITEM A): ")
print("----------------------------------------------------------------")
print("\n")
print("================================================================")
print("Tabela 1 em intervalos de classe\n")
intclasses.printinttable(sis1Inter, sis1modf, sis1Aux)
print("================================================================")
print("Tabela 2 em intervalos de classe\n")
intclasses.printinttable(sis2Inter, sis2modf, sis2Aux)
print("================================================================")
print("\n")



sis1mediaAr = mdvardes.mediaAr(sis1Aux, sis1freq)
sis1variancia = mdvardes.variancia(sis1, sis1mediaAr)
sis1desvioP = mdvardes.desvioP(sis1variancia)


sis2mediaAr = mdvardes.mediaAr(sis2Aux, sis2freq)
sis2variancia = mdvardes.variancia(sis2, sis2mediaAr)
sis2desvioP = mdvardes.desvioP(sis2variancia)

print("----------------------------------------------------------------")
print("RESPOSTA ITEM B): ")
print("----------------------------------------------------------------")
print("\n")
print("================================================================")
print("Média (Aritmética), variância e desvio padrão, respectivamente, da tabela 1:")
print(sis1mediaAr)
print(sis1variancia)
print(sis1desvioP)
print("================================================================")
print(sis2mediaAr)
print(sis2variancia)
print(sis2desvioP)
print("================================================================")
print("\n")


nteste = mdvardes.tamanhoAmostraSemDesvio(100, 0.10, 0.5, 1.65)
nSis1 = mdvardes.tamAmsDes(sis1variancia)
nSis2 = mdvardes.tamAmsDes(sis2variancia)


nteste = np.ceil(nteste)
nSis1 = np.ceil(nSis1)
nSis2 = np.ceil(nSis2)
##fazer os prints
print("----------------------------------------------------------------")
print("RESPOSTA ITEM C): ")
print("----------------------------------------------------------------")
print("\n")
print("================================================================")
print("Tamanho da amostra sem utilizar a variancia de dados:")
print(nteste)
print("================================================================")
print("Tamanho da amostra do sistema 1 e sistema 2, respectivamente:")
print(nSis1)
print(nSis2)
print("================================================================")
print("\n")

Sis1Int1, Sis1Int2 = mdvardes.intervalo(sis1mediaAr, sis1desvioP, nSis1)
Sis2Int1, Sis2Int2 = mdvardes.intervalo(sis2mediaAr, sis2desvioP, nSis2)
Sis1Int1 = np.floor(Sis1Int1)
Sis1Int2 = np.ceil(Sis1Int2)
Sis2Int1 = np.floor(Sis2Int1)
Sis2Int2 = np.ceil(Sis1Int2)


print("----------------------------------------------------------------")
print("RESPOSTA ITEM D): ")
print("----------------------------------------------------------------")
print("\n")
print("================================================================")
print("Intervalo de confiança do Sistema 1, usando a amostra = 45: ")
print(Sis1Int1, Sis1Int2)
print("================================================================")
print("Intervalo de confiança do Sistema 2, usando a amostra = 45: ")
print(Sis2Int1, Sis2Int2)
print("================================================================")
print("\n")


sis1Sim = mc.sim(Sis1Int1, Sis1Int2)
sis2Sim = mc.sim(Sis2Int1, Sis2Int2)

sis1SimMed = mdvardes.media(sis1Sim)
sis2SimMed = mdvardes.media(sis2Sim)

sis1Sim.sort()
sis2Sim.sort()


sis1SimAux, sis1SimFreq = freq.freqSim(sis1Sim)
sis2SimAux, sis2SimFreq = freq.freqSim(sis2Sim)

sis1SimInterAux = sis1Inter
sis2SimInterAux = sis2Inter

sis1SimInterFreq = intclasses.modfreq(sis1SimFreq, sis1SimAux, sis1SimInterAux)
sis2SimInterFreq = intclasses.modfreq(sis2SimFreq, sis2SimAux, sis2SimInterAux)

print("----------------------------------------------------------------")
print("RESPOSTA ITEM E): ")
print("----------------------------------------------------------------")
print("\n")
print("================================================================")
print("Tabela de intevalo de classe da simulação dentro do intervalo de confiança do Sistema 1:\n")
intclasses.printinttable(sis1SimInterAux, sis1SimInterFreq, sis1Aux)
print("================================================================")
print("Tabela de intevalo de classe da simulação dentro do intervalo de confiança do Sistema 2:\n")
intclasses.printinttable(sis2SimInterAux, sis2SimInterFreq, sis2Aux)
print("================================================================")
print("\n")


print("----------------------------------------------------------------")
print("RESPOSTA ITEM F): ")
print("----------------------------------------------------------------")
print("\n")
print("================================================================")
print("Percebemos que o Sistema 1(Rede A), possui médias, variâncias e desvios padrões menores que o Sistema 2(Rede B).")
print("Após a simulação dos dois sistemas percebemos que o sistema 1 tende e ter pacote de dados um pouco menores que o sistema 2, em que em várias simulações teve pacotes maiores.")
print("Se ambas as redes (sistemas) forem utilizados para o mesmo proposito, chegamos a conclusão que o Sistema 1 tem uma performance melhor que o sistema 2, pois envia as mesmas mensagens em tamanhos menores.")
print("Mas, essa situação só é verdadeira, se e somente se, ambas as redes transmitem os mesmos dados.")
print("================================================================")

