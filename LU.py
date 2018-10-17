import numpy as np


def LU(B):
    A = np.array(B)
    n = len(A)
    # print(A)

    L = np.zeros(shape=(n, n))
    U = np.zeros(shape=(n, n))

    for k in range(n - 1):
        a = A[:, k]
        a[k + 1:] = a[k + 1:] / a[k]
        a[0:k + 1] = np.zeros(k + 1)
        # print(gauss_vector)
        L[:, k] = a
        L[k][k] = 1.0
        # print(L)
        # print(A)
        for l in range(k + 1, n):
            B[l, :] = B[l, :] - a[l] * B[k, :]

        A = np.array(B)
    L[k + 1][k + 1] = 1.0
    U = A
    print(U)
    print(L)

if __name__ == '__main__':
    A = np.array([[2., 2., 3.],
                  [4., 7., 7.],
                  [-2., 4., 5.]])
    LU(A)











