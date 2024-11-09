import numpy as np
import sympy as sp
def soluciones(columnafinal,tablaInicial,newMatriz):
    indicesColFinal=np.zeros(len(columnafinal))
    indicesColFinal1=np.zeros(len(columnafinal))
    for i in range(len(indicesColFinal)):
        for k in range(tablaInicial.shape[1]):
            if tablaInicial[0,k]==columnafinal[i]:
                indicesColFinal[i]=k-2
                indicesColFinal1[i]=k
    Be=newMatriz[:,[int(indicesColFinal[0]),int(indicesColFinal[1]),int(indicesColFinal[2])]]
    Be_inv=np.linalg.inv(Be)
    Ce=tablaInicial[1,[int(indicesColFinal1[0]),int(indicesColFinal1[1]),int(indicesColFinal1[2])]]
    #Se agrega esta modificación:
    for i in range(len(Ce)):
        if "M" in Ce[i]:
            Ce[i]=0
    for i in range(len(Ce)):
        if "M" not in Ce[i]:
            a=int(float(Ce[i]))*-1
            Ce[i]=a            
    print("C es ",Ce)
    recursos=newMatriz[:,-1]
    solutions=[]
    for i in range(len(recursos)):
        recursosSp=sp.Matrix(recursos)
        recursosSp[i]='b1'
        newRecursos=sp.Matrix(Be_inv)*recursosSp
        ecuaciones=[]
        for j in range(len(newRecursos)):
            ecu=str(newRecursos[j])
            ecu2= ecu+">0"
            ecuaciones.append(ecu2)
            b1=sp.symbols('b1')            
        solucion = str(sp.solve([sp.sympify(ecuaciones[0]),sp.sympify(ecuaciones[1]),sp.sympify(ecuaciones[2])], b1))
        solutions.append(solucion)
    return solutions,Be_inv,recursos,Ce,indicesColFinal