import cv2
import math
import numpy as np
#linear regression
X1=[0,1,1,2,1,0,2,3,4,3,2,1,5]
X2=[80,110,115,135,112,90,138,180,250,190,140,112,400]
Y=[800000,1100000,1050000,1500000,1200000,750000,1400000,2100000,5000000,2300000,1600000,1150000,7500000]

def avg(num_list):
    avg = 0
    for num in num_list:
        avg += num
    avg = avg / num_list.__len__()
    return avg

if(X1.__len__() == Y.__len__()):
    sumU = 0
    sumD = 0
    avgX1 = avg(X1)
    avgX2 = avg(X2)
    avgY = avg(Y)
    for i in range(X1.__len__()):
        sumU += (X1[i]-avgX1)*(Y[i]-avgY)
        sumD += (X1[i]-avgX1)*(X1[i]-avgX1)
    b1 = sumU/sumD
    for i in range(X2.__len__()):
        sumU += (X2[i]-avgX2)*(Y[i]-avgY)
        sumD += (X2[i]-avgX2)*(X2[i]-avgX2)
    b2 = sumU/sumD
    
    b0 = avgY-b1*avgX1 - b2*avgX2
    print("b2={} b1={}  b0={}".format(b2,b1,b0))

    #visualize
    mask = np.ones((500,500), dtype="uint8")*255
    for i in range(6):
        pos = math.ceil(i*495/6)
        mask[495:500,pos:pos+5] = 0
    for i in range(X1.__len__()):
        pos = math.ceil(X1[i]*495/6)
        value = 500 - math.ceil(Y[i]/10000000*500)
        mask[value:value+5,pos:pos+5]  = 125
    for i in range(int(500/5)):
        pos = i*5
        v = b0 + b1*5/495*pos + b2*400/500*pos
        value = 500 - math.ceil(v/10000000*500)
        print(value)
        mask[value:value+5,pos:pos+5]  = 180
    cv2.imwrite('reg.jpg',mask)