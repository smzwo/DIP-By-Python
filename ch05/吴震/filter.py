import cv2
import numpy as np

def main():
    image = cv2.imread('sljy.jpg', 0)

    Km = np.array(([1/9, 1/9, 1/9,
                   1/9, 1/9, 1/9,
                   1/9, 1/9, 1/9]), dtype="float32")
    dstImage = cv2.filter2D(image, -1, Km)
    htich = np.hstack((image, dstImage))
    cv2.imshow('srcImage & dstImage', htich)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()