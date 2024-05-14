import hashlib
from PIL import Image
import time


def split_image(image, num_blocks):
    width, height, _ = image.shape
    block_size_x = width // num_blocks
    block_size_y = height // num_blocks
    blocks = []
    for y in range(num_blocks):
        for x in range(num_blocks):
            left = x * block_size_x
            upper = y * block_size_y
            right = left + block_size_x
            lower = upper + block_size_y

            block = image[left:right, upper:lower]
            blocks.append(block)
    return blocks


def hash_block(block):
    hash_object = hashlib.sha256()
    hash_object.update(block.tobytes())
    return hash_object.hexdigest()


def sha256_main(image):
    # image_path = r'H:\ColorDe_Code\000000000081.jpg'  # 替换为你的图像路径
    num_blocks = 4  # 分成的块数
    # image = Image.open(image_path)
    blocks = split_image(image, num_blocks)
    hashed_blocks = []
    for block in blocks:
        hashed_block = hash_block(block)
        hashed_blocks.append(hashed_block)
    return hashed_blocks
    # print("Hashed Blocks:", hashed_blocks)

# if __name__ == "__main__":
#     S_time = time.time()
#     main()
#     End_time = time.time()
#     print(End_time - S_time)
