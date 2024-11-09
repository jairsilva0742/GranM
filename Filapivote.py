from sympy import *
def find(Matrix,indice):
    indexPivote=0
    menor=10000
    for i in range(Matrix.shape[0]-2):
        b=parse_expr(Matrix[i+2,indice])
        
        if b>0:
            a=parse_expr(Matrix[i+2,-1])/parse_expr(Matrix[i+2,indice])
            if a<menor:
                menor=a
                indexPivote=i+2
    return indexPivote