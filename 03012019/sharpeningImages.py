import cv2
import numpy as np 
import matplotlib.pyplot as plt
def main():
    img = cv2.imread('lena.jpg',0)
    hist_original = cv2.calcHist([img],[0],None,[256],[0,256])
    G = img.astype(np.double)
    kernel = np.ones((4,4),np.float32)/16
    J = cv2.filter2D(G,-1,kernel)
    K = G - J
    U = 0.5*K + J 
    U = U.astype(np.uint8)
    hist = cv2.calcHist([U],[0],None,[256],[0,256])
    plt.plot(hist_original,color='b')
    plt.plot(hist,color='r')
    plt.legend(('original','new image'),loc='upper right')
    plt.xlim([0,256])
    plt.show()
    cv2.imshow('sdfaas',U)
    cv2.waitKey(0)
if __name__ == "__main__":
    main()