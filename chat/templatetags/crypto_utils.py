# crypto_utils.py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from Cryptodome.Random import get_random_bytes
from cryptography.fernet import Fernet

class CryptoUtils:
    key = Fernet.generate_key()
    def generate_fernet_key():
        return Fernet.generate_key()

    def encrypt_message(message, key):
        cipher_suite = Fernet(key)
        encrypted_message = cipher_suite.encrypt(message.encode('utf-8'))
        return encrypted_message

# Function to decrypt message
    def decrypt_message(encrypted_message, key):
        cipher_suite = Fernet(key)
        decrypted_message = cipher_suite.decrypt(encrypted_message).decode('utf-8')
        return decrypted_message
