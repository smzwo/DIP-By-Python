import cv2

def myLineAdjust(image, k, b):
    # 将tuple中的元素取出，赋值给height，width，channels
    height = image.shape[0]
    width = image.shape[1]

    for row in range(height):
        for col in range(width):
            val = image[row][col]
            newVal = val * k + b
            if newVal > 255 :
                image[row][col] = 255
            else:
                image[row][col] = newVal

    return image

if __name__ == '__main__':

    image = cv2.imread('cat.jpg', 0)
    cv2.imshow('srcImage', image)

    dstImage = myLineAdjust(image, 1, 100)
    cv2.imshow('dstImage', dstImage)

    cv2.waitKey(0)