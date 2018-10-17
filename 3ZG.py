import numpy as np

def ZG(a,b,c,d):
    t=np.transpose(b)
    n=len(t)
    u=np.zeros(n)
    l=np.zeros(n)
    u[0]=b[0]
    for k in range(1,n):
        if(u[k-1]==0):
            D=0
            break
        l[k]=a[k]/u[k-1]
        u[k]=b[k]-l[k]*c[k-1]

    y=np.zeros(n)
    y[0]=d[0]
    for k in range(1,n):
        y[k]=d[k]-l[k]*y[k-1]

    x=np.zeros(n)
    if(u[n-1]==0):
        D=0
    x[n-1]=y[n-1]/u[n-1]
    for k in range(n-2,-1,-1):
        x[k]=(y[k]-c[k]*x[k+1])/u[k]
    print(x)

if __name__ == '__main__':
     a=[0,-1,-1,-1]
     b=[2,2,2,2]
     c=[-1,-1,-1,0]
     d=[1,0,0,0]
     ZG(a,b,c,d)



