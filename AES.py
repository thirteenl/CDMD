from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
from PIL import Image
import io

# AES加密块大小（16字节）
AES_BLOCK_SIZE = 16


def pad(data):
    """填充数据以确保它是AES块大小的整数倍"""
    length = AES_BLOCK_SIZE
    count = len(data)
    add = length - (count % length)
    return data + (add * chr(add)).encode()


def aes_encrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data)
    encrypted_data = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted_data)


def aes_decrypt(encrypted_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(base64.b64decode(encrypted_data))
    unpadded_data = decrypted_data[:-decrypted_data[-1]]
    return unpadded_data


def encrypt_image(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    key = get_random_bytes(32)  # 生成16字节的随机密钥
    encrypted_data = aes_encrypt(image_data, key)
    return encrypted_data, key


def decrypt_image(encrypted_data, key):
    decrypted_data = aes_decrypt(encrypted_data, key)
    image = Image.open(io.BytesIO(decrypted_data))
    # print(key)
    return image


# # 使用示例
# image_path = r'H:\ColorDe_Code\000000000205.jpg' # 待加密的图像文件路径
# key = get_random_bytes(16)  # 生成16字节的随机密钥
#
# # 加密图像
# encrypted_image = encrypt_image(image_path, key)
#
# # 解密图像
# decrypted_image = decrypt_image(encrypted_image, key)
# print(encrypted_image)
# decrypted_image.show()  # 显示解密后的图像