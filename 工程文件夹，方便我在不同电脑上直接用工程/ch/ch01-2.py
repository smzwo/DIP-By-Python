import cv2
import os

#获取脚本所在位置
root_path = os.getcwd()

#获取cat.jpg所在位置，即资源文件位置
cat_path = root_path + '/../source/'

#获取cat.jpg名字
imageName = os.path.abspath(cat_path + 'cat.jpg')

imgae = cv2.imread(imageName)

cv2.imshow("windowsName", imgae)

cv2.waitKey(0)