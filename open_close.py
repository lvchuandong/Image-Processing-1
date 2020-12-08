# coding=utf-8
import cv2

img = cv2.imread('images/img1.jpg', 0)
cv2.imshow('image', img)
# 定义结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 闭运算
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# 显示腐蚀后的图像
cv2.imshow("Close", closed)

# 开运算
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# 显示腐蚀后的图像
cv2.imshow("Open", opened)

cv2.waitKey(0)
cv2.destroyAllWindows()