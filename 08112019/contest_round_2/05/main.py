import cv2 
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg',0)
img[((img > 100) & (img < 150)) | ((img > 10) & (img < 70))] = 0
cv2.imwrite('result.jpg',img)
