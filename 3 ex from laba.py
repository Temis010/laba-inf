import timeit
import matr
import numpy as np

startTime=timeit.default_timer()

x=list(map(int,input('введи элементы матрицы >>> ').split()))
m_x,n_x=map(int,input('введи размерность матрицы >>> ').split('*'))
X=matr.transpose(x,m_x,n_x)
det_X=matr.det(X)

Xx=matr.transpose(x,m_x,n_x)

for m in range(n_x):
    for n in range(m_x):
        x_vr=[]
        k=0
        for i in range(n_x):
            if i!=m:
                x_vr.append([])
                for j in range(m_x):
                    if j!=n:
                        x_vr[k].append(X[i][j])
                k+=1
        Xx[m][n]=((-1)**(m+n)*(matr.det(x_vr)))/det_X

print(Xx)

startTime1=timeit.default_timer()
midTime=timeit.default_timer()

x=list(map(int,input('введи элементы матрицы A >>> ').split()))
razm_x=tuple(map(int,input('введи размерность матрицы A >>> ').split('*')))
X=np.array(x,int)
X=X.reshape(razm_x)
Obr=np.linalg.inv(X)
print(Obr)

endTime=timeit.default_timer()
print(midTime-startTime,endTime-midTime)
print(startTime,midTime,endTime)
