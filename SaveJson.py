import os
import json
import time

import cv2
from BL_MLE_Tag import main
from LBP import lbp
from CS_Phash import OutP
from A_S_SHA256 import sha256_main
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

root = r"H:\ColorDe_Code\JsonFile"
if not os.path.exists(root):
    os.mkdir(root)

al_name = "SHA_256"  # 修改算法名
for key in folder_dict.keys():
    json_path = os.path.join(root, al_name + "_" + key + ".json")
    dict_ = {}
    counter = 0
    label_time = 0
    for counter, img_path in enumerate(folder_dict.get(key)):
        img = cv2.imread(img_path)
        # 调用标签算法
        label_start_time = time.time()
        label = phash(img)   #更改算法
        label_end_time = time.time()
        label_time += label_end_time - label_start_time
        if (counter + 1) % 100 == 0 and counter < 1000:
            print("{}-{}-{} Tag_time: {}".format(al_name, key, counter + 1, label_time))
        dict_[img_path] = label  # {img_path:label}
    with open(json_path, "w+") as jf:
        json.dump(dict_, jf)
