import cv2
import numpy as np 

def main():
    img = cv2.imread('lena.jpg')
    print(img.shape)
    S = 8 
    m , n = int(img.shape[0]/8),int(img.shape[1]/8) 
    print(m)
    J = np.zeros((m,n,3),dtype='uint8')
    for c in range(3):
        for i in range(m):
            for j in range(n):
                sum = 0 
                for h in range(i,i+1):
                    for w in range(j,j+1):
                        sum += img[h,w,c]
                J[i,j,c] = int(sum/2)
    cv2.imshow('J',J)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()