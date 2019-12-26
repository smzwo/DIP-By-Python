# # include<opencv2/opencv.hpp>
# # include<iostream>
# using
# namespace
# std;
# using
# namespace
# cv;
# int
# main(int
# a, char ** p)
# {
#     Mat
# input = imread("水滴.png", CV_LOAD_IMAGE_GRAYSCALE); // 以灰度图像的方式读入图片
# imshow("input", input); // 显示原图
# int
# w = getOptimalDFTSize(input.cols);
# int
# h = getOptimalDFTSize(input.rows); // 获取最佳尺寸，快速傅立叶变换要求尺寸为2的n次方
# Mat
# padded;
# copyMakeBorder(input, padded, 0, h - input.rows, 0, w - input.cols, BORDER_CONSTANT, Scalar::all(0)); // 填充图像保存到padded中
# Mat
# plane[] = {Mat_ < float > (padded), Mat::zeros(padded.size(), CV_32F)}; // 创建通道
# Mat
# complexIm;
# merge(plane, 2, complexIm); // 合并通道
# dft(complexIm, complexIm); // 进行傅立叶变换，结果保存在自身
# split(complexIm, plane); // 分离通道
# magnitude(plane[0], plane[1], plane[0]); // 获取幅度图像，0
# 通道为实数通道，1
# 为虚数，因为二维傅立叶变换结果是复数
# int
# cx = padded.cols / 2;
# int
# cy = padded.rows / 2; // 一下的操作是移动图像，左上与右下交换位置，右上与左下交换位置
# Mat
# temp;
# Mat
# part1(plane[0], Rect(0, 0, cx, cy));
# Mat
# part2(plane[0], Rect(cx, 0, cx, cy));
# Mat
# part3(plane[0], Rect(0, cy, cx, cy));
# Mat
# part4(plane[0], Rect(cx, cy, cx, cy));
#
# part1.copyTo(temp);
# part4.copyTo(part1);
# temp.copyTo(part4);
#
# part2.copyTo(temp);
# part3.copyTo(part2);
# temp.copyTo(part3);
#
# // ** ** ** 傅里叶逆变换 ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
# Mat
# _complexim;
# complexIm.copyTo(_complexim); // 把变换结果复制一份，进行逆变换，也就是恢复原图
# Mat
# iDft[] = {Mat::zeros(plane[0].size(), CV_32F), Mat::zeros(plane[0].size(), CV_32F)}; // 创建两个通道，类型为float，大小为填充后的尺寸
# idft(_complexim, _complexim); // 傅立叶逆变换
# split(_complexim, iDft); // 结果貌似也是复数
# magnitude(iDft[0], iDft[1], iDft[0]); // 分离通道，主要获取0通道
# normalize(iDft[0], iDft[0], 1, 0, CV_MINMAX); // 归一化处理，float类型的显示范围为0 - 1, 大于1为白色，小于0为黑色
# imshow("idft", iDft[0]); // 显示逆变换
#                             // ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
#
# plane[0] += Scalar::all(1); // 傅立叶变换后的图片不好分析，进行对数处理，结果比较好看
# log(plane[0], plane[0]);
# normalize(plane[0], plane[0], 1, 0, CV_MINMAX);
#
# imshow("dft", plane[0]);
# waitKey();
# return 0;
# }
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cat.jpg', 0)
# 傅里叶变换
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
# 移频
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
# 创建一个掩膜，中间方形为1，其余为0
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1
# 使用掩膜
fshift = dft_shift * mask
magnitude_spectrum1 = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))
# 逆移频
f_ishift = np.fft.ifftshift(fshift)
# 逆傅里叶变换
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

plt.subplot(221), plt.imshow(img, cmap='gray'),
plt.title('Input Image'), plt.axis('off')
plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray'),
plt.title('Magnitude Spectrum')
plt.subplot(223), plt.imshow(img_back, cmap='gray'),
plt.title('Input Image'), plt.axis('off')
plt.subplot(224), plt.imshow(magnitude_spectrum1, cmap='gray'),
plt.title('Magnitude Spectrum')
plt.show()


https://blog.csdn.net/ZhangXiaoyu_sy/article/details/99672623#7.2%E5%82%85%E9%87%8C%E5%8F%B6%E5%8F%98%E6%8D%A2