from sympy import *

def comprobar(Matrix,minimizar):
    M=symbols("M")
    stop=False
    if minimizar:
        print("minimizar")
        for i in range(Matrix.shape[1]-3):
            a=parse_expr(Matrix[1,i+2]).subs(M,5000)            
            if a<0:
                stop=True               
            elif a==0:
                stop=True
            else:
                stop=False
                break
    else:
        print("maximizar")
        for i in range(Matrix.shape[1]-3):
            a=parse_expr(Matrix[1,i+2]).subs(M,5000)           
            if a>0:
                stop=True               
            elif a==0:
                stop=True                
            else:
                stop=False               
                break
    return stop
