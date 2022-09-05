#vecOrd = vetor ordenado já relacionado as frequencias.
#VecInt = vetor dos intervalos de classe.

def intclasses(intervalo, vecOrd):
    inttableclass = []
    
    aux = vecOrd[0]
    ##inttableclass.append(aux)
    while aux < vecOrd[vecOrd.__len__()-1]:
        aux = aux + intervalo
        if aux > vecOrd[vecOrd.__len__()-1]:
            inttableclass.append(vecOrd[vecOrd.__len__()-1])
            break

        else:
            inttableclass.append(aux)
    
    return inttableclass


def modfreq(freq, vecOrd, vecInt):
    i = 0
    j = 0
    newFreq = []
    while i < vecInt.__len__():
        ##vetor no intervalo de classes
        newFreq.append(0)
        while j < vecOrd.__len__():
            ##vetor ordenado, sem repeticoes
            if vecOrd[j] <= vecInt[i]:
                newFreq[i] = newFreq[i] + freq[j]
                j = j + 1

            else:
                break
        i = i + 1

    return newFreq

def printinttable(inttable, modfreq, vecOrd):
    i = -1
    j = 0
    print("     Intervalos        ||    Frequência")
    while i < inttable.__len__()-1:
        if i == -1:
            print(vecOrd[0], " |---| ", inttable[0],"        ||    ", modfreq[0]) 
            i = i+1   
            
        else:
            print(inttable[i], " ---| ", inttable[i+1],"     ||    ", modfreq[i+1])
            i = i +1
        







