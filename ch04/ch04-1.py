import matplotlib.pyplot as plt
import cv2

img_BGR = cv2.imread('cat.jpg')  # BGR
cv2.imshow("BGR", img_BGR)

img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB", img_RGB)

img_GRAY = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", img_GRAY)

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", img_HSV)

img_YcrCb = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb)
cv2.imshow("YcrCb", img_YcrCb)

img_HLS = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HLS)
cv2.imshow("HLS", img_HLS)

img_XYZ = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2XYZ)
cv2.imshow("XYZ", img_XYZ)

img_LAB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", img_LAB)

img_YUV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YUV)
cv2.imshow("YUV", img_YUV)

cv2.waitKey(0)