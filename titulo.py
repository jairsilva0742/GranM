import numpy as np
def titulo(tam,variable):
    a=np.zeros(tam)
    for i in range(tam):
        a[i]=i+1
    a=a.astype(int).astype(str)
    for i in range(tam):
        a[i]=variable+a[i]
    return a