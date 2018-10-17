import numpy as np
def GS(A,b):
    n=len(A)
    x=np.zeros(n)
    for k in range(1, 1000, 1) :
        e=0
        for i in range(n):
            sum=0
            xb=x[i]
            for j in range(n):
                if(j!=i):
                    sum=sum+A[i][j]*x[j]
            x[i]=(b[i]-sum)/A[i][i]
            e=e+abs(x[i]-xb)
        if(e/n<0.0001):
            break
    print('k.no.=',k)
    print(x)

if __name__ == '__main__':
    A=[[4,1,1],[1,4,1],[1,1,4]]
    b=[6,6,6]
    GS(A,b)



