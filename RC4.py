import os
from Crypto.Cipher import ARC4
from PIL import Image
import io

def generate_key(length=16):
    return os.urandom(length)

def encrypt_image(input_file):
    # 生成随机密钥
    key = generate_key()

    # 读取原始图像文件内容
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # 使用 RC4 加密算法进行加密
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(plaintext)

    return ciphertext, key

def decrypt_image(ciphertext, key):
    # 使用之前生成的密钥对加密后的内容进行解密
    cipher = ARC4.new(key)
    plaintext = cipher.decrypt(ciphertext)

    return plaintext

# def display_image(data):
#     image = Image.open(io.BytesIO(data))
#     image.show()
#
# # 测试加密和解密
# input_image = r'H:\ColorDe_Code\000000000205.jpg'
#
# # 加密图像
# encrypted_data, key = encrypt_image(input_image)
# print("Image encrypted successfully.")
#
# # 解密图像
# decrypted_data = decrypt_image(encrypted_data, key)
# print("Image decrypted successfully.")
#
# # 显示解密后的图像
# display_image(decrypted_data)
