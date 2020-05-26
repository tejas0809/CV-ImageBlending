'''
  File name: getIndexes.py
  Author:
  Date created:
'''

import numpy as np


def getIndexes(mask, targetH, targetW, offsetX, offsetY):
# %% Enter Your Code Here
    indexes=np.zeros((targetH,targetW),dtype=int)
    mask[mask>0]=1
    mask[mask>0]=[i+1 for i in range(len(mask[mask>0]))]
    indexes[offsetY:offsetY+mask.shape[0],offsetX:offsetX+mask.shape[1]]=mask
    return indexes
