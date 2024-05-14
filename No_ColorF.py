# import cv2
# import numpy as np
from scipy.stats import pearsonr
# import time
#
# # 读取并重置图像尺寸
# def resize_image(image_path, width, height):
#     img = cv2.imread(image_path)
#     resized_img = cv2.resize(img, (width, height))
#     return resized_img
#
# # 提取图像的RGB值并串联成一维数据
# def extract_rgb(image):
#     r, g, b = cv2.split(image)
#     rgb = np.concatenate((r.flatten(), g.flatten(), b.flatten()))
#     return rgb
#
# # 计算两个一维数据的皮尔森相关系数
# def pearson_similarity(data1, data2):
#     correlation, _ = pearsonr(data1, data2)
#     return correlation
#
# # 读取并处理两张图像
# image1 = resize_image(r"H:\ColorDe_Code\000000000081.jpg", 128, 128)
# image2 = resize_image(r"H:\ColorDe_Code\000000000205.jpg", 128, 128)
#
# Color_S_time=time.time()
# # 提取图像的RGB值
# rgb1 = extract_rgb(image1)
# rgb2 = extract_rgb(image2)
#
# # 计算皮尔森相似度
# similarity = pearson_similarity(rgb1, rgb2)
# Color_E_time=time.time()
# print("Pearson Similarity:", similarity)
# print(Color_E_time-Color_S_time)
# print(len(rgb1))
import cv2
import numpy as np
import time


# 读取图片

def None_RGB(image_path, size):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (size, size))
    # OpenCV默认以BGR格式读取图像，如果需要RGB，可以转换
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 获取图像的高度和宽度
    height, width = image_rgb.shape[:2]

    # # 遍历图像的每个像素并获取RGB值
    # for y in range(height):
    #     for x in range(width):
    #         # 获取像素的RGB值
    #         b, g, r = image_rgb[y, x]
    #
    #         # # 打印RGB值或进行其他处理
    #         # print(f"Pixel at ({x}, {y}) has RGB values: ({r}, {g}, {b})")

    # 将BGR转换为RGB-------这一步可以不需要
    all_rgb_values = []
    for y in range(height):
        for x in range(width):
            r, g, b = image_rgb[y, x]
            all_rgb_values.append((r, g, b))

    # 将RGB值级联成一维数组
    rgb_array = np.reshape(all_rgb_values, (-1, 3)).flatten()

    # print(len(rgb_array))
    return rgb_array


# 计算两个一维数据的皮尔森相关系数
def pearson_similarity(data1, data2):
    correlation, _ = pearsonr(data1, data2)
    return correlation
#
#
# S_time = time.time()
# image_path_1 = r'H:\ColorDe_Code\0001.jpg'
# data1 = C_RGB(image_path_1)
# image_path_2 = r'H:\ColorDe_Code\0002.jpg'
# data2 = C_RGB(image_path_2)
#
# pearson_similarity(data1, data2)
# E_time = time.time()
# print(E_time - S_time)
