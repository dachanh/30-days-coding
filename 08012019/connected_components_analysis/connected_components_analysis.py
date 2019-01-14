import cv2
from skimage.filters import threshold_local
from skimage import measure
import numpy as np 

def main():
    green = np.uint8([[[255,255,255 ]]])
    hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
    print( hsv_green )
if __name__ == "__main__":
    main()