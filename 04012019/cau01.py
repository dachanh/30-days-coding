import cv2
import numpy as np 

def main():
    cap = cv2.VideoCapture('test.mp4')
    count = 0 
    f_10 = None
    f_30 = None
    res  = None 
    while (True):
        count += 1
        _,frame = cap.read()
        if count == 10 :
            f_10 = frame
        if count == 30 :
            f_30 = frame
            res = cv2.absdiff(f_10 ,f_30)
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.imshow('test',res)
    cv2.waitKey(0)

if __name__ == "__main__":
    main()