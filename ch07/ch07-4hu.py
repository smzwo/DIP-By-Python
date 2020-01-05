import cv2
from datetime import datetime
import numpy as np
np.set_printoptions(suppress=True)

def humoments(img_gray):
    '''
    由于7个不变矩的变化范围很大,为了便于比较,可利用取对数的方法进行数据压缩;同时考虑到不变矩有可能出现负值的情况,因此,在取对数之前先取绝对值
    经修正后的不变矩特征具有平移 、旋转和比例不变性
    '''
    # 标准矩定义为m_pq = sumsum(x^p * y^q * f(x, y))
    row, col = img_gray.shape
    #计算图像的0阶几何矩
    m00 = img_gray.sum()
    m10 = m01 = 0
    #　计算图像的二阶、三阶几何矩
    m11 = m20 = m02 = m12 = m21 = m30 = m03 = 0
    for i in range(row):
        m10 += (i * img_gray[i]).sum()
        m20 += (i ** 2 * img_gray[i]).sum()
        m30 += (i ** 3 * img_gray[i]).sum()
        for j in range(col):
            m11 += i * j * img_gray[i][j]
            m12 += i * j ** 2 * img_gray[i][j]
            m21 += i ** 2 * j * img_gray[i][j]
    for j in range(col):
        m01 += (j * img_gray[:, j]).sum()
        m02 += (j ** 2 * img_gray[:, j]).sum()
        m30 += (j ** 3 * img_gray[:, j]).sum()
    # 由标准矩我们可以得到图像的"重心"
    u10 = m10 / m00
    u01 = m01 / m00
    # 计算图像的二阶中心矩、三阶中心矩
    y00 = m00
    y10 = y01 = 0
    y11 = m11 - u01 * m10
    y20 = m20 - u10 * m10
    y02 = m02 - u01 * m01
    y30 = m30 - 3 * u10 * m20 + 2 * u10 ** 2 * m10
    y12 = m12 - 2 * u01 * m11 - u10 * m02 + 2 * u01 ** 2 * m10
    y21 = m21 - 2 * u10 * m11 - u01 * m20 + 2 * u10 ** 2 * m01
    y03 = m03 - 3 * u01 * m02 + 2 * u01 ** 2 * m01
    # 计算图像的归格化中心矩
    n20 = y20 / m00 ** 2
    n02 = y02 / m00 ** 2
    n11 = y11 / m00 ** 2
    n30 = y30 / m00 ** 2.5
    n03 = y03 / m00 ** 2.5
    n12 = y12 / m00 ** 2.5
    n21 = y21 / m00 ** 2.5
    # 计算图像的七个不变矩
    h1 = n20 + n02
    h2 = (n20 - n02) ** 2 + 4 * n11 ** 2
    h3 = (n30 - 3 * n12) ** 2 + (3 * n21 - n03) ** 2
    h4 = (n30 + n12) ** 2 + (n21 + n03) ** 2
    h5 = (n30 - 3 * n12) * (n30 + n12) * ((n30 + n12) ** 2 - 3 * (n21 + n03) ** 2) + (3 * n21 - n03) * (n21 + n03) \
        * (3 * (n30 + n12) ** 2 - (n21 + n03) ** 2)
    h6 = (n20 - n02) * ((n30 + n12) ** 2 - (n21 + n03) ** 2) + 4 * n11 * (n30 + n12) * (n21 + n03)
    h7 = (3 * n21 - n03) * (n30 + n12) * ((n30 + n12) ** 2 - 3 * (n21 + n03) ** 2) + (3 * n12 - n30) * (n21 + n03) \
        * (3 * (n30 + n12) ** 2 - (n21 + n03) ** 2)
    inv_m7 = [h1, h2, h3, h4, h5, h6, h7]
    inv_m7 = np.log(np.abs(inv_m7))
    return inv_m7

if __name__ == '__main__':
    t1 = datetime.now()
    img = cv2.imread('lena.jpg',0)
    print(humoments(img))
    print(datetime.now() - t1)