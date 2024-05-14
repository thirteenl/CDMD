import os
import time
#from DES import encrypt_image, decrypt_image
# from Three_DES import encrypt_image, decrypt_image
# from RC4 import encrypt_image, decrypt_image
# from SM4 import encrypt_image, decrypt_image
from AES import encrypt_image, decrypt_image

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
    encrypt_time = 0
    decrypted_time = 0
    for counter, img_path in enumerate(folder_dict.get(key)):
        # 加密
        encrypt_start_time = time.time()
        encrypt_data, encrypt_key = encrypt_image(img_path)  # 调用加密算法
        encrypt_end_time = time.time()
        encrypt_time += (encrypt_end_time - encrypt_start_time)

        # 解密
        decrypted_start_time = time.time()
        img = decrypt_image(encrypt_data, encrypt_key)  # 调用解密算法
        decrypted_end_time = time.time()
        decrypted_time += (decrypted_end_time - decrypted_start_time)

        if (counter + 1) % 200 == 0:
            print("{}-{} encrypt_time: {}".format(key, counter + 1, encrypt_time))
            # print("{}-{} decrypted_time: {}".format(key, counter + 1, decrypted_time))
        if counter > 1000:
            break
