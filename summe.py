import math
import numpy as np


'''
Diese Funktion berechnet die Summe von ausgewaehlten Reihe
:param n: Anzahl von Summanden
:param a: die Serie(harmonische, Talor1, Taylor2)
:paramc: "normale" oder getrennte summierung
:returns: float, die Summe
'''
def sum(n, a, b, c):

    if a == 1:#Reihegenerator, A - Reihe
        if b == 1:
            A = [1 / np.float16(i) for i in range(1, n + 1)]
        elif b == 2:
            A = [1 / np.float32(i) for i in range(1, n + 1)]
        elif b == 3:
            A = [1 / np.float64(i) for i in range(1, n + 1)]
    elif a == 2:
        if b == 1:
            A = [n ** np.float16(i) / math.factorial(i) for i in range(1, n + 1)]
        elif b == 2:
            A = [n ** np.float32(i) / math.factorial(i) for i in range(1, n + 1)]
        elif b == 3:
            A = [n ** np.float64(i) / math.factorial(i) for i in range(1, n + 1)]
    elif a == 3:
        if b == 1:
            A = [(-1) ** np.float16(i) * n ** np.float16(i) / math.factorial(i) for i in range(1, n + 1)]
        elif b == 2:
            A = [(-1) ** np.float32(i) * n ** np.float32(i) / math.factorial(i) for i in range(1, n + 1)]
        elif b == 3:
            A = [(-1) ** np.float64(i) * n ** np.float32(i) / math.factorial(i) for i in range(1, n + 1)]
    if c == 1:  # Berechnung die Summe
        if a == 1 or 2:
            if b == 1:
                f = np.sum(A, dtype=np.float16)

            elif b == 2:
                f = np.sum(A, dtype=np.float32)
            elif b == 3:
                f = np.sum(A, dtype=np.float64)
        elif a == 3:
            if b == 1:
                f = (np.sum(A, dtype=np.float16)) ** (-1)
            elif b == 2:
                f = (np.sum(A, dtype=np.float32)) ** (-1)
            elif b ==3:
                f = (np.sum(A, dtype=np.float32)) ** (-1)

    elif c == 2:
        A.sort()
        d = 0
        for i in range(0, len(A)):
            if A[i] > 0:
                d = i
            break
        g = A[d:]
        e = A[0:d]
        if b == 1:
            f = np.sum(g, dtype=np.float16) + np.sum(e, dtype=np.float16)
        elif b == 2:
            f = np.sum(g, dtype=np.float32) + np.sum(e, dtype=np.float32)
        elif b == 3:
            f = np.sum(g, dtype=np.float64) + np.sum(e, dtype=np.float64)
    return f


'''
Diese Funktion berechnet die Summe von ausgewaehlten Reihe
:param n: Anzahl von Summanden
:param a: die Serie(harmonische, Talor1, Taylor2)
:paramc: "normale" oder getrennte summierung
:returns: float, die Summe
'''
def abw(a, n, f):
    if a == 1:
        if n == 1:
            k = f - float(1)
        elif n == 2:
            k = f - float(3) / 2
        elif n == 3:
            k = f - float(11) / 6
        elif n == 4:
            k = f - float(25) / 12
        elif n == 5:
            k = f - float(137) / 607

        elif n == 6:
            k = f - float(49) / 20
        elif n == 7:
            k = f - float(363) / 140
        elif n>7:
            k = 'rerr'
    elif a == 2:
        k = f - math.e ** n
    elif a == 3:
        k = f - (1 / math.e ** (-n))
    list1 = [1, 2, 3, 4, 5, 6, 7]
    return k


'''Die main-Funktion'''
def main():
    while True:#Eingabe
        try:
            n = input("Please enter k: ")
            n = int(n)
            if n < 0 or n == 0:
                print('n should be larger as 0')
                continue
            break
        except ValueError:
            print
            "invalid value"

    while True:
        liste = [1, 2]
        try:
            c = input('''Please choose a sum type:
            1 - normal
            2 - separate sum
                ''')
            c = int(c)
            if c not in liste:
                print('n should be 1 or 2')
                continue
            break
        except ValueError:
            print
            "invalid value"
    while True:
        liste = [1, 2, 3]
        try:
            a = input('''Please choose a sequence:
            1 - harmonic series
            2 - taylor series
            3 - tylor series for 1/e**n''')
            a = int(a)
            if a not in liste:
                print('n schould be 1, 2 or 3')
                continue
            break
        except ValueError:
            print
            "invalid value"
    while True:
        liste = [1, 2, 3]
        try:
            b = input('''Choose type 
            1 - np.float16
            2 - np.float32
            3 - np.float64''')
            b = int(b)
            if b not in liste:
                print('n schould be 1, 2 or 3')
                continue
            break
        except ValueError:
            print
            "invalid value"
    f = sum(n, a, b, c)
    if math.isinf(f)==True:
        print("OverflowError, n is too high")
    else:
        print(f)
        g = abw(a, n, f)
        print(g)

if __name__ == "__main__":
    main()
