import cv2
import numpy as np 

def main():
    img = cv2.imread('lena.jpg',0)
    _,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    thresh = cv2.resize(thresh,(100,150))
    cv2.imshow('thresh',thresh)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()