import cv2
img = cv2.imread("lena.jpg",0)
cv2.imshow("img", img)
# 获取图片行数
w = img.shape[0]
# 获取图片列数
h = img.shape[1]
sum=float()
# sum1=float()
sum1=[]
# sum2=float()
sum2=[]
gray=float()
# x=y=0
# 处理图片


def getMediaVaule(list):
    number = 0
    for i in range(len(list)):
        number = number + list[i]
    return  number / len(list)


for i in range(w):
    for j in range(h):
        sum = sum + img[i, j]
        #print(img[i, j])
gray=sum/w/h
print(gray)
for m in range(1,20):
    for i in range(w):
        for j in range(h):
            if img[i,j]<gray:
                # x=x+1
                # sum1=sum1+img[i,j]
                sum1.append(img[i, j])
            else:
                # y=y+1
                sum2.append(img[i, j])

                # sum2=sum2+img[i,j]
        panduan = getMediaVaule(sum1)
        panduan2 = getMediaVaule(sum2)
        if abs(gray-panduan/2- panduan2/2)>1:
            print(gray)
            gray=panduan/2 + panduan2/2
            print(gray)
            sum1 = []
            sum2 = []
        else:
            gray = panduan / 2 + panduan2 / 2
            print(gray)
            break
    break
for i in range(w):
    for j in range(h):
        if img[i, j] > gray:
            img[i, j]=255
        if img[i, j] < gray:
            img[i, j]=0
print(gray)
cv2.imshow("dst", img)
cv2.waitKey(0)
