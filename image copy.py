import cv2
import numpy as np

img = cv2.imread('j.jpg')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
v = np.array(imgray)

for x in range(v.shape[0]):
    for y in range(v.shape[1]):
        if v[x,y] < 20:
            v[x,y] = 255
        else:
            v[x,y] = 0


cv2.imwrite('j.jpg',v)