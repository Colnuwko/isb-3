import os
import yaml
import help_function
from typing import Any
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import padding as padding2, serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key


def generation_private_key() -> Any:
    """генерация пары ключей для асимметричного алгоритма шифрования"""
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def generation_public_key(key: Any) -> Any:
    """генерация открытого ключа"""
    return key.public_key()


def serialiaztion_public_key(key: Any) -> None:
    """сериализация открытого ключа"""
    with open(help_function.get_path("path_to_public_key"), "wb") as file:
        file.write(key.public_bytes(encoding=serialization.Encoding.PEM,
                                    format=serialization.PublicFormat.SubjectPublicKeyInfo, ))


def serialiaztion_private_key(key: Any) -> None:
    """сериализация закрытого ключа"""
    with open(help_function.get_path("path_to_secret_key"), "wb") as file:
        file.write(key.private_bytes(encoding=serialization.Encoding.PEM,
                                     format=serialization.PrivateFormat.TraditionalOpenSSL,
                                     encryption_algorithm=serialization.NoEncryption()))


def deserializ_private_key() -> bytes:
    """десериализация закрытого ключа"""
    with open(help_function.get_path("path_to_secret_key"), "rb") as pem_in:
        private_bytes = pem_in.read()
    private_key = load_pem_private_key(private_bytes, password=None)
    print(type(private_key))
    return private_key


def deserialization_public_key() -> bytes:
    """десериализация открытоёго ключа"""
    with open(help_function.get_path("path_to_public_key"), "rb") as pem_in:
        private_bytes = pem_in.read()
    private_key = load_pem_public_key(private_bytes, password=None)
    print(type(private_key))
    return private_key






