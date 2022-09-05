import random as rd


#Geração de numeros randomicos 
#para gerar a simulação de Monte Carlo
def sim(int1, int2):
    i = 0
    vec = []
    while i != 50:
        aux = rd.randint(int1, int2)
        vec.append(aux)
        i = i + 1

    return vec







