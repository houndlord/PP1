from scipy import *
from scipy import linalg
import numpy as np
from scipy.sparse import diags
import matplotlib as plt


class Matrix():
    def __init__(self, mtype, dim, dtype):
        self.mtype = mtype
        self.dim = dim
        self.dtype = dtype
        if mtype == 'hilbert':
            if dtype == 'float16':
                self.matrix = np.array(linalg.hilbert(dim), dtype=np.float16)
                self.inv = np.array(linalg.invhilbert(dim), dtype=np.float16)
            elif dtype == 'float32':
                self.matrix = np.array(linalg.hilbert(dim), dtype=np.float32)
                self.inv = np.array(linalg.invhilbert(dim), dtype=np.float32)
            elif dtype == 'float64':
                self.matrix = np.array(linalg.hilbert(dim), dtype=np.float64)
                self.inv = np.array(linalg.invhilbert(dim), dtype=np.float64)
        elif mtype =='saite':
            k = np.array([(-1) * np.ones(dim - 1), 2 * np.ones(dim), (-1) * np.ones(dim - 1)])
            offset = [-1, 0, 1]
            if dtype == 'float16':
                self.matrix  = np.array(diags(k, offset).toarray(), dtype=np.float16)
                self.inv = np.array(linalg.inv(self.matrix), dtype=np.float16)
            elif dtype == 'float32':
                self.matrix = np.array(diags(k, offset).toarray(), dtype=np.float32)
                self.inv = np.array(linalg.inv(self.matrix), dtype=np.float32)
            elif dtype == 'float64':
                self.matrix = np.array(diags(k, offset).toarray(), dtype=np.float64)
                self.inv = np.array(linalg.inv(self.matrix), dtype=np.float64)


    def solve(self, b):
        n = 5
        k = np.array([(-1) * np.ones(n - 1), 2 * np.ones(n), (-1) * np.ones(n - 1)])
        offset = [-1, 0, 1]
        A = diags(k, offset).toarray()
        m, n = shape(A)
        for i in arange(0, n):
            pivot = A[i, i]
            for k in arange(i + 1, n):
                A[k, i] = A[k, i] / pivot
                A[k, i + 1:n] = A[k, i + 1:n] - A[k, i] * A[i, i + 1:n]
        L = eye(n) + tril(A, -1)
        U = triu(A)
        y = np.zeros(b.size)
        for i, j in enumerate(b.flatten()):
            y[i] = j
            if i:
                for n in xrange(i):
                    y[i] -= y[n] * L[i, n]
        y[i] /= L[i, i]

        x = np.zeros(b.size)
        lastidx = b.size - 1  # last index
        for iidx in xrange(b.size):
            i = b.size - 1 - iidx  # backwards index
            x[i] = y[i]
            if iidx:
                for jidx in xrange(iidx):
                    j = b.size - 1 - jidx
                    x[i] -= x[j] * U[i, j]
        x[i] /= U[i, i]
        return(x)










def main():
    def condition(a):
        b = a.matrix
        a = np.linalg.norm(a.matrix)
        c = np.linalg.norm(b)
        return a*c


if __name__ == "__main__":
    main()