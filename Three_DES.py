from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
from PIL import Image
import io




def des_encrypt(data, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_data = pad(data, DES3.block_size)  # 对数据进行填充
    encrypted_data = cipher.encrypt(padded_data)
    return base64.b64encode(encrypted_data)


def des_decrypt(encrypted_data, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_data = cipher.decrypt(base64.b64decode(encrypted_data))
    unpadded_data = unpad(decrypted_data, DES3.block_size)  # 移除填充
    return unpadded_data


def encrypt_image(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    # 密钥生成
    key = get_random_bytes(24)
    encrypted_data = des_encrypt(image_data, key)
    return encrypted_data, key


def decrypt_image(encrypted_data, key):
    decrypted_data = des_decrypt(encrypted_data, key)

    # 将解密后的字节数据转换回图像对象
    image_obj = Image.open(io.BytesIO(decrypted_data))
    return image_obj


# # 使用示例
# image_path = r'H:\ColorDe_Code\000000000205.jpg'  # 图片路径
# encrypted_data = encrypt_image(image_path, key)
# decrypted_image = decrypt_image(encrypted_data, key)
# print(encrypted_data)
# decrypted_image.show()  # 显示解密后的图片