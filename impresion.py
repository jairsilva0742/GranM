from sympy import *
from sympy.core.numbers import Float
def imp(matrix):
    
    for i in range(matrix.shape[0]):        
        for j in range(matrix.shape[1]):
            a=(matrix[i,j])
            if isinstance(a, Float):
                a=round(float(Float(a)),1)
            print(" |",a,end="")
            
        print(" "*i)