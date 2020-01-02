import cv2

#读取文件
img = cv2.imread("sl.jpg",0)
cv2.imshow('img',img)
#获取图片行数
w = img.shape[0]
#获取图片列数
h = img.shape[1]
for i in range(w-1):
    for j in range(h-1):
        img[i, j] = img[i - 1, j - 1] / 9 + img[i - 1, j] / 9 + img[i - 1, j + 1] / 9 + img[i, j - 1] / 9 + img[
            i, j] / 9 + img[i, j + 1] / 9 + img[i + 1, j - 1] / 9 + img[i + 1, j] / 9 + img[i + 1, j + 1] / 9
cv2.imshow('dst',img)
cv2.waitKey()



