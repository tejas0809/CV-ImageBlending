'''
  File name: seamlessCloningPoisson.py
  Author:
  Date created:
'''
import numpy as np
from scipy import sparse as spla
from getIndexes import getIndexes
from getCoefficientMatrix import getCoefficientMatrix
from getSolutionVect import getSolutionVect
from reconstructImg import reconstructImg

def seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY):


    targetH=targetImg.shape[0]
    targetW=targetImg.shape[1]
    indexes=getIndexes(mask,targetH,targetW,offsetX,offsetY)
    coeffA=getCoefficientMatrix(indexes)
    solVectorb_R=getSolutionVect(indexes,sourceImg[:,:,0],targetImg[:,:,0],offsetX,offsetY)
    solVectorb_G=getSolutionVect(indexes,sourceImg[:,:,1],targetImg[:,:,1],offsetX,offsetY)
    solVectorb_B=getSolutionVect(indexes,sourceImg[:,:,2],targetImg[:,:,2],offsetX,offsetY)
    x_R=spla.linalg.spsolve(coeffA,solVectorb_R.T)
    x_G=spla.linalg.spsolve(coeffA,solVectorb_G.T)
    x_B=spla.linalg.spsolve(coeffA,solVectorb_B.T)

    x_R=np.clip(x_R,0,255)
    x_G=np.clip(x_G,0,255)
    x_B=np.clip(x_B,0,255)
    resultImg=reconstructImg(indexes,x_R,x_G,x_B,targetImg)
    return resultImg
