import cv2
import numpy as np 

def histogram_equalisation(img):
    total_of_pixels = img.shape[0] * img.shape[1]
    res = np.zeros(img.shape,dtype='uint8')
    hist = cv2.calcHist([img],[0],None,[256],[0,256])
    cum_sum = np.cumsum(hist)
    LUT = np.zeros((256))
    for it in range(256):
        out = int((cum_sum[it]*255)/(total_of_pixels+1))
        LUT[it] = out
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[i,j] = LUT[img[i,j]]
    return res
def main():
    img = cv2.imread('lena.jpg')
    hls = cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
    res = histogram_equalisation(hls[:,:,1])
    equ = cv2.equalizeHist(hls[:,:,1])
    res_1 = np.hstack((hls[:,:,1],equ))
    cv2.imshow('test',res_1)
    cv2.imshow('original',hls[:,:,1])
    cv2.imshow('result',res)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()