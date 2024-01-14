# custom_filters.py
# from . views import decrypt_message
from .crypto_utils import CryptoUtils
from django import template
from django.utils import timezone
import base64

from Cryptodome.Cipher import AES
register = template.Library()
@register.filter(name='format_date_day')
@register.filter
def format_date(value):
    today = timezone.now().date()
    yesterday = today - timezone.timedelta(days=1)

    if value.date() == today:
        return "Today"
    elif value.date() == yesterday:
        return "Yesterday"
    else:
        return value.strftime("%a, %b %d")
# @register.filter
# def decrypt_message(chat, *args, **kwargs):
#     encrypted_message = chat.body
#     key = chat.encryption_key
#     iv = chat.encryption_iv

#     cipher = AES.new(base64.b64decode(key), AES.MODE_CBC, base64.b64decode(iv))
#     decrypted_message = cipher.decrypt(base64.b64decode(encrypted_message)).decode('utf-8')
#     return decrypted_message
    
# @register.filter
# def base64decode(value):
#     try:
#         decoded_bytes = base64.b64decode(value)
#         return decoded_bytes.decode('utf-8')
#     except:
#         return value

@register.filter(name='encrypt_message')
def encrypt_message(value, key):
    crypto_utils = CryptoUtils()
    encrypted_message = crypto_utils.encrypt_message(value, key)
    return encrypted_message

@register.filter(name='decrypt_message')
def decrypt_message(encrypted_text, key):
    # Ensure that the decrypt_message method accepts three arguments (encrypted_text, key, and any additional argument)
    decrypted_text = CryptoUtils.decrypt_message(encrypted_text, key)
    return decrypted_text