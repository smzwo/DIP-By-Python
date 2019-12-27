import cv2
#读取文件路径
img_path = 'C:/Users/17806/Desktop/cat.jpg'
#读取图片
img = cv2.imread(img_path)
#声明窗口
cv2.namedWindow("img")
#显示图像
cv2.imshow("img", img)
#按键等待  0表示一直等待
cv2.waitKey(0)