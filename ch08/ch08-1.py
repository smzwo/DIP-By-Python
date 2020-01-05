#jpg图片的压缩
import cv2
img = cv2.imread('cat.jpg',1)
#对于jpg文件的压缩，第三个参数是压缩质量
cv2.imwrite('D:\imageTest.jpeg',img,[cv2.IMWRITE_JPEG_QUALITY,90])
#1M 100K 10K 图片质量的范围是0-100 有损压缩
#jpg图片的额压缩压缩质量参数数值越小，压缩比越高
