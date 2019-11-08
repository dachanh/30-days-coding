import cv2 
import numpy as np 


img = cv2.imread('trump.jpg')

B , G , R = cv2.split(img)

C = 255 - R 
M = 255 - G
Y = 255 - B
result = cv2.merge((C,M,Y))
cv2.imwrite('result.jpg',result)