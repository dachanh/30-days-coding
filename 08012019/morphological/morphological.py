import cv2
import numpy as np 


def main():
    img = cv2.imread('test.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    """
        don't use kernel
    """
    for it in range(3):
        eroded = cv2.erode(gray.copy(),None,iterations= it + 1)
        cv2.imwrite("./result/Eroded_Non-kernel-%d.png" % (it+1), eroded)
        dilated = cv2.dilate(gray.copy(),None,iterations = it + 1)
        cv2.imwrite("./result/Dilated_Non-kernel-%d.png"%(it+1),dilated) 
    """
        user kernel
    """
    size = [(3,3),(5,5),(7,7)]
    for it in range(3):
        kernel =  np.ones(size[it],np.uint8)
        eroded = cv2.erode(gray.copy(),kernel,it+1)
        cv2.imwrite("./result/Eroded_Kernel-%d.png"%(it+1),eroded)
        dilated = cv2.dilate(gray.copy(),kernel,it+1)
        cv2.imwrite("./result/Dilated_Kernel-%d.png"%(it+1),dilated)
    cv2.waitKey(0)
if __name__ == "__main__":
    main()