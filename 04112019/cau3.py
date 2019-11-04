import numpy as np 
import cv2

data = open('data.txt','r').readlines()
v  , b= [[],[],[]] , []
for indx ,line in enumerate(data):
    temp = line.split()
    v[0].append(int(temp[0]))
    v[1].append(int(temp[1]))
    v[2].append(int(temp[2]))
    b.append(int(temp[3]))
 
img = cv2.imread('./lion.jpg')
k = cv2.copyMakeBorder(img,0,0,0,0,cv2.BORDER_REPLICATE) 
m,n = img.shape[:2]
ID = []
for idx,it in enumerate(b):
    if it  != 0:
        ID.append(idx)
for c in range(3):
    for it in ID: v[c][it] = 0
    for j in range(n):
        count = 1
        for i in range((j-1)*m + 1 ,j*m):
            k[count,j,c] = v[c][i]
            count += 1
k =np.array(k,np.uint8)
cv2.imshow('k',k)
cv2.waitKey(0)
