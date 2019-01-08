import cv2
import numpy as numpy


def main():
    img = cv2.imread('./advance_test.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    """
    Structuring element : RECT
    """
    size = [(3,3),(5,5),(7,7)]
    for it in range(3):
        SE = cv2.getStructuringElement(cv2.MORPH_RECT,size[it])
        openning = cv2.morphologyEx(gray.copy(),cv2.MORPH_OPEN,SE) 
        cv2.imwrite("./res_openning/Openning-%d.png"%(it+1),openning)
    """
    """

    """
    """
    cv2.waitKey(0)

if __name__ == "__main__":
    main()