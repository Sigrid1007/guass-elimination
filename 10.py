# test for asdfasdf
#打印矩阵A
def pprint(A):
    n = len(A)
    for i in range(0, n):
        line = ""
        for j in range(0,n+1)
            line += str(A[i][j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")
#高斯消元法
def gauss(A)
    #找主元
    n=len(A)
    for i in range(0,n):
        main_factor=abs(A[i],[i])
        max_row=i
        for k in range(i+1,n):
            if abs(A[k][i])>main_factor:
                main_factor=abs(A[k][i])
                max_row=k
    #判断是否为奇异阵
    if main_factor =0
            break
    else:
        #交换行
        for p in range(i,n+1):
            tmp=A[max_row][p]
            A[max_row][k]=A[i][p]
            A[i],[p]=tmp
        消元
        for j in range(i+1,n):
            c=-A[j][i]/A[i][i]
            for m in range(i,n+1):
                if i==m:
                    A[j][m]=0
                else:
                    A[j][m]+=c*A[i][m]
    #计算x
    x = [0 for i in range(n)]
    for i in range(n-1,-1,-1):
        x[i]=A[i][n]/A[i][i]
        print 
        for k in range(i-1,-1,-1):
            A[k][n]-=A[k][i]*x[i]
    return x
