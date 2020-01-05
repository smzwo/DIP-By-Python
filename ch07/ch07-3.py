import cv2
img = cv2.imread("lena.jpg",0)
cv2.imshow("img", img)
# 获取图片行数
w = img.shape[0]
# 获取图片列数
h = img.shape[1]
sum=float()
sum1=float()
sum2=float()
gray=float()
x=y=0
# 处理图片
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
                x=x+1
                sum1=sum1+img[i,j]
            else:
                y=y+1
                sum2=sum2+img[i,j]
    value=(sum1/x + sum2/y)/2
    if abs(gray-value)>1:
        gray=value
        print(gray)
        sum1 = 0
        sum2 = 0
        x=0
        y=0
    else:
        gray = (sum1/x + sum2/y)/2
        print(gray)
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
