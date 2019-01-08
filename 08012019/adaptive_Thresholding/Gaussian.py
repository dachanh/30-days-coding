import cv2
import numpy as np 
import matplotlib.pyplot as plt 

 
def main():
    img = cv2.imread('trump.jpg',0)
    thresh_Mean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                        cv2.THRESH_BINARY,55,2)
    thresh_Mean_INV = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                        cv2.THRESH_BINARY_INV,55,2)
    cv2.imshow('thresh',thresh_Mean)
    cv2.imshow('thresh INV',thresh_Mean_INV)

    cv2.waitKey(0)

if __name__ == "__main__":
    main()