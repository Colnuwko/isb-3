import script1
import os
import yaml
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, padding as padding2
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import load_pem_private_key


def deserialization_private_key(secret_key_path: str) -> bytes:
    """десериализация закрытого ключа в файл, на вход берём путь до приватного ключа"""
    with open(script1.get_path(secret_key_path), "rb") as pem_in:
        private_bytes = pem_in.read()
    private_key = load_pem_private_key(private_bytes, password=None)
    return private_key


def decode_sym_key(path_to_sym_key, private_key) -> str:
    """дешифрование симметричного ключа асимметричным алгоритмом вернёт d_symmetric_key"""
    with open(script1.get_path(path_to_sym_key), "rb") as f:
        dec_key = f.read()
        symmetrical_key = private_key.decrypt(dec_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                    algorithm=hashes.SHA256(),
                                                                    label=None,
                                                                    )
                                              )
        return symmetrical_key


def padding_text(bit) -> str:
    """паддинг данных для работы блочного шифра (делаем длину сообщения кратной длине шифруемого блока"""
    with open(script1.get_path("initial_file"), "r") as file:
        content = file.read()
    padder = padding2.ANSIX923(int(bit*8)).padder()
    text = bytes(content, "UTF-8")
    padded_text = padder.update(text) + padder.finalize()
    return padded_text


def encrypted_text_symmetric_algorithm(symmetric_key, bit):
    """шифрование текста симметричным алгоритмом, ничего не вернёт"""
    padded_text = padding_text(bit)
    iv = os.urandom(int(bit))
    cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    text = encryptor.update(padded_text) + encryptor.finalize()
    dict = {"text": text, "iv": iv}
    with open(script1.get_path("encrypted_file"), "w") as _file:
        yaml.dump(dict, _file)
