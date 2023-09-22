import help_function
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os


def generation_sym_key(bit: int) -> bytes:
    """генерация и сохранение ключа симметричного алгоритма шифрования"""
    sym_key = os.urandom(bit)
    return sym_key


def save_sym_key(sym_key: bytes) -> None:
    with open(help_function.get_path("path_to_sym_key"), "wb") as f:
        f.write(sym_key)


def load_sym_key() -> bytes:
    with open(help_function.get_path("path_to_sym_key"), "rb") as f:
        return f.read()


def symmetric_encrypt(sym_key: bytes, text: bytes) -> None:
    """шифрование текста при помощи симметричного ключа и сохранение в файл"""
    padder = padding.ANSIX923(128).padder()
    padded_text = padder.update(text) + padder.finalize()
    iv = os.urandom(16)
    cipher = Cipher(algorithms.SEED(sym_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(padded_text) + encryptor.finalize()
    dict = {"text": cipher_text, "iv": iv}
    with open(help_function.get_path("path_to_encrypted_file"), "wb") as _file:
        _file.write(dict["iv"] + dict["text"])


def symmetric_decrypt(sym_key: bytes, encrypted_text: bytes) -> None:
    """Дешифрование текста с помощью симеметричного ключа и сохранение в файл"""
    iv = encrypted_text[:16]
    cipher_text = encrypted_text[16:]
    cipher = Cipher(algorithms.SEED(sym_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    text = decryptor.update(cipher_text) + decryptor.finalize()
    unpadder = padding.ANSIX923(128).unpadder()
    unpadded_text = unpadder.update(text) + unpadder.finalize()
    with open(help_function.get_path("path_to_decrypted_file"), "wb") as _file:
        _file.write(unpadded_text)
