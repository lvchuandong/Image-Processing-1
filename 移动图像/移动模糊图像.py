import cv2
import numpy as np
import os
import shutil

file_names = os.listdir('./new_img')
file_names.sort()
# print(file_names[0], len(file_names))
for file_len in range(len(file_names)):
    file_name = file_names[file_len]
    img = cv2.imread('new_img/' + file_name)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imagevar = cv2.Laplacian(img_gray, cv2.CV_64F).var()
    print(file_len, imagevar)
    if imagevar < 50:
        shutil.move('new_img/' + file_name, 'blurry_img/' + file_name)
    
    