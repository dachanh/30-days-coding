import cv2 
import numpy as np 


img = cv2.imread('lena.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Canny = cv2.Canny(gray,14,15)
img[Canny != 255] = 0
cv2.imwrite('result.jpg',img)
