from cv2 import *
import matplotlib.pyplot as plt
import numpy as np

img = imread('./img/1.png')
data = np.loadtxt('./img/matrix.txt')
data = data.astype(np.uint8)
for it in range(data.shape[0]):
    print(data[it][0],data[it][1],data[it][2],data[it][3])
    rectangle(img,(data[it][0],data[it][1]),(data[it][0]+data[it][2],data[it][1]+data[it][3]),(0,254,34),3)
imshow('asda',img)
waitKey(0)


