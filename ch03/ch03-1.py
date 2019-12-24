import cv2

def myLineAdjust(image, k, b):
    # 将tuple中的元素取出，赋值给height，width，channels
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print(channels)

    for row in range(height):
        for col in range(width):
            # 若有多通道，则每个通道像素都会改变
            for channel in range(channels):
                val = image[row][col][channel]
                newVal = val * k + b
                if newVal > 255 :
                    image[row][col][channel] = 255
                else:
                    image[row][col][channel] = newVal

    return image

if __name__ == '__main__':

    image = cv2.imread('cat.jpg')
    cv2.imshow('srcImage', image)

    dstImage = myLineAdjust(image, 1, 100)
    cv2.imshow('dstImage', dstImage)

    cv2.waitKey(0)
