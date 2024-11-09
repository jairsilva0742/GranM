import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
from sympy import *
from sympy.core.numbers import Float
from sympy import Float
from sympy import Rational
import SolFinales,precioSombra,variablesDecision,titulo,Columnapivote,Filapivote,Parada,impresion

def granM(c,d,e,m,entrada1_1,entrada1_2,entrada2_1,entrada2_2,resultado2,entrada3_1,entrada3_2,resultado3,entrada4_1,entrada4_2,resultado4):
    minimizar=m
    #-1 para menor que, 1 para mayor que, 0 para igual y para la funcion Z
    #zeta=np.array([1.5,2.5])
    #zeta=np.array([80,90])
    print(entrada1_1," ",entrada1_2)
    zeta=np.array([entrada1_1,entrada1_2])
    #zeta=np.array([80,90])

    TamZ=len(zeta)
    #r1=np.array([2,1,90,-1])
    #r1=np.array([1,1,30,0])
    r1=np.array([entrada2_1,entrada2_2,resultado2,c])
    #r1=np.array([1,1,30,0])

    #r2=np.array([1,1,50,1])
    #r2=np.array([0.2,0.35,9,1])
    #r2=np.array([1,3,20,1])
    r2=np.array([entrada3_1,entrada3_2,resultado3,d])
    #r2=np.array([0.2,0.35,9,1])

    #r3=np.array([1,0,10,-1])
    #r3=np.array([0.06,0.12,3,-1])
    #r3=np.array([1,1,10,0])
    r3=np.array([entrada4_1,entrada4_2,resultado4,e])
    #r3=np.array([0.06,0.12,3,-1])

    matriz=np.array([r1,r2,r3])
    cont=0
    cont2=0


    for i in range(matriz.shape[0]):
        if matriz[i,matriz.shape[1]-1]==1:
            cont=cont+1
        elif matriz[i,matriz.shape[1]-1]==0:
            cont2=cont2+1

    Columnas=TamZ+matriz.shape[0]+cont

    #En esta parte  se hace el titulo de la tabla simplex
    a=titulo.titulo(TamZ,'x')
    b=titulo.titulo(matriz.shape[0]-cont2,'S')
    c=titulo.titulo(cont+cont2,'A')
    tit=np.concatenate((['VB'],['Z'],a,b,c,['b']))


    zeta=np.concatenate(((-1*zeta),np.zeros(Columnas-len(zeta)+1)))
    zeta=zeta.astype(str)

    for i in range(cont+cont2):
        #dependiendo de si se desea minimizar o no, M adquiere valor negativo en la matriz
        if minimizar:
            zeta[-(i+1)-1]='-M'
        else:
            zeta[-(i+1)-1]='M'

    #acá se colocan los indices en las variables de holgura y aumentadas de acuerdo al caso
    contA=0
    contS=0
    newMatriz=np.zeros((matriz.shape[0],Columnas+1))
    for i in range(matriz.shape[0]):
        for j in range(TamZ):
            newMatriz[i,j]=matriz[i,j]
        
        newMatriz[i,-1]=matriz[i,-2]
        
        if matriz[i,-1]==1:
            newMatriz[i,TamZ+contS]=-1
            newMatriz[i,TamZ+matriz.shape[0]-cont2+contA]=1
            contA=contA+1
            contS=contS+1
        if matriz[i,-1]==0:
            newMatriz[i,TamZ+matriz.shape[0]-cont2+contA]=1
            contA=contA+1
        if matriz[i,-1]==-1:
            newMatriz[i,TamZ+contS]=1
            contS=contS+1
    print(newMatriz)
    tit2=['Z']
    for k in range(newMatriz.shape[0]):
        for i in range(matriz.shape[0]+cont):
            if newMatriz[k,TamZ+i]==1:
                tit2=np.concatenate((tit2,[tit[2+TamZ+i]]))

    newMatriz2=newMatriz.astype(str)
    newMatriz2=np.insert(newMatriz2,[0],zeta,axis=0)

    zeros=np.zeros(matriz.shape[0]+1)
    zeros[0]=1
    zeros=zeros.astype(str)

    newMatriz2=np.insert(newMatriz2,[0],zeros.reshape(-1,1),axis=1)
    newMatriz2=np.insert(newMatriz2,[0],tit2.reshape(-1,1),axis=1)
    newMatriz2=np.insert(newMatriz2,[0],tit,axis=0)
    tabla5=np.zeros_like(newMatriz2)
    print("======================================")
    print("TABLA SIMPLEX AUMENTADA INICIAL")
    tablaInicial=np.copy(newMatriz2)
    impresion.imp(newMatriz2)
    print("======================================")
    #se busca la M en la columna de la ecuación Z
    indexCol=[]
    for i in range(newMatriz2.shape[1]):
        if newMatriz2[1,i].count('M')>0:
            indexCol.append(i)
            
    print(indexCol)

    #Se busca la fila donde esta el 1, en la columna
    indexFil=[]
    for k in range(len(indexCol)):
        for i in range(newMatriz.shape[0]):
            if newMatriz[i,indexCol[k]-2]==1:
                indexFil.append(i)
                break;
    print(indexFil)


    M=symbols("M")
    #esto es para eliminar la M de la primera fila
    #Se toma opera asi -M*Fk-->F1, donde Fk es la fila que tiene el 1 debajo de la M
    #se hace solo para una por ahora
    for k in range(len(indexFil)):
        for i in range(newMatriz2.shape[1]-1):
            if minimizar:
                a=(parse_expr(newMatriz2[indexFil[k]+2,i+1])*(M))+parse_expr(newMatriz2[1,i+1])
                
                if isinstance(a, Float):
                    a=Rational(Float(a)).limit_denominator()
                newMatriz2[1,i+1]=a
            else:
                a=(parse_expr(newMatriz2[indexFil[k]+2,i+1])*(-M))+parse_expr(newMatriz2[1,i+1])
                
                if isinstance(a, Float):
                    a=Rational(Float(a)).limit_denominator()
                    
                newMatriz2[1,i+1]=a
            
    print("=================================================")
    print("TABLA CON LA ELIMINACIÓN DE LA M DE FILA 1")
    tabla2=np.copy(newMatriz2)
    impresion.imp(newMatriz2)
    print("=================================================")

    #elección de columna pivote:
    indexMax=Columnapivote.find(newMatriz2,minimizar)
    print("La col pivote es: ",indexMax)

            
                
    indexPivote=Filapivote.find(newMatriz2,indexMax)
    print("La Fila pivote es: ",indexPivote)

    #se hace cambio de variable de busqueda
    newMatriz2[indexPivote,0]=newMatriz2[0,indexMax]
    base=parse_expr(newMatriz2[indexPivote,indexMax])
    for i in range(newMatriz2.shape[1]-2):
        a=(parse_expr(newMatriz2[indexPivote,i+2])/base)
        newMatriz2[indexPivote,i+2]=Rational(float(Float(a))).limit_denominator()

    for j in range(newMatriz2.shape[0]-1):
        if j+1 != indexPivote:
            inverso=(parse_expr(newMatriz2[j+1,indexMax])*(-1))
            if isinstance(inverso, Float):
                inverso=Rational(float(Float(inverso))).limit_denominator()
                #round(float(Float(inverso)),1)
            for i in range(newMatriz2.shape[1]-2):
                a=(parse_expr(newMatriz2[indexPivote,i+2])*(inverso))+parse_expr(newMatriz2[j+1,i+2])
                if isinstance(a, Float):
                        a=Rational(float(Float(a))).limit_denominator()
                        #a=float(Float(a))
                newMatriz2[j+1,i+2]=a
    print("=================================================")
    print("TABLA CON PRIMERA ELIMINACIÓN GAUSS JORDAN")
    tabla4=np.copy(newMatriz2)
    impresion.imp(newMatriz2)
    print("=================================================")

    indexMax=Columnapivote.find(newMatriz2,minimizar)
    print("La col pivote es: ",indexMax)

    indexPivote=Filapivote.find(newMatriz2,indexMax)
    print("La Fila pivote es: ",indexPivote)

    #se hace cambio de variable de busqueda
    newMatriz2[indexPivote,0]=newMatriz2[0,indexMax]
    base=parse_expr(newMatriz2[indexPivote,indexMax])
    for i in range(newMatriz2.shape[1]-2):
        a=(parse_expr(newMatriz2[indexPivote,i+2])/base)
        newMatriz2[indexPivote,i+2]=Rational(float(Float(a))).limit_denominator()
        #round(float(Float(a)),1)

    for j in range(newMatriz2.shape[0]-1):
        if j+1 != indexPivote:
            inverso=(parse_expr(newMatriz2[j+1,indexMax])*(-1))
            if isinstance(inverso, Float):
                inverso=Rational(float(Float(inverso))).limit_denominator()
                #round(float(Float(inverso)),1)
            for i in range(newMatriz2.shape[1]-2):
                a=(parse_expr(newMatriz2[indexPivote,i+2])*(inverso))+parse_expr(newMatriz2[j+1,i+2])
                if isinstance(a, Float):
                        a=Rational(float(Float(a))).limit_denominator()
                        #round(float(Float(a)),1)
                newMatriz2[j+1,i+2]=a
    print("=================================================")
    print("TABLA CON SEGUNDA ELIMINACIÓN GAUSS JORDAN")
    tabla3=np.copy(newMatriz2)
    impresion.imp(newMatriz2)
    print("=================================================")
    res=[]
    soluciones=np.empty((TamZ,2),dtype=object)
    if Parada.comprobar(newMatriz2,minimizar):
        if abs(sympify(newMatriz2[1,-1]).subs(M,1)-sympify(newMatriz2[1,-1]).as_coefficients_dict().get(1, 0))<=1e-7:
            a=(newMatriz2[1,0])
            b=(round(float(Float(sympify(newMatriz2[1,-1]).subs(M,10))),1))
            print(res)
            print(newMatriz2[1,0]," = ",round(float(Float(sympify(newMatriz2[1,-1]).subs(M,10))),1))
        else:
            print(newMatriz2[1,0]," = ",newMatriz2[1,-1])
        for i in range(TamZ):
            variable=newMatriz2[0,2+i]
            soluciones[i,0]=variable
            for j in range(newMatriz2.shape[0]-1):
                if parse_expr(newMatriz2[j+1,2+i])==1:
                    soluciones[i,1]=newMatriz2[j+1,-1]
                    print(variable," = ",newMatriz2[j+1,-1])
        
        #Aca Se realiza el primer análisis de soluciones Finales
        columnafinal=newMatriz2[2:,0]
        solutions,Be_inv,recursos,Ce,indicesColFinal=SolFinales.soluciones(columnafinal,tablaInicial,newMatriz)
        print("recursos ",recursos)
        sombra=precioSombra.get(Be_inv,recursos,Ce)
        solutions2=variablesDecision.get(newMatriz2,tablaInicial,Ce,indicesColFinal)
        pendiente1=-(entrada2_1/entrada2_2)
        pendiente2=-(entrada3_1/entrada3_2)
        pendiente3=-(entrada4_1/entrada4_2)
        Ecuacion1=pendiente1*x+(resultado2/entrada2_2)
        Ecuacion2=pendiente2*x+(resultado3/entrada3_2)
        Ecuacion3=pendiente3*x+(resultado4/entrada4_2)
        return a,b,tablaInicial,soluciones,tabla2,tabla3,tabla4,tabla5,solutions,sombra,solutions2
    
    indexMax=Columnapivote.find(newMatriz2,minimizar)
    print("La col pivote es: ",indexMax)

    indexPivote=Filapivote.find(newMatriz2,indexMax)
    print("La Fila pivote es: ",indexPivote)

    #se hace cambio de variable de busqueda
    newMatriz2[indexPivote,0]=newMatriz2[0,indexMax]
    base=parse_expr(newMatriz2[indexPivote,indexMax])
    for i in range(newMatriz2.shape[1]-2):
        a=(parse_expr(newMatriz2[indexPivote,i+2])/base)
        newMatriz2[indexPivote,i+2]=Rational(float(Float(a))).limit_denominator()
        #round(float(Float(a)),1)

    for j in range(newMatriz2.shape[0]-1):
        if j+1 != indexPivote:
            inverso=(parse_expr(newMatriz2[j+1,indexMax])*(-1))
            if isinstance(inverso, Float):
                inverso=Rational(float(Float(inverso))).limit_denominator()
                #round(float(Float(inverso)),1)
            for i in range(newMatriz2.shape[1]-2):
                a=(parse_expr(newMatriz2[indexPivote,i+2])*(inverso))+parse_expr(newMatriz2[j+1,i+2])
                if isinstance(a, Float):
                        a=Rational(float(Float(a))).limit_denominator()
                        #round(float(Float(a)),1)
                newMatriz2[j+1,i+2]=a
    print("=================================================")
    print("TABLA CON TERCERA ELIMINACIÓN GAUSS JORDAN")
    tabla5=np.copy(newMatriz2)
    impresion.imp(newMatriz2)
    print("=================================================")

    if Parada.comprobar(newMatriz2,minimizar):
        if abs(sympify(newMatriz2[1,-1]).subs(M,1)-sympify(newMatriz2[1,-1]).as_coefficients_dict().get(1, 0))<=1e-7:
            a=(newMatriz2[1,0])
            b=(round(float(Float(sympify(newMatriz2[1,-1]).subs(M,10))),1))
            print(res)
            print(newMatriz2[1,0]," = ",round(float(Float(sympify(newMatriz2[1,-1]).subs(M,10))),1))
        else:
            print(newMatriz2[1,0]," = ",newMatriz2[1,-1])
        for i in range(TamZ):
            variable=newMatriz2[0,2+i]
            soluciones[i,0]=variable
            for j in range(newMatriz2.shape[0]-1):
                if parse_expr(newMatriz2[j+1,2+i])==1:
                    soluciones[i,1]=newMatriz2[j+1,-1]
                    print(variable," = ",newMatriz2[j+1,-1])
        #Aca Se realiza el primer análisis de soluciones Finales
        columnafinal=newMatriz2[2:,0]
        solutions,Be_inv,recursos,Ce,indicesColFinal=SolFinales.soluciones(columnafinal,tablaInicial,newMatriz)
        sombra=precioSombra.get(Be_inv,recursos,Ce)
        solutions2=variablesDecision.get(newMatriz2,tablaInicial,Ce,indicesColFinal)
        return a,b,tablaInicial,soluciones,tabla2,tabla3,tabla4,tabla5,solutions,sombra,solutions2
    else:
        return a,b,tablaInicial,soluciones,tabla2,tabla3,tabla4,tabla5,solutions,sombra,solutions2