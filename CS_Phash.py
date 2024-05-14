import cv2
import numpy as np
import time


def OutP(image):
    # # 定义数组A和B
    # A = entropies # 生成随机数组A，范围在0到99之间
    # B = segmented_mean_entropies  # 生成随机数组B，范围在0到99之间

    # # 读取图像
    # image = cv2.imread(r'H:\ColorDe_Code\000000000205.jpg')

    # 1. 将图像灰度化
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 2. 重置图像为128*128
    resized_image = cv2.resize(gray_image, (128, 128))

    # 3. 对图像执行DCT变换
    dct_image = cv2.dct(np.float32(resized_image))

    # 4. 求出DCT变换后的平均值
    mean_value = np.mean(dct_image)

    # 5. 将小于平均值的设为0
    dct_image[dct_image < mean_value] = 0

    # 6. 将DCT变换后的利用采用插值法重组为256*256灰度图像
    interpolated_image = cv2.idct(dct_image)

    # 7. 将256*256灰度图像均分成64分子图像
    sub_images = np.array_split(interpolated_image, 64)

    # 8. 求每份子图像的灰度熵
    entropies = [cv2.calcHist([sub_image.astype(np.uint8)], [0], None, [256], [0, 256]) for sub_image in sub_images]
    entropies = [-np.sum(p * np.log2(p + 1e-6)) for p in entropies]  # A
    # print(entropies)

    # 9. 求出1-16，17-32，33-48，49-64灰度熵的均值
    segmented_entropies = [entropies[i:i + 16] for i in range(0, 64, 16)]
    segmented_mean_entropies = [np.mean(segment) for segment in segmented_entropies]  # B
    # print(segmented_mean_entropies)

    # # 10. 将1-64的灰度熵分别与4份灰度熵的均值比较，若大于均值设为1，小于均值设为0
    # binary_values = []
    # for entropy in entropies:
    #     segment_index = int((entropy - 1e-6) / 16)  # 计算所在的段索引
    #     binary_value = 1 if entropy > segmented_mean_entropies[segment_index] else 0
    #     binary_values.append(binary_value)

    # 将A数组中的每个数与B数组中的每个数比较，大于B中数则取为1，反之为0
    result = []
    for num_A in entropies:
        for num_B in segmented_mean_entropies:
            if num_A > num_B:
                result.append(1)
            else:
                result.append(0)

    # 将结果组成256位长的字符串
    binary_string = ''.join(map(str, result))
    binary_string_256 = binary_string[:256]
    return binary_string_256
    # print(binary_string_256)

#
# if __name__ == "__main__":
#     Start_time = time.time()
#     time.sleep(1)
#     OutP(cv2.imread(r'H:\ColorDe_Code\000000000205.jpg'))
#     End_time = time.time()
#
#     print(End_time - Start_time)
