# import cv2 as cv
# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.feature import local_binary_pattern
# import time
#
# img = cv.imread(r"H:\ColorDe_Code\000000000205.jpg", cv.IMREAD_COLOR)
# plt.imshow(img[:, :, ::-1])
#
# # 转换为灰度图
# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# plt.imshow(img_gray, plt.cm.gray)
#
# # LBP特征提取
# # 可以使用PIL Image，也可以使用skimage
# # 本示例使用skimage（scikit-image包，基于scipy的图像处理包），首先要确保
# # skimage包已经安装，可以使用pip install scikit-image来进行安装
# # 1. 设置需要的参数
# #   LBP算法中半径参数
# radius = 1
# #   邻域像素点个数
# n_points = 8 * radius
#
# # 开始时间
# start_time = time.time()
#
# # 原始LBP特征提取
# lbp = local_binary_pattern(img_gray, 8, 1)
#
# # 结束时间
# stop_time = time.time()
#
# # 圆形LBP特征提取
# lbp_ror = local_binary_pattern(img_gray, n_points, radius, method="ror")
# # 旋转不变LBP特征提取
# lbp_var = local_binary_pattern(img_gray, n_points, radius, method="var")
# # 等价特征
# lbp_uniform = local_binary_pattern(img_gray, n_points, radius, method="nri_uniform")
#
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 16), dpi=100)
# axes[0][0].set_title("LBP")
# axes[0][0].imshow(lbp, plt.cm.gray)
# axes[0][1].set_title("LBP ROR")
# axes[0][1].imshow(lbp_ror, plt.cm.gray)
# axes[1][0].set_title("LBP VAR")
# axes[1][0].imshow(lbp_var, plt.cm.gray)
# axes[1][1].set_title("LBP NRI_UNIFORM")
# axes[1][1].imshow(lbp_uniform, plt.cm.gray)
# print(lbp)
#
#
# print(stop_time-start_time)

import cv2
import numpy as np

# 8个邻域
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def calculate_LBP_pixel(img, i, j):
    center = img[i, j]
    pattern = 0
    # 依次比较像素值，构建LBP特征
    for k in range(8):
        row = i + dy[k]
        col = j + dx[k]
        if img[row, col] >= center:
            pattern += 2 ** k
    return pattern


def LBP(img):
    rows, cols = img.shape
    lbp_img = np.zeros((rows - 2, cols - 2), dtype=np.uint8)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            lbp_img[i - 1, j - 1] = calculate_LBP_pixel(img, i, j)
    return lbp_img


def normalize_histogram(hist):
    hist_sum = np.sum(hist)
    return hist / hist_sum


def apply_threshold(hist, threshold):
    return [1 if val > threshold else 0 for val in hist]


def lbp(img):
    # 读取图像
    # img = cv2.imread(r"H:\ColorDe_Code\000000000081.jpg", cv2.IMREAD_GRAYSCALE)
    # 转为灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 计算LBP
    lbp_img = LBP(img)

    # 计算直方图
    hist, _ = np.histogram(lbp_img, bins=np.arange(0, 256), range=(0, 255))

    # 计算直方图的平均值
    avg_hist = np.mean(hist)

    # 将直方图值与平均值比较，大于平均值设为1，小于等于平均值设为0
    binary_hist = apply_threshold(hist, avg_hist)
    return binary_hist

# print("Binary Histogram:", binary_hist)  #结果是255长度的字符串
