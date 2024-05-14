import numpy as np
import ColorF
#皮尔森系数相似验证
def pearson_correlation(x, y):
    # 计算x和y的平均值
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # 计算x和y的差值
    diff_x = x - mean_x
    diff_y = y - mean_y

    # 计算皮尔逊相关系数
    correlation = np.sum(diff_x * diff_y) / (np.sqrt(np.sum(diff_x**2)) * np.sqrt(np.sum(diff_y**2)))

    return correlation


# 不同图像的色彩指纹作为输入，并计算二者相似度
x=ColorF.Color_values_array
y=ColorF.Color_values_array
print(pearson_correlation(x, y))