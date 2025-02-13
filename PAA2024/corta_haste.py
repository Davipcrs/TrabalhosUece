import math


def corta_haste(p: list, n: int):
    if (n == 0):
        return 0

    auxiliar = - math.inf
    i = 0
    while i < n:
        # print(i)
        # print(p[i])
        i = i + 1
        auxiliar = max(auxiliar, p[i-1] + corta_haste(p, n - i))

    return auxiliar


print(corta_haste([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 10))
