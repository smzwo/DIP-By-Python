# 编程实现加载并显示三幅图像，其中一幅通过指定文件名的方式读取，一幅图片通过用户键盘输入指定文件，最后一幅通过用户输入资源文件夹下任一一个图片名
import cv2
import os

def imageLoad(*args):
    num = 0
    for image in args:
        imageName = 'srcImage' + str(num)
        num = num + 1
        srcImage = cv2.imread(image)
        cv2.imshow(imageName, srcImage)

if __name__ == '__main__':
    imageFirstName = "cat.jpg"
    imageSecondName = input("请输入指定文件路径：")
    imageThirdName = input('请输入资源文件夹下任一图片名字：')
    # 获取脚本所在位置
    root_path = os.getcwd()
    # 获取图片所在位置，即资源文件位置
    image_path = root_path + '/../source/'
    # 获取名字
    imageThirdName = os.path.abspath(image_path + imageThirdName)


    imageLoad(imageFirstName, imageSecondName, imageThirdName)
    cv2.waitKey(0)