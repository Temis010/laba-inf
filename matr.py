def matrix(a,m_a,n_a):
    if len(a)==m_a*n_a:
        A=[]
        for m in range(m_a):
            A.append([])
            for n in range(n_a):
                A[m].append(a[m*n_a+n])
        return A
    else:
        print('несоответствие указанного размеров и количества элементов')
            
def transpose(a,m_m,n_n):
    xX=[]
    for n in range(n_n):
        xX.append([])
        for m in range(m_m):
            xX[n].append(a[m*n_n+n])
    return xX

def umn(A,B,m_a,n_a,m_b,n_b):
    if n_a!=m_b:
        print('умножение невозможно')
    else:
        X=[]
        for m in range(m_a):
            X.append([])
            for n in range(n_b):
                new_elem=0
                for i in range(n_a):
                    new_elem+=A[m][i]*B[i][n]
                X[m].append(new_elem)
        return X

def det(x):
    if len(x[0])!=len(x):
        print('неквадратичная матрица!!!')
    else:
        razm=len(x)
        if razm==2:#Логично, что простой случай с размерностью = 2
            return x[0][0]*x[1][1]-x[1][0]*x[0][1]
        elif razm==1:
            return x[0][0]
        else:
            otv=0 #уже сам не знаю, что происходит). Если надо, то при встрече объясню
            for ind in range(razm):
                matr=[]
                for m in range(1,razm):
                    matr.append([])
                    for n in range(razm):
                        if n!=ind:
                            matr[m-1].append(x[m][n])
                otv+=(-1)**(1+ind+1)*(det(matr))*x[0][ind]
            return otv


















    
