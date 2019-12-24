import cv2

# 此方法需要将相应的图片放置到工程目录下
imgae = cv2.imread("cat.jpg")

cv2.imshow("windowsName", imgae)

cv2.waitKey(0)