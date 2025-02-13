import matplotlib.pyplot as plt
import time
from quicksort import *


def getExecutionTime(callFunction):
    initTime = time.time()
    callFunction()
    endTime = time.time()
    execTime = endTime - initTime
    print('Duration: {}'.format(execTime))


"""
Outros testes
"""


with open('data.txt', 'r') as f:
    lines = f.readlines()
    i = 0
    timearrEndPartition = []
    timearrinitPartition = []
    timearrCenterPartition = []
    timearrRandomPartition = []
    for line in lines:

        strArray = line.split(
            ' ')
        intArray = [int(string) for string in strArray]
        initTime = time.time()
        quickSort(intArray, 0, len(intArray) - 1, endPartition)
        endTime = time.time()
        execTime = endTime - initTime
        timearrEndPartition.append(int(execTime * (10**5)))

        initTime = time.time()
        intArray = [int(string) for string in strArray]
        quickSort(intArray, 0, len(intArray) - 1, initPartition)
        endTime = time.time()
        execTime = endTime - initTime
        timearrinitPartition.append(int(execTime * (10**5)))

        initTime = time.time()
        intArray = [int(string) for string in strArray]
        quickSort(intArray, 0, len(intArray) - 1, centerPartition)
        endTime = time.time()
        execTime = endTime - initTime
        timearrCenterPartition.append(int(execTime * (10**5)))

        initTime = time.time()
        intArray = [int(string) for string in strArray]
        quickSort(intArray, 0, len(intArray) - 1, randomPartition)
        endTime = time.time()
        execTime = endTime - initTime
        timearrRandomPartition.append(int(execTime * (10**5)))

    print(timearrEndPartition)
    print(timearrinitPartition)
    print(timearrCenterPartition)
    print(timearrRandomPartition)
    f.close()


num_vectors = 51


plt.figure(figsize=(10, 6))
plt.plot(range(1, num_vectors + 1), timearrEndPartition, marker='o',
         linestyle='-', color='b', label="Pivo no final")
plt.plot(range(1, num_vectors + 1), timearrinitPartition, marker='s',
         linestyle='--', color='r', label="Pivo no começo")
plt.plot(range(1, num_vectors + 1), timearrCenterPartition,
         marker='^', linestyle='-.', color='g', label="Pivo no centro")
plt.plot(range(1, num_vectors + 1), timearrRandomPartition,
         marker='d', linestyle=':', color='m', label="Pivo Aleatório")

plt.title("Tempo de Execução por Vetor", fontsize=16)
plt.xlabel("Índice do Vetor", fontsize=14)
plt.ylabel("Tempo de Execução (x10⁻⁵ s)", fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.tight_layout()

plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(range(1, num_vectors + 1), timearrEndPartition,
            marker='o', linestyle='-', color='b', label="Pivo no final")
plt.scatter(range(1, num_vectors + 1), timearrinitPartition,
            marker='s', linestyle='--', color='r', label="Pivo no começo")
plt.scatter(range(1, num_vectors + 1), timearrCenterPartition,
            marker='^', linestyle='-.', color='g', label="Pivo no centro")
plt.scatter(range(1, num_vectors + 1), timearrRandomPartition,
            marker='d', linestyle=':', color='m', label="Pivo Aleatório")

#
plt.title("Tempo de Execução por Vetor", fontsize=16)
plt.xlabel("Índice do Vetor", fontsize=14)
plt.ylabel("Tempo de Execução (x10⁻⁵ s)", fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.tight_layout()

plt.show()
