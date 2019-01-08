import cv2
import numpy as np
import matplotlib.pyplot as plt
def main():
    img = cv2.imread('test_btc.jpg')
    height , width = img.shape[:2]
    S = np.zeros(img.shape,dtype='uint8')
    for r in range(height):
        for c in range(width):
            if (c <= 1):
                S[r,c,:] = img[r,c,:]
            else:
                S[r,c,:] = 2*img[r,c,:] - img[r,c-1,:]
    cv2.imshow('test',S)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()