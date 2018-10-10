# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 10:03:45 2017
@author: www
"""

#   python实现LU分解

import numpy as np


def LU(B):
    A = np.array(B)
    n = len(A)
    # print(A)

    L = np.zeros(shape=(n, n))
    U = np.zeros(shape=(n, n))

    for k in range(n - 1):
        C= A[:, k]
        C[k + 1:] = C[k + 1:] / C[k]
        C[0:k + 1] = np.zeros(k + 1)
        # print(gauss_vector)
        L[:, k] = C
        L[k][k] = 1.0
        # print(L)
        # print(A)
        for l in range(k + 1, n):
            B[l, :] = B[l, :] - C[l] * B[k, :]

        A = np.array(B)
    L[k + 1][k + 1] = 1.0
    U = A
    print(U)
    print(L)





