import cv2
import numpy as np 

def birdview(img):
    pass

def thresh_hls_s(img, thresh = (170,255)):
    hls = cv2.cvtColor(img,cv2.COLOR_RGB2HLS).astype(np.float)
    binary_image = np.zeros((hls.shape[0],hls.shape[1]),dtype='uint8')
    binary_image[(hls[:,:,2] >= thresh[0]) & (hls[:,:,2] <= thresh[1])] = 255
    return binary_image

def thresh_hls_l(img, thresh = (140,255)):
    hls = cv2.cvtColor(img,cv2.COLOR_RGB2HLS)
    binary_image = np.zeros((hls.shape[0],hls.shape[1]),dtype='uint8')
    binary_image[(hls[:,:,1] > thresh[0]) & (hls[:,:,1] <= thresh[1])] = 255
    return binary_image


def sobel_x(img,thresh = (140,255)):
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    binary_image = np.zeros((img.shape[0],img.shape[1]),dtype='uint8')
    return sobelx

def sobel_y(img,thresh = (140,255)):
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
    binary_image = np.zeros((img.shape[0],img.shape[1]),dtype='uint8')
    return sobely

def main():
    img = cv2.imread('test.png')
    cv2.imshow('original',img)
    sobelx = sobel_x(img)
    sobely = sobel_y(img)
    #hls_s = thresh_hls_s(img)
    hls_l = thresh_hls_l(img)
    cv2.imshow('Sobel X',sobelx)
    cv2.imshow('Sobel Y',sobely)
    cv2.imshow('s channel',thresh_hls_s(img))
    cv2.imshow('bitwise and',cv2.bitwise_not(sobelx,sobely))
    cv2.imshow('L',hls_l)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()