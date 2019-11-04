import cv2 
import numpy as np 


img = cv2.imread('lion.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
H2GRAY = np.zeros((hsv.shape[0],hsv.shape[1]),np.float64)
H = hsv[:,:,0]/179
H2GRAY[(H > 0.22) & (H < 0.45)] = 1
cv2.imshow('sds',H2GRAY)
cv2.waitKey()