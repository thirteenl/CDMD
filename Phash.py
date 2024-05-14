import time

import cv2
import numpy as np
#from HammingD import hmddistance
# 定义感知哈希
def phash(img):
    # step1：调整大小为8*8
    # img = cv2.imread(image_path)
    img = cv2.resize(img, (8, 8))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype(np.float32)
    # step2：离散余玄变换
    img = cv2.dct(img)
    img = img[0:8, 0:8]
    sum = 0.
    hash_str = ''
    #step3：计算均值
    for i in range(8):
        for j in range(8):
            sum += img[i, j]
    avg = sum / 64
    # avg=np.mean(img)
    # print(avg)
    # step4：获取hash
    for i in range(8):
        for j in range(8):
            if img[i, j] > avg:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str



# # 开始时间
# start_time = time.time()
# image_path=r"H:\ColorDe_Code\000000000205.jpg"
# Image=cv2.imread(image_path)
# # 结束时间
# stop_time = time.time()
#
# print(phash(Image))
# print(stop_time-start_time)
#
#
# if __name__ == '__main__':
#     img1 = cv2.imread(r'J:\PiLiangTest\ImageofSPIFT\000000000139.jpg')
#     img2 = cv2.imread(r'J:\PiLiangTest\ImageofSPIFT\000000000285.jpg')
#     # mp_img = motion(img1, 10, 0)
#     hash1 = phash(img1)
#     hash2 = phash(img2)
#     dis = hmddistance(hash1, hash2)
#     print(len(hash1))
#     # print(hash2)
#     print("汉明距离", dis)


