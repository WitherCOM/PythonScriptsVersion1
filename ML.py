import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image


img = Image.open('teszt.png')
img = np.asarray(img)
red = img[:,:,0].copy()

filt = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])



def matrix_spec(mx1,mx2):
    ki = 0
    for x in range(3):
        for y in range(3):
            ki += mx1[x,y]*mx2[x,y]
    return ki

def applyfilter(pic_in,filt,stride=1):
    if (img.shape[0]-3)%stride == 0:
        w =(img.shape[0]-3)/stride+1
    else:
        w=(img.shape[0]-3 - (img.shape[0]-3)%stride)/stride+1

    if (img.shape[1]-3)%stride == 0:
        h =(img.shape[1]-3)/stride+1
    else:
        h=(img.shape[1]-3 - (img.shape[1]-3)%stride)/stride+1

    pic_out = np.zeros((int(w),int(h)),dtype='u1')
    if pic_in.ndim == 3:
        for x in range(0,pic_out.shape[0]):
            for y in range(0,pic_out.shape[1]):
                for z in range(pic_in.shape[2]):
                    pic_out[x,y] += matrix_spec(filt,pic_in[x*stride:x*stride+3,y*stride:y*stride+3,z])
    else:
        for x in range(0,pic_out.shape[0]):
            for y in range(0,pic_out.shape[1]):
                pic_out[x,y] = matrix_spec(filt,pic_in[x*stride:x*stride+3,y*stride:y*stride+3])
    
    return pic_out



new = applyfilter(img,filt,3)

