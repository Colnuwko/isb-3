import argparse
import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

import os


### вЫПОЛНИМ 1 ПУНКТ


def load_settings():
    settings = {
        "decrypted_file": "C:/Users/Солнышко/PycharmProjects/isb-3/decrypted/dec_file.txt",
        "encrypted_file": "C:/Users/Солнышко/PycharmProjects/isb-3/encrypted/enc_file.txt",
        "initial_file": "C:/Users/Солнышко/PycharmProjects/isb-3/initial_file.txt",
        "public_key": "C:/Users/Солнышко/PycharmProjects/isb-3/public_key/public_key.pem",
        "secret_key": "C:/Users/Солнышко/PycharmProjects/isb-3/private_key/secret_key.pem",
        "symmetric_key": "C:/Users/Солнышко/PycharmProjects/isb-3/symmetrical_key/key.txt",
        "enc_symmetric_key": "C:/Users/Солнышко/PycharmProjects/isb-3/symmetrical_key/enc_key.txt"
    }
    with open('settings.json', 'w') as fp:
        json.dump(settings, fp)


def get_path(file_name):
    with open('settings.json') as json_file:
        json_data = json.load(json_file)
        return json_data[file_name]


def generation_key_symmetric(bit, name) -> bytes:
    """генерация ключа симметричного алгоритма шифрования"""
    sym_key = os.urandom(bit)
    with open(get_path(name),"wb")as f:
        f.write(sym_key)

    return sym_key


def generation_private_key():
    """генерация пары ключей для асимметричного алгоритма шифрования или приватный ключ"""
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def generation_public_key(key):
    """генерация открытого ключа"""
    return key.public_key()


def serialiaztion_public_key(key, name):
    """сериализация открытого ключа"""
    with open(get_path(name), "wb") as file:
        file.write(key.public_bytes(encoding=serialization.Encoding.PEM,
                                    format=serialization.PublicFormat.SubjectPublicKeyInfo, ))


def serialiaztion_private_key(key, name):
    """сериализация закрытого ключа"""
    with open(get_path(name), "wb") as file:
        file.write(key.private_bytes(encoding=serialization.Encoding.PEM,
                                     format=serialization.PrivateFormat.TraditionalOpenSSL,
                                     encryption_algorithm=serialization.NoEncryption()))


def encrypted_sym_key(sym_key, public_key, name):
    """шифрование симметричного ключа открытым ключом при помощи RSA-OAEP, вернёт encrypted_symmetric_key"""
    enc_public_key = public_key.encrypt(sym_key, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None, ))
    with open(get_path(name), "wb") as file:
        file.write(enc_public_key)
