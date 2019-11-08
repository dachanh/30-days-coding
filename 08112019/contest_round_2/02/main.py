import numpy as np 
import cv2 


img = cv2.imread('lion.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
H2GRAY = np.zeros((hsv.shape[0],hsv.shape[1]),np.float64)
H = hsv[:,:,0]/179
H2GRAY[(H > 0.22) & (H < 0.45)] = 255
cv2.imwrite('result.jpg',H2GRAY)
