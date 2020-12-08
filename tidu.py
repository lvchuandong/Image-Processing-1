import cv2
import numpy as np

img = cv2.imread('4.png', 0)
# print(img.shape)
# cv2.imshow('img', img)
cv2.destroyAllWindows()


def cv_imshow(img, name):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)  # 绝对值转换
# cv_imshow(sobelx, 'sobelx')

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)  # 绝对值转换
# cv_imshow(sobely, 'sobely')
# 分别为计算x和y，再求和
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)  # 将x和y融合起来
print(sobelxy.shape)
# for i in range(len(sobelxy)):
#     print(sobelxy[i])
# cv_imshow(sobelxy, 'sobelxy')
img_h, img_w = sobelxy.shape
img_w_new = int(img_w*0.02)
kernel_mat = np.ones((img_h, img_w_new))
mat_list = []
for i in range(img_w-img_w_new+1):
    sum_kernel = np.sum(np.multiply(sobelxy[:,i:i+img_w_new], kernel_mat))
    mat_list.append(sum_kernel)
# print(mat_list)
# for i in range(len(mat_list)):
#     if mat_list[i]<img_h*img_w_new*20:
#         cv2.line(sobelxy, (i,0), (i,img_h), (255,255,255),2)
new_mat_list = mat_list[int(img_w*0.1):int(img_w*0.9)]
min_index = new_mat_list.index(min(new_mat_list)) + int(img_w*0.1)
cv2.line(sobelxy, (min_index,0), (min_index,img_h), (255,255,255),2)
cv2.imshow('img',sobelxy)
cv2.waitKey(0)

