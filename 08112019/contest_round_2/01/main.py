import cv2
import numpy as np 

img = cv2.imread('lion.jpg')
hsv_img = cv2.imread('lionHSV.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.merge((gray,gray,gray))
result = np.concatenate((img,hsv_img,gray),axis=1)
cv2.imwrite('result.jpg',result)
cv2.waitKey(0)