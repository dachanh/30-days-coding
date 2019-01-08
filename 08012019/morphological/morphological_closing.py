import cv2
import numpy as np  


def main():
    size = [(3,3),(5,5),(7,7)]
    for it in range(3):
        string = "./res_openning/Openning-"+str(it+1)+".png"
        img = cv2.imread(string,0)
        SE = cv2.getStructuringElement(cv2.MORPH_RECT,size[it])
        closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,SE)
        cv2.imwrite("./res_closing/Closing-%d.png"%(it+1),closing)


if __name__ == "__main__":
    main()