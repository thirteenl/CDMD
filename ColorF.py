import cv2
from collections import Counter
import time
import numpy as np
from scipy.stats import pearsonr


#     # print(count_rgb_zone_combinations(all_rgb_values))
# 现在all_rgb_values包含了图像中所有像素的RGB值

# print(all_rgb_values)


# 定义区段映射函数
def map_to_zone(value):
    if 0 <= value < 63:
        return 0
    elif 63 <= value < 127:
        return 1
    elif 127 <= value < 191:
        return 2
    elif 191 <= value <= 255:
        return 3
    else:
        raise ValueError("Value out of range")


# 计算两个一维数据的皮尔森相关系数
def pearson_similarity(data1, data2):
    correlation, _ = pearsonr(data1, data2)
    # print(correlation)
    return correlation


def C_RGB(image_path, patch,size):
    # 初始化统计表
    table_fp = {(i, j, k): 0 for i in range(4) for j in range(4) for k in range(4)}

    # 读取图像文件
    # image_path = r'H:\ColorDe_Code\000000000205.jpg'  # 文件路径
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
    for y in range(0, height, patch):
        for x in range(0, width, patch):
            r, g, b = np.mean(image_rgb[y:y + patch, x:x + patch], axis=(0, 1))
            # print(b, g, r)
            # 映射
            k = (map_to_zone(r), map_to_zone(g), map_to_zone(b))
            table_fp[k] += 1
    return table_fp

# # 输入色彩值
# rgb_values = all_rgb_values
#
# # 统计每种RGB组合的次数
# combination_counts = count_rgb_zone_combinations(rgb_values)
#
# # 打印结果
# for combination, count in combination_counts:
#     print(f"Combination {combination} appears {count} times")
#
# print(combination_counts)
#
# Color_values_array = [value for _, value in combination_counts]
# print(Color_values_array)
# ---------------------------------颜色组合测试
#
# image_patch = r"H:\ColorDe_Code\0001.jpg"
# image_path_2 = r'H:\ColorDe_Code\0002.jpg'
#
# # 初始化表
# table1 = init_fp_table()
# table2 = init_fp_table()
#
# # color fp
# Color_S_time = time.time()
# c1 = C_RGB(image_patch, table1, 2)
# c2 = C_RGB(image_path_2, table2, 2)
#
# pearson_similarity(list(c1.values()), list(c2.values()))
# Color_E_time = time.time()
# print(Color_E_time - Color_S_time)
