import cv2
import numpy as np
import matplotlib.pyplot as plt
def main():
    img = cv2.imread('lena.jpg')
    height , width = img.shape[:2]
    S = np.zeros(img.shape,dtype='uint8')
    for h in range(height):
        for w in range(width):
            if (w == 0):
                S[h,w,:] = img[h,w,:]
            else:
                S[h,w,:] = 2*img[h,w,:] - img[h,w-1,:]
    hist_col =  cv2.calcHist([S],[2],None,[256],[0,256])
    plt.plot(hist_col)
    plt.xlim([0,255])
    plt.show()


if __name__ == "__main__":
    main()