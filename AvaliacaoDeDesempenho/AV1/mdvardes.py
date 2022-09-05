def media(vecOrd):
    listsum = sum(vecOrd)
    aux = listsum/(vecOrd.__len__())

    return aux


def mediaAr(vecMod, freq):
    i = 0
    aux = 0
    auxDiv = 0    
    while i < vecMod.__len__():
        aux = aux + (vecMod[i] * freq[i])

        
        auxDiv = auxDiv + freq[i]
        i = i + 1
    
    return aux/auxDiv


def variancia(vec, media):
    i = 0
    aux = 0
    auxDiv = vec.__len__()
    while i < vec.__len__():
        aux = aux + (vec[i]-media)**2
        i = i + 1

    return aux/auxDiv

def desvioP(variancia):
    aux = variancia**(1/2)

    return aux



#nao depende da variancia
def tamanhoAmostraSemDesvio(Pop, e, p, z):
    n = 0
   ##Pop seria o nosso N (Tamanho população)

    auxS = ( ( (z**2) * p * (1 - p)) / ((e**2)) )
    auxB = ( 1 + (((z**2) * p * (1-p)) / ((e**2) * Pop) )  )


    n  = auxS/auxB

    return n



#dependendo da variancia
def tamAmsDes(var):
    z = 1.65
    E = 0.10 * 100
    ##E = z *((var / n)**(1/2))
    n = ((z * (var**1/2))/E)**2

    return n


def intervalo(media, des, n):
    z = 1.65
    intervalo1 = media + (z * (des/(n**1/2)))
    intervalo2 = media - (z * (des/(n**1/2)))
    

    return intervalo2, intervalo1