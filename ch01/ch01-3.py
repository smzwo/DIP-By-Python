import cv2

image_path = '路径/cat.jpg'

imgae = cv2.imread(image_path)

cv2.imshow("windowsName", imgae)

cv2.waitKey(0)