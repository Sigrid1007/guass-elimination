import numpy as np
class Matrix():

    def __init__(self,M):
        self.shape=len(M)
        self.R=np.linalg.matrix_rank(M)
        self.det=np.linalg.det(M)
        self.inv=np.linalg.inv(M)


    def gs(self):
        n = len(M)
        x = np.zeros(n)
        for k in range(1, 1000, 1):
            e = 0
            for i in range(n):
                sum = 0
                xb = x[i]
                for j in range(n):
                    if (j != i):
                        sum = sum + M[i][j] * x[j]
                x[i] = (b[i] - sum) / M[i][i]
                e = e + abs(x[i] - xb)
            if (e / n < 0.0001):
                break
        print('k.no.=', k)
        print(x)







if __name__ == '__main__':
    M=[[36,9],[5,8]]
    b=[1,3]
    A=Matrix(M)
    print(A.R)
    print(A.gs())
    print(A.inv)

    X=np.random.randint(10,size=(3,3))
    print(X)
    X=Matrix(M)
    print(X.R)




