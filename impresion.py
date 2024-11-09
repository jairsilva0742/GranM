from sympy import *
from sympy.core.numbers import Float
def imp(matrix):
    
    for i in range(matrix.shape[0]):        
        for j in range(matrix.shape[1]):
            a=(matrix[i,j])
            if isinstance(a, Float):
                a=round(float(Float(a)),1)
            print(" |",a,end="")
            """if len(a)==13:
                print(" |",a,end="")
            if len(a)==12:
                print(" | ",a,end="")
            if len(a)==11:
                print(" |  ",a,end="")
            if len(a)==10:
                print(" |   ",a,end="")
            if len(a)==9:
                print(" |    ",a,end="")
            if len(a)==8:
                print(" |     ",a,end="")
            if len(a)==7:
                print(" |      ",a,end="")
            if len(a)==6:
                print(" |       ",a,end="")
            if len(a)==5:
                print(" |        ",a,end="")
            if len(a)==4:
                print(" |         ",a,end="")
            if len(a)==3:
                print(" |          ",a,end="")
            if len(a)==2:
                print(" |           ",a,end="")
            if len(a)==1:
                print(" |            ",a,end="")"""
            
        print(" "*i)