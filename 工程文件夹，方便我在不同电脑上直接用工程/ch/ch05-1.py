import cv2

# 求平均
def getAverage(list):
    temp = 0
    for i in list:
        temp = temp + i
    avg = temp / len(list)
    return avg

def main():
    image = cv2.imread('cat.jpg', 0)
    cv2.imshow('srcImage', image)

    # 将tuple中的元素取出，赋值给height，width，channels
    height = image.shape[0]
    width = image.shape[1]
    # 边界不做处理
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            # 创建一个3✖️3的9阶滤波器
            np = [image[row - 1][col - 1], image[row - 1][col], image[row - 1][col + 1],
                  image[row][col - 1], image[row][col], image[row][col + 1],
                  image[row + 1][col - 1], image[row + 1][col], image[row + 1][col + 1]]
            # 求平均值
            avg = getAverage(np)
            # 给目标图像中对应像素赋灰度值
            image[row][col] = avg

    cv2.imshow('dstImage', image)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()

