import cv2
import numpy as np

img = cv2.imread('halo.jpg')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
CNTS = []

def check_black(img):
    pixels = 0
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x,y] == 0:
                pixels += 1
    return pixels

for x in contours:
    if 10 < x.shape[0] < 80:       
        el = cv2.fitEllipse(x)      
        lm = np.ones(img.shape[:2], dtype="uint8") * 255
        cv2.fillPoly(lm,pts=[x],color=(0,0,0))
        cv2.ellipse(lm,el,color=(255,255,255))
        if check_black(lm) > 150:
            CNTS.append(x)
        
mask = np.ones(img.shape[:2], dtype="uint8") * 255
print(img.shape[:2])
cv2.drawContours(mask, CNTS, -1, 0, -1)

extra = np.concatenate(CNTS[:])
boundrect = cv2.boundingRect(extra)
cv2.rectangle(img,boundrect,color=(255,0,0))

cv2.imwrite('j.jpg',img)