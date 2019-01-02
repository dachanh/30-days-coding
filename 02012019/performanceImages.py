import cv2 
import numpy as np 

def main():
    img1 = cv2.imread('noise.png')
    img2 = cv2.imread('lena.jpg')
    img1 = cv2.resize(img1,(img2.shape[0],img2.shape[1]))
    #res = cv2.addWeighted(img1,0.7,img2,0.3,0)
    res = np.hstack([img1,img2])
    cv2.imshow('test1',res)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()