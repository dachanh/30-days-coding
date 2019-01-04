import cv2
import numpy as  np 
import matplotlib.pyplot as plt

def band_thresholding(img,thresh):
    print(img)
    _,thresholding = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
    _,thresholding_inv = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
    print(thresholding)
    print(thresholding_inv)
    result = cv2.bitwise_and(thresholding,thresholding_inv)
    cv2.imshow('binary',thresholding)
    cv2.imshow('binary inv',thresholding_inv)
    cv2.imshow('band thresholding',result) 
    return result

def main():
    img = cv2.imread('lena.jpg',0)
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    plt.plot(hist)
    plt.xlim([0,255])
    plt.show()
    result = band_thresholding(img,127)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()