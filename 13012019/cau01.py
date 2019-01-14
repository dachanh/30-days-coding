import cv2
import  numpy as np
import matplotlib.pyplot as plt

f = open('./img/label.txt')
line = f.readline()
temp = './img/'
count = 1
for i in range(1,5):
    temp = './img/'+str(i)+'.png'
    img = cv2.imread(temp)
    plt.subplot(1,4,i)
    plt.imshow(img)
    plt.title(line)
    line = f.readline()
plt.show()

