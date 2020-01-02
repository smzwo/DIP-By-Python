import cv2


def bubbleSort(list):
    n = len(list)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

def main():
    #读取文件
    img = cv2.imread("sljy.jpg",0)
    cv2.imshow('img',img)
    #获取图片行数
    w = img.shape[0]
    #获取图片列数
    h = img.shape[1]
    for i in range(w-1):

        for j in range(h-1):
          np=[img[i - 1, j - 1],img[i - 1, j],img[i - 1, j + 1],img[i, j - 1],img[i, j],img[i, j + 1],img[i + 1, j - 1],img[i + 1, j],img[i + 1, j + 1]]
          bubbleSort(np)
          img[i,j]=np[4]
    cv2.imshow('dst',img)
    cv2.waitKey()

if __name__ == '__main__':
    main()