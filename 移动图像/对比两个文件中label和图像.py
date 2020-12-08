import cv2
import numpy as np
import os
import shutil

file_names_img = os.listdir('003image')
file_names_img.sort()
file_names_img = [i[:-4] for i in file_names_img]
file_names_label = os.listdir('003label')
file_names_label.sort()
# print(file_names[0], len(file_names))
for file_len in range(len(file_names_label)):
    file_name_label = file_names_label[file_len]
    if file_name_label[:-4] in file_names_img:
        shutil.copyfile('003label/' + file_name_label, 'new_label/' + file_name_label)
    print(file_len)

    
    
    