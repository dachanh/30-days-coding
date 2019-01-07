import cv2
import numpy as np
img = cv2.imread('image_test.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations =1) 
openning = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.imshow('openning',openning)
cv2.waitKey(0)