'''
  File name: reconstructImg.py
  Author:
  Date created:
'''
import numpy as np



def reconstructImg(indexes, red, green, blue, targetImg):
# %% Enter Your Code Here
    resultImg=np.copy(targetImg)
    coords=np.argwhere(indexes>0)
    for x,y in coords:
        resultImg[x,y,0]=red[indexes[x,y]-1]
        resultImg[x,y,1]=green[indexes[x,y]-1]
        resultImg[x,y,2]=blue[indexes[x,y]-1]
    return resultImg
