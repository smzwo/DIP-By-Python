import cv2

def imageLoad(*args):
    num = 0
    for image in args:
        imageName = 'srcImage' + str(num)
        num = num + 1
        srcImage = cv2.imread(image)
        cv2.imshow(imageName, srcImage)

if __name__ == '__main__':
    imageLoad("cat.jpg", "football.jpg")
    cv2.waitKey(0)