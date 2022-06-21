def tableclass(vec):
    i = 0
    j = 0
    k = 0
    freq = []
    auxvec = []

    while i != 100:
        freq.append(0)
        if i == 99 and j == 100:
                if vec[i-1] == vec[i]:
                        freq[k] = freq[k] + 1
                else:
                        auxvec.append(vec[i])
                        
                        i = i+ 1
        
        while j != 100:
            if vec[i] == vec[j]:
                freq[k] = freq[k] + 1
                j = j+1

            else:
                auxvec.append(vec[i])
                i = j
                k = k + 1
                break
                

    freq.pop()
    return auxvec, freq


def freqSim(vec):
    vecFreq = []
    vecMod = []
    i = 0
    aux = 0
    while aux != vec.__len__():
        auxC=0
        auxC = vec.count(vec[aux])
        aux = aux + auxC
        vecFreq.append(auxC)
        vecMod.append(vec[aux-1])

    return vecMod, vecFreq

