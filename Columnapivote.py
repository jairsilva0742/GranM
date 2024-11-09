from sympy import *

def find(Matrix,minimizar):
    indexMax=[]
    M=symbols("M")
    if minimizar:
        maximo=-5000
        for i in range(Matrix.shape[1]-2):
            a=parse_expr(Matrix[1,i+1]).subs(M,5000)
            if a>maximo:
                maximo=a
                indexMax=i+1
    else:
        minimo=5000
        for i in range(Matrix.shape[1]-2):
            a=parse_expr(Matrix[1,i+1]).subs(M,5000)
            if a<minimo:
                minimo=a
                indexMax=i+1
    print(indexMax)
    return indexMax
