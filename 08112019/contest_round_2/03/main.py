import cv2
import numpy as np 

img = cv2.imread('lena.jpg',0)
_,thresh = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
cv2.imwrite('result.jpg',thresh)
