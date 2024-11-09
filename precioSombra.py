import numpy as np
def get(Be_inv,recursos,Ce):
    sombra=[]
    original=np.dot(np.array(Ce, dtype=float),np.dot(Be_inv,recursos))
    
    for i in range(len(recursos)):
        recursos[i]=recursos[i]+1
        x=np.dot(Be_inv,recursos)
        zz=np.dot(np.array(Ce, dtype=float),x)                     
        sombra.append(abs(zz-original))
    return sombra