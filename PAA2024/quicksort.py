"""
// @DOCSTART
// ## quicksort.py  @NL
// Escrito Por: Davi Coelho  @NL
// Data: 09/01/2025  @NL
//  @NL
// Implementação QuickSort com diversas funções de Partições.  @NL
// @DOCEND
"""


"""
// @DOCSTART
// ### Funções de Partição:  @NL
// initPartition  @NL
// endPartition (Default)  @NL
// randomPartition  @NL
// certerPartition  @NL
// ### Função Principal:  @NL
// quickSort (Principal do arquivo)  @NL
// @DOCEND
"""




from math import ceil
from random import randint
import sys
def initPartition(arr, left, right):
    pivot = arr[left]

    changeIndexLeft = left + 1  # Pq o Left já é o Pivô
    changeIndexRight = right  # Pq vai ser necessário fazer uma 'comparação dupla'

    while True:
        # It indicates we have already moved all the elements to their correct side of the pivot
        while changeIndexLeft <= changeIndexRight and arr[changeIndexRight] >= pivot:
            changeIndexRight = changeIndexRight - 1

        # Opposite process
        while changeIndexLeft <= changeIndexRight and arr[changeIndexLeft] <= pivot:
            changeIndexLeft = changeIndexLeft + 1

        # Case in which we will exit the loop
        if changeIndexLeft <= changeIndexRight:
            _changePosHelper(arr=arr, goal=changeIndexLeft,
                             start=changeIndexRight)
        else:
            # We exit out of the loop
            break

    _changePosHelper(arr=arr, goal=changeIndexRight, start=left)
    # arr[left], arr[changeIndexRight] = arr[changeIndexRight], arr[left]
    # As we got pivot element index is end
    # now pivot element is at its sorted position
    # return pivot element index (end)
    return changeIndexRight


def endPartition(arr, left, right):
    pivot = arr[right]
    changeIndex = left - 1
    for checkIndex in range(left, right):
        if arr[checkIndex] <= pivot:
            changeIndex = changeIndex + 1
            _changePosHelper(arr=arr, start=checkIndex, goal=changeIndex)

    _changePosHelper(arr=arr, goal=changeIndex+1, start=right)
    # arr[changeIndex+1], arr[right] = arr[right], arr[changeIndex+1]
    return changeIndex+1


def randomPartition(arr, left, right):
    randomValue = randint(left, right)
    pivot = arr[randomValue]

    _changePosHelper(arr=arr, goal=left, start=randomValue)
    return endPartition(arr=arr, left=left, right=right)


def centerPartition(arr, left, right):

    pivot = arr[(left + right) // 2]
    # print("pivot inicial: pos, value", ((left + right) // 2), pivot)
    _changePosHelper(arr=arr, goal=left, start=(left + right) // 2)
    changeIndexLeft = left
    changeIndexRight = right

    while (changeIndexLeft < changeIndexRight):
        # Lê da esquerda para direita
        while changeIndexLeft <= changeIndexRight and arr[changeIndexLeft] <= pivot:
            changeIndexLeft = changeIndexLeft + 1

        # Lê da direita para a esquerda
        while changeIndexLeft <= changeIndexRight and arr[changeIndexRight] >= pivot:
            changeIndexRight = changeIndexRight - 1

        # Troca o da direita com o da esquerda
        if (changeIndexLeft < changeIndexRight):
            _changePosHelper(arr=arr, goal=changeIndexRight,
                             start=changeIndexLeft)
        else:
            break
    _changePosHelper(arr=arr, goal=changeIndexRight, start=left)
    # arr[left], arr[changeIndexLeft] = arr[changeIndexLeft], arr[left]
    # return (left + right) // 2
    return changeIndexRight


def _changePosHelper(arr, start, goal):
    # print("swap: [pos, value]", goal, arr[goal], start, arr[start])
    arr[goal], arr[start] = arr[start], arr[goal]
    return


# // @DOCSTART
# // @CBS python
def quickSort(arr: list, left: int, right: int, partitionFunction=endPartition):
    # print('left: ', left)
    # print('right: ', right)
    if left < right:
        pivotIndex = partitionFunction(arr, left, right)
        # print('pivot: ', pivotIndex)
        quickSort(arr=arr, left=left, right=pivotIndex -
                  1, partitionFunction=partitionFunction)
        quickSort(arr=arr, left=pivotIndex+1, right=right,
                  partitionFunction=partitionFunction)


# // @CBE
# // @NL
# // @DOCEND


def test(inputArray: str):
    strArray = inputArray.split(
        ' ')
    intArray = [int(string) for string in strArray]
    # generated = generateArray()
    # intArray = generated
    print("Init State")
    print(intArray)

    print("Random Partition")
    quickSort(intArray, 0, len(intArray) - 1, randomPartition)
    print(intArray)

    intArray = [int(string) for string in strArray]
    # intArray = generated
    quickSort(intArray, 0, len(intArray) - 1, endPartition)
    print("End Partition")
    print(intArray)

    intArray = [int(string) for string in strArray]
    # intArray = generated
    quickSort(intArray, 0, len(intArray) - 1, initPartition)
    print("Init Partition")
    print(intArray)

    intArray = [int(string) for string in strArray]
    # intArray = generated
    quickSort(intArray, 0, len(intArray) - 1, centerPartition)
    print("Center Partition")
    print(intArray)


def runTests():
    print(sys.getrecursionlimit())
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        i = 0
        for line in lines:

            print("new exec, num: ", i)

            test(str(line))

            print("\n\n\n")
            i = i + 1
        f.close()


def generateArray():
    import random
    array = random.sample(range(1_000_000), 100_000)

    print(array)
    return array
