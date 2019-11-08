import cv2 
import numpy as np 
import matplotlib.pyplot as plt
img = cv2.imread('./trump.jpg')
noise = cv2.imread('./noise.jpg')
f = np.zeros((img.shape),np.uint8)
for c in range(3):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            f[i][j][c] = img[i][j][c] if img[i][j][c] + noise[i][j][c] > 255 else img[i][j][c] + noise[i][j][c]   
cv2.imwrite('result.jpg',f)