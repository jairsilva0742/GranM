import sympy as sp
def get(newMatriz2,tablaInicial,Ce,indicesColFinal):
    BinvA=newMatriz2[2:,2:-1]
    CC=tablaInicial[1,2:-1]
    solutions2=[]
    for i in range(len(Ce)):
        CeSp=sp.Matrix(Ce)
        CCSp=sp.Matrix(CC)
        CeSp[i]='C1'
        CCSp[int(indicesColFinal[i])]='-C1'
        Ope=CeSp.T*sp.Matrix(BinvA)
        Ope1=Ope+CCSp.T
        print("C ",CCSp)
        print(" C*BeinvA",Ope)
        print(" Vector ",Ope1)
        ecuaciones2=[]
        for j in range(len(Ope1)):
            ecu=str(Ope1[j])
            if "C1" in ecu and "M" not in ecu:
                ecu2= ecu+">0"
                ecuaciones2.append(ecu2)
        c1=sp.symbols('C1')
        print(len(ecuaciones2))   
        if len(ecuaciones2)==2:
            solucion2 = str(sp.solve([sp.sympify(ecuaciones2[0]),sp.sympify(ecuaciones2[1])], c1))
        elif len(ecuaciones2)==3:
            solucion2 = str(sp.solve([sp.sympify(ecuaciones2[0]),sp.sympify(ecuaciones2[1]),sp.sympify(ecuaciones2[3])], c1))
        elif len(ecuaciones2)==1:
            solucion2 = str(sp.solve([sp.sympify(ecuaciones2[0])], c1))
        else:
            solucion2 = str(sp.solve([sp.sympify(ecuaciones2[0]),sp.sympify(ecuaciones2[1]),sp.sympify(ecuaciones2[3]),sp.sympify(ecuaciones2[4])], c1))
        solutions2.append(solucion2)
    return solutions2