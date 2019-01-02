import cv2 
import numpy as np 

def main():
    img = cv2.imread('trump.jpg')
    J = cv2.imread('silicon_valley.jpg')
    J = cv2.resize(J,(img.shape[1],img.shape[0]))
    T1 , T2 , T3 = cv2.split(img)
    _,thresh1 = cv2.threshold(T1,120,255,cv2.THRESH_BINARY)
    _,thresh2 = cv2.threshold(T2,120,255,cv2.THRESH_BINARY)
    _,thresh3 = cv2.threshold(T3,120,255,cv2.THRESH_BINARY)
    M = np.zeros((img.shape[0],img.shape[1]),dtype='uint8')
    N = np.zeros((img.shape[0],img.shape[1]),dtype='uint8')
    M = thresh1*thresh2*thresh3
    N = cv2.bitwise_not(M)
    K = np.zeros((img.shape),dtype='uint8')
    for c in range(3):
        K[:,:,c] = M*J[:,:,c] +  N*img[:,:,c]
    cv2.imshow('K',K)
    cv2.waitKey(0) 


if __name__ == "__main__":
    main()