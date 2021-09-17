import numpy as np
import matplotlib.pyplot as plt

d_all = [0.1, 0.2, 0.3, 0.4, 0.5]


'''
Diese Funktion liest die gegebene Daten, die von Kommata getrennt sind von einer Datei

:param fname: Dateiname
:returns: zwei Array - die x_i u. y_i(siehe Aufgabe) 
'''
def read_data(fname):
    data = np.loadtxt(fname, delimiter=",")
    x_i = data[: , 0]
    y_i = data[: , 1]
    return x_i, y_i

'''
Erstellt die Koeffizientennmatrix A 
durch gegebene Formel: y_i = a*e**d*x_i + b*e**(-d)*x_i + c (siehe Aufgabe)

:param arr: Das eingegebene Array
:param d: Das eingegebene d
:returns: numpy.array - Matrix A 
'''
def make(arr, d):
    a1 = np.exp(d*arr)
    a2 = np.exp(-d *arr)
    a3 = np.ones(len(arr))
    A = np.array([a1, a2, a3])
    return A


'''
Diese Funktion findet die Loesung des Quadratmittel-Problems mithilfe QR-Zerlegung 
Wenn Vollrangbedienung nicht erfuellt ist, dann ValueError
:param arr1: Matrix A
:param arr2: Matrix b
:returns: numpy.array - Loesung des Quadratittel-Problems
'''
def lq(arr1, arr2):
    if np.linalg.matrix_rank(arr1) > np.ma.size(arr1, 1):
        raise ValueError('Vollrangbidienung ist nich erfuellt')
    arr1 = arr1.T
    arr2 = arr2.T
    Q, R = np.linalg.qr(arr1)#QR Zerlegung
    Qb = np.dot(Q.T, arr2.T)#
    parameters = np.linalg.solve(R, Qb)
    return parameters


'''
Erstellt eine png-Datei mit graphische Darstellung der Loesung des Quadratmittel-Problems 
in Abhaengigkeit von d's
:param fname: Dateiname
:param a, b, c: -- die gefundene Parameter
:param d: Das eingegebene d
:param arr1: das eingegebene Array - x_i
:param arr2: das eingegebene Array - y_i
'''
def graph(fname, a, b, c, d, arr1, arr2):#die gegebene Funktion
    x_i = arr1
    y_i = arr2
    def f(x_i, a, b, c, d):
        return a * np.exp(d * x_i) + b * np.exp(-d * x_i) + c
    fig = plt.figure(fname)
    plt.plot(x_i, y_i, 'k.')
    plt.plot(x_i, f(x_i, a, b, c, d), label='d=' + str(d))
    plt.legend()
    plt.show()
    fig.savefig(fname)

'''
Diese Funktion berechet das Residiuum r = A*x - b
:param arr1: das eingegebene Array - Matrix A
:param arr2: das eingegebene Array - Matrix x
:param arr3: das eingegebene Array - Matrix b
:returns: a - das Residiuum, b - der Norm des Residiuums
'''
def residual(arr1, arr2, arr3):
    arr1 = arr1.T
    arr3=arr3.T
    a = np.dot(arr1, arr2)
    a = np.subtract(a, arr3)
    b = np.linalg.norm(a)
    return a, b

'''
Diese Funktion berechet Differenz zw. cond(A) u. cond(A-transponierte*A)
:param arr: das eingegebene Array - A
:returns: Differenz
'''
def cond_delta(arr):
    a = np.linalg.norm(np.linalg.pinv(arr))
    b = np.linalg.norm(arr)
    g = a*b
    c = np.dot(arr.T, arr)
    a = np.linalg.norm(np.linalg.pinv(c))
    b = np.linalg.norm(c)
    f = a*b
    return(abs(g-f))



'''Die main- Funktion'''
def main():


    print('run_1')#'normale' Eingangsdatei
    x_i, y_i = read_data('input1.txt')
    for d in d_all:
        A = make(x_i, d)
        params = lq(A, y_i)
        a = params[0]
        b = params[1]
        c = params[2]
        e, f = residual(A, params, y_i)
        print('residual:', e)
        print('norm of residual', f)
        print('delta_condition', cond_delta(A))
        graph('run1', a, b, c, d, x_i, y_i)


    x_i, y_i = read_data('input2.txt')#gerundete Eingansdatei
    print('run_2')
    for d in d_all:
        A = make(x_i, d)
        params = lq(A, y_i)
        a = params[0]
        b = params[1]
        c = params[2]
        e, f = residual(A, params, y_i)
        print('residual:', e)
        print('norm of residual', f)
        print('delta_condition', cond_delta(A))
        graph('run2', a, b, c, d, x_i, y_i)

    x_i, y_i = read_data('input3.txt')#Teilmenge der gegebenen Datei
    print('run_3')
    for d in d_all:
        A = make(x_i, d)
        params = lq(A, y_i)
        a = params[0]
        b = params[1]
        c = params[2]
        e, f = residual(A, params, y_i)
        print('residual:', e)
        print('norm of residual', f)
        print('delta_condition', cond_delta(A))
        graph('run3', a, b, c, d, x_i, y_i)


if __name__ == "__main__" :
    main()





