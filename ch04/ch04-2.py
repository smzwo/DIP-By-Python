import cv2
#读取文件
img_BGR = cv2.imread("cat.jpg")
img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)
img_YcrCb = img_BGR
#获取图片行数
w = img_RGB.shape[0]
#获取图片列数
h = img_RGB.shape[1]
for i in range(w):
    for j in range(h):
        #处理方式
        img_YcrCb[i, j, 0] = (img_RGB[i, j, 0] * 0.256789 + img_RGB[i, j, 0] * 0.504129 + img_RGB[
            i, j, 0] * 0.097906) + 16
        img_YcrCb[i, j, 1] = (img_RGB[i, j, 0] * -0.148223 + img_RGB[i, j, 1] * -0.290992 + img_RGB[
            i, j, 2] * 0.439215) + 128
        img_YcrCb[i, j, 2] = (img_RGB[i, j, 0] * 0.439215 + img_RGB[i, j, 1] * -0.367789 + img_RGB[
            i, j, 2] * -0.071426) + 128
#显示处理图像
cv2.imshow("img_RGB", img_RGB)
cv2.imshow("img_YcrCb", img_YcrCb)
#按键等待  0表示一直等待
cv2.waitKey(0)
