import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('008.jpg', 0)  # 转灰度

# 中值滤波
img = cv2.medianBlur(img, 3)

# 二值阈值化
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # cv2.THRESH_BINARY: 阈值类型

# 阈值取相邻区域的平均值。

# img:   输入图像的名称
# 255：   预设满足条件的最大值
# ADAPTIVE_THRESH_MEAN_C :  自定义阈值算法;该算法为局部邻域块的平均值，即先求出块中的均值，再减去常数C。
# cv2.THRESH_BINARY: 阈值类型
# 11： 邻域块的大小
#  2：常数，阈值等于平均值或者加权平均值减去这个常数。
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

#:阈值取值相邻区域的加权和，权重为一个高斯窗口

th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,
                            2)  # ADAPTIVE_THRESH_GAUSSIAN_C：局部邻域块的高斯加权和。该算法是在区域中某一点周围的像素根据高斯函数按照他们离中心点的距离进行加权计算，再减去常数C。

titles = ['Original Image', 'Global Thresholding(v=127)', 'Adaptive Mean Thresholding',
          'Adaptive Gaussian Thresholding']

images = [img, th1, th2, th3]
print(th2)
cv2.imshow('th2', th1)
cv2.waitKey(0)

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
