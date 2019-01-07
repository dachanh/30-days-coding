import cv2
import numpy as np 

def main():
    img = cv2.imread('trum.jpg',0)
    output =  np.zeros((img.shape),np.uint8)
    output[img > 70] = 255
    Kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(17,17))
    J = cv2.morphologyEx(output, cv2.MORPH_OPEN, Kernel)
    cv2.imshow('output',output)
    cv2.imshow('openning',J)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()