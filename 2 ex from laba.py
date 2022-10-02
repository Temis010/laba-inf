import numpy as np
import sys

'''a=list(map(int,input('введи элементы матрицы A >>> ').split()))
razm_a=tuple(map(int,input('введи размерность матрицы A >>> ').split('*')))
A=np.array(a,int)#переделываем в одномерный массив(матрица с 1 строкой)
A=A.reshape(razm_a)#придаем нужные размеры

b=list(map(int,input('введи элементы матрицы B >>> ').split()))
razm_b=tuple(map(int,input('введи размерность матрицы B >>> ').split('*')))
B=np.array(b,int)
B=B.reshape(razm_b)

X=A.T#транспонирование матрицы A
print('A.T = ',X,'\n---------------------------------')

if not(razm_a[1]==razm_b[0]):#проверка на возможность умножения. если нельзя, то прога вылетает
    print('размерность играет роль')
    sys.exit(0)
    
X=np.dot(A,B)#умножение матриц
print('A*B = ',X,'\n---------------------------------')'''


c=list(map(int,input('введи элементы матрицы C >>> ').split()))
razm_c=tuple(map(int,input('введи размерность матрицы C >>> ').split('*')))
C=np.array(c,int)
C=C.reshape(razm_c)

rank_C=np.linalg.matrix_rank(C)#нахождение ранга матрицы
print('rank C = ',rank_C)
