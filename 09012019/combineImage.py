import cv2
import numpy as np 
import matplotlib.pyplot as plt
def main():
    I = cv2.imread("trum.jpg")
    G = np.zeros((I.shape[0],I.shape[1]),dtype='uint8')
    for h in range(I.shape[0]):
        for w  in  range(I.shape[1]):
            G[h,w] = (1/2)*(max(max(I[h,w,0],I[h,w,1]),I[h,w,2])+ min(min(I[h,w,0],I[h,w,1]),I[h,w,2]))
    hist_G = cv2.calcHist([G],[0],None,[256],[50,100])
    plt.plot(hist_G)
    plt.xlim([50,100])
    plt.show()
    cv2.imshow("sd",G)
    cv2.waitKey(0)
if __name__ == "__main__":
    main()