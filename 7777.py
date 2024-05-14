import cv2
import os
import numpy as np

# 读取文件夹路径和文件扩展名
folder_path = r"H:\DATAdata_First\Endoscopicreal"
extension = ".jpg"

# 获取文件夹中前10张图像的文件名
file_names = [f for f in os.listdir(folder_path) if f.endswith(extension)][101:200]

# 添加噪声的函数
def add_noise(image):
    # 添加高斯噪声
    mean = 0
    var = 0.2
    sigma = var ** 0.5
    h, w, c = image.shape
    noise = np.random.normal(mean, sigma, (h, w, c))
    noisy_image = np.clip(image + noise * 255, 0, 255).astype(np.uint8)
    return noisy_image

# 遍历图像文件，并添加噪声后重新写入文件
for file_name in file_names:
    # 读取图像
    image_path = os.path.join(folder_path, file_name)
    image = cv2.imread(image_path)

    # 添加噪声
    noisy_image = add_noise(image)

    # 生成噪声图像的文件名
    noisy_image_name = os.path.splitext(file_name)[0] + "_Noise.jpg"
    noisy_image_path = os.path.join(folder_path, noisy_image_name)

    # 写入文件
    cv2.imwrite(noisy_image_path, noisy_image)

    print(f"Noisy image saved: {noisy_image_path}")
