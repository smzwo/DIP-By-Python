import cv2
import numpy as np

#读取文件
# def imred(name):
#     cv_img = cv2.imdecode(np.fromfile(name, dtype=np.uint8), -1)
#     return cv_img
img1 = cv2.imread("cb.jpg",0)
img2 = cv2.imread("cb1.jpg",0)
#显示图像
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
#获取图片行数
w = img2.shape[0]
#获取图片列数
h = img2.shape[1]
#处理图片
for i in range(w):
    for j in range(h):
        #处理方式

        img1[i,j]=img1[i,j]/2+img2[i,j]/2

        if img1[i,j] > 255:
            img1[i, j] = 255
        if img1[i,j] < 0:
            img1[i, j] = 0
#显示处理图像
cv2.imshow("dst", img1)
#按键等待  0表示一直等待
cv2.waitKey(0)