import numpy as np
from PIL import Image
from scipy import signal
import matplotlib.pyplot as plt
import createMask
import argparse
from seamlessCloningPoisson import seamlessCloningPoisson


mask= createMask.main('1_source.jpg')
targetImg = np.array(Image.open('1_background.jpg').convert('RGB'))
sourceImg=np.array(Image.open('1_source.jpg').convert('RGB'))
offsetX=290
offsetY=250
resultImg=seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY)
plt.imshow(resultImg)
plt.show()
