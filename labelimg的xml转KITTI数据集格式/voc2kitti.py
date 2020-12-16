import xml.etree.ElementTree as ET
import os
from tqdm import tqdm

base_xml_dir = "./150label/"
xml_list = os.listdir(base_xml_dir)
kitti_saved_dir = "./label_txt/"


def convert_annotation(file_name):
    in_file = open(base_xml_dir + file_name)
    tree = ET.parse(in_file)
    root = tree.getroot()

    with open(kitti_saved_dir + file_name[:-4] + '.txt', 'w') as f:
        for obj in root.iter('object'):
            cls = obj.find('name').text
            # if cls not in object_class_list:
            #     object_class_list.append(cls)
            xmlbox = obj.find('bndbox')
            """
                第5～8这4个数：物体的2维边界框
                xmin，ymin，xmax，ymax
            """
            xmin, ymin, xmax, ymax = xmlbox.find('xmin').text, xmlbox.find('ymin').text, \
                                     xmlbox.find('xmax').text, xmlbox.find('ymax').text
            # if cls == 'trafficsignal' or 'trafficlight':
            #     cls = 'road_sign'
            # elif cls == 'car' or 'bus':
            #     cls = 'vehicle'
            # elif cls == 'bicycle' or 'motorbike':
            #     cls = 'bicycle'
            # elif cls == 'person':
            #     cls = 'pedestrain'
            # else:
            #     pass

            # f.write(cls + " " + '0.00' + " " + '0' + " " + '0.0' + " " + str(xmin) + " "
            #         + str(ymin) + " " + str(xmax) + " " + str(ymax) + " " +
            #         '0.0' + " " + '0.0' + " " + '0.0' + " " + '0.0' + " " + '0.0' + " " + '0.0' + " " + '0.0' + '\n')
            f.write(cls + " " + str(xmin) + " "
                    + str(ymin) + " " + str(xmax) + " " + str(ymax) +
                     '\n')

# object_class_list = []  # ['trafficsignal', 'car', 'person', 'trafficlight', 'bicycle', 'motorbike', 'bus'] 

for i in tqdm(range(len(xml_list))):
    convert_annotation(xml_list[i])
    # print(i)

# print(object_class_list)

