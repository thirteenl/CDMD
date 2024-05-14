import os
import time

import cv2

from ColorF import C_RGB, pearson_similarity
from Phash import phash


def read_images_from_folder(parent_folder):
    folder_dict = {}
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        folder_dict[folder_name] = []
        if os.path.isdir(folder_path):
            for file_name in os.listdir(folder_path):
                if file_name.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.BMP')):
                    image_path = os.path.join(folder_path, file_name)
                    folder_dict[folder_name].append(image_path)
    return folder_dict


parent_folder = r"H:\DATAdata_First"
folder_dict = read_images_from_folder(parent_folder)  # {folder_name:[image_path]}

for key in folder_dict.keys():
    color_time = 0
    no_color_time = 0
    for counter, img_path in enumerate(folder_dict.get(key)):
        img = cv2.imread(img_path)
        # color
        color_start_time = time.time()
        # c_table = C_RGB(img_path, 8, 1080)
        phash_valun=phash(img)
        # pearson_similarity(list(phash_valun.values()), list(phash_valun.values()))
        color_end_time = time.time()
        color_time += (color_end_time - color_start_time)

        # no_color
        # no_color_start_time = time.time()
        # no_c = None_RGB(img_path, 1080)
        # pearson_similarity(no_c, no_c)
        # no_color_end_time = time.time()
        # no_color_time += (no_color_end_time - no_color_start_time)

        if (counter + 1) % 100 == 0:
            print("{}-{} color_time: {}".format(key, counter + 1, color_time))
           # print("{}-{} no_color_time: {}".format(key, counter + 1, no_color_time))
        if counter > 1000:
            break
