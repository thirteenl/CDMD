from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
from PIL import Image
import io
import secrets


def generate_key():
    return secrets.token_bytes(16)


def encrypt_image(image_path):
    key = generate_key()
    cipher = CryptSM4()
    cipher.set_key(key, SM4_ENCRYPT)

    with open(image_path, 'rb') as f:
        image_data = f.read()

    encrypted_data = cipher.crypt_ecb(image_data)

    return encrypted_data, key


def decrypt_image(encrypted_data, key):
    cipher = CryptSM4()
    cipher.set_key(key, SM4_DECRYPT)

    decrypted_data = cipher.crypt_ecb(encrypted_data)
    # image = Image.open(io.BytesIO(decrypted_data))
    # image.show()
    return decrypted_data


# # 加密图像
# encrypted_data, key = encrypt_image(r'H:\ColorDe_Code\000000000205.jpg')
#
# # 解密图像并显示
# decrypt_and_display_image(encrypted_data, key)
