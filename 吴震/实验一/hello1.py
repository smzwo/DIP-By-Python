import cv2
#读取文件
img = cv2.imread("cat.jpg")
#声明窗口（可省略）
cv2.namedWindow("img")
#显示图像
cv2.imshow("img", img)
#按键等待  0表示一直等待
cv2.waitKey(0)