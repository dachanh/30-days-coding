import cv2
import numpy as np 


img = cv2.imread('simple.jpg')

G = cv2.GaussianBlur(img,(25,25),0)
cv2.imwrite('result.jpg',G)