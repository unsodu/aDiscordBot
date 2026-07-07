import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def _derive_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_message(message: str, password: str):
    salt = os.urandom(16)
    key = _derive_key(password, salt)
    f = Fernet(key)

    token = f.encrypt(message.encode())

    return base64.urlsafe_b64encode(salt).decode(), token.decode()

def decrypt_message(password: str, salt_b64: str, token: str):
    salt = base64.urlsafe_b64decode(salt_b64.encode())
    key = _derive_key(password, salt)
    f = Fernet(key)

    return f.decrypt(token.encode()).decode()