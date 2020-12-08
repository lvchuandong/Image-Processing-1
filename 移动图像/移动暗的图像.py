import cv2
import numpy as np
import os
import shutil

file_names = os.listdir('./003image')
file_names.sort()
# print(file_names[0], len(file_names))
for file_len in range(len(file_names)):
    file_name = file_names[file_len]
    img = cv2.imread('003image/' + file_name)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_mean = np.mean(img_gray)
    print(file_len, img_mean, file_name)
    if img_mean < 50:
        shutil.move('003image/' + file_name, 'new_img/' + file_name)
    