'''
  File name: getCoefficientMatrix.py
  Author:
  Date created:
'''
import numpy as np
from scipy import sparse

def getCoefficientMatrix(indexes):
    maxim=np.max(indexes)
    # print("maxin",maxim)
    coeffA=np.zeros((maxim,maxim),dtype=int)
    np.fill_diagonal(coeffA,4)
    coords=np.argwhere(indexes>0)
    for (x,y) in coords:
        if indexes[x,y-1]>0:
            coeffA[indexes[x,y]-1,indexes[x,y-1]-1]=-1
        if indexes[x,y+1]>0:
            coeffA[indexes[x,y]-1,indexes[x,y+1]-1]=-1
        if indexes[x-1,y]>0:
            coeffA[indexes[x,y]-1,indexes[x-1,y]-1]=-1
        if indexes[x+1,y]>0:
            coeffA[indexes[x,y]-1,indexes[x+1,y]-1]=-1
    # print("h",coeffA.shape)
    coeffA=sparse.csr_matrix(coeffA)
    return coeffA
