import cv2
import numpy as np 

def main():
    img = cv2.imread('Gaussian.PNG',0)
    height , width = img.shape[:2] 
    res = np.zeros((height,width),dtype='uint8')
    kernel = np.array([[0,1,1,1,0],
                        [1,2,2,2,1],
                        [1,1,5,1,1],
                        [1,2,2,2,1],
                        [0,1,1,1,0]])
    mid = int(np.einsum('ij->',kernel)/2)
    for h in range(2,height-2):
        for w in range(2,width-2):
            neightbor = []
            for l in range(-2,3):
                for r in range(-2,3):
                    a = img[h+l,w+r]
                    weight = kernel[l+2,r+2]
                    for _ in range(weight):
                        neightbor.append(a)
            neightbor.sort()
            res[h,w] = neightbor[mid]     
    cv2.imshow('img',res)
    cv2.waitKey(0)          


if __name__ == "__main__":
    main()