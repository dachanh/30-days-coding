import cv2
import numpy as np 


img = cv2.imread('lion.jpg')
B , G , R = cv2.split(img)
cv2.imwrite('result.jpg',R)