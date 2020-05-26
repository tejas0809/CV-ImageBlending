'''
  File name: getSolutionVect.py
  Author:
  Date created:
'''
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def getSolutionVect(indexes, source, target, offsetX, offsetY):
# %% Enter Your Code argwhere
    laplace=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    convolvedSource=signal.convolve2d(source,laplace,mode='same')
    coords=np.argwhere(indexes>0)
    smallCoords=coords-(offsetY,offsetX)
    # mask1=indexes[offsetY:offsetY+source.shape[0],offsetX:offsetX+source.shape[1]]
    # mask1[mask1>0]=1
    # plt.imshow(mask)
    # plt.show()
    # source1=np.copy(source)
    # source1=source1*mask1
    # plt.imshow(source1)
    # plt.show()
    # convolvedSource=signal.convolve2d(source1,laplace,mode='same')

    SolVectorb=[convolvedSource[i,j] for i,j in smallCoords]

    for (x,y) in coords:
        summ=0
        if indexes[x,y+1]==0:
            summ=summ+target[x,y+1]
        if indexes[x,y-1]==0:
            summ=summ+target[x,y-1]
        if indexes[x+1,y]==0:
            summ=summ+target[x+1,y]
        if indexes[x-1,y]==0:
            summ=summ+target[x-1,y]
        SolVectorb[indexes[x,y]-1]=SolVectorb[indexes[x,y]-1]+summ
    SolVectorb1=np.asarray(SolVectorb, dtype=np.int)
    SolVectorb2=SolVectorb1.reshape((1,SolVectorb1.shape[0]))
    return SolVectorb2
