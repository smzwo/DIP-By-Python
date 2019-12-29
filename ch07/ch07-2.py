# 迭代阈值分割
import cv2

# 获取列表（数组）的平均值
def getMediaNum(list):
    sum = 0
    for i in range(len(list)):
        sum = sum +list[i]
    meidiaNum = sum / len(list)
    return meidiaNum

# 获取平均灰度
def getMedianGrayValue(image):
    grayValue = 0
    height = srcImg.shape[0]
    width = srcImg.shape[1]
    for row in range(height):
        for col in range(width):
            grayValue = grayValue + image[row][col]

    medianGrayValue = grayValue / (height * width)
    return medianGrayValue

# 迭代计算最优阈值
def getBestGrayValue(image, mediaGrayValue):
    grayValuePart_1 = []
    grayValuePart_2 = []
    height = image.shape[0]
    width = image.shape[1]
    for row in range(height):
        for col in range(width):
            grayValuePart_1.append(image[row][col]) if float(image[row][col]) > mediaGrayValue else grayValuePart_2.append(image[row][col])
    bestGrayValue = (getMediaNum(grayValuePart_1) + getMediaNum(grayValuePart_2)) / 2
    if (abs(bestGrayValue - mediaGrayValue) > 1):
        mediaGrayValue = bestGrayValue
        getBestGrayValue(image, mediaGrayValue)
    return bestGrayValue

if __name__ == '__main__':
    srcImg = cv2.imread('lena.jpg', 0)
    cv2.imshow('srcImg', srcImg)

    mediaGrayValue = getMedianGrayValue(srcImg)

    # 按中间阈值分割，自行填充代码

    # 获取最优阈值，并输出

    # 按最优阈值分割

    # 图片显示