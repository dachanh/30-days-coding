import cv2 
import numpy as np 


img = cv2.imread('trump.jpg')
hls = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
cv2.imwrite('result.jpg',hls[:,:,2])
