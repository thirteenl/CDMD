import hashlib
import numpy as np
from PIL import Image
import time
import cv2

# 计算 p
p = 10 ** 9 + 7  # 一个足够大的素数，确保位数远远超过哈希值的长度


def preprocess_image(image):
    # 转换为灰度图
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 调整大小为4x4
    #resized_image = gray_image.resize((16, 16))
    return gray_image


def hash_image(image):
    hash_object = hashlib.sha256()
    hash_object.update(image.tobytes())
    hash_hex = hash_object.hexdigest()
    return int(hash_hex, 16) % p  # 将哈希值转换为整数，并取模 p


def calculate_exponentiation(hashed_image, g):
    return pow(g, hashed_image, p)


def main(image):
    # image_path = r"H:\ColorDe_Code\000000000205.jpg"
    g = 5  # 循环群G的生成元
    # try:
    #     image = Image.open(image_path)
    # except FileNotFoundError:
    #     print("文件不存在！")
    #     return
    # except Exception as e:
    #     print("发生错误：", e)
    #     return

    # 图像预处理
    processed_image = preprocess_image(image)

    # 哈希加密
    hashed_image = hash_image(processed_image)
    # print(hashed_image)

    # 计算指数运算
    result = calculate_exponentiation(hashed_image, g)
    return result


# if __name__ == "__main__":
#     S_time=time.time()
#     main()
#     E_time=time.time()
#     print(E_time-S_time)
