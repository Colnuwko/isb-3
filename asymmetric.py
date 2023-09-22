import help_function
from typing import Any
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key


def generation_private_key() -> Any:
    """генерация пары ключей для асимметричного алгоритма шифрования"""
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def generation_public_key(key: Any) -> Any:
    """генерация открытого ключа"""
    return key.public_key()


def serialiaztion_public_key(public_key: Any) -> None:
    """сериализация открытого ключа"""
    with open(help_function.get_path("path_to_public_key"), "wb") as file:
        file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                           format=serialization.PublicFormat.SubjectPublicKeyInfo))


def serialiaztion_private_key(key: Any) -> None:
    """сериализация закрытого ключа"""
    with open(help_function.get_path("path_to_secret_key"), "wb") as file:
        file.write(key.private_bytes(encoding=serialization.Encoding.PEM,
                                     format=serialization.PrivateFormat.TraditionalOpenSSL,
                                     encryption_algorithm=serialization.NoEncryption()))


def deserialization_private_key() -> bytes:
    """десериализация закрытого ключа"""
    with open(help_function.get_path("path_to_secret_key"), "rb") as pem_in:
        private_bytes = pem_in.read()
    private_key = load_pem_private_key(private_bytes, password=None)
    return private_key


def deserialization_public_key() -> bytes:
    """десериализация открытоёго ключа"""
    with open(help_function.get_path("path_to_public_key"), "rb") as pem_in:
        public_bytes = pem_in.read()
    public_key = load_pem_public_key(public_bytes)
    return public_key


def asymmetric_encrypt(public_key: Any, text: bytes) -> None:
    """Шифрование симетричного ключа с помощью открытого ключа, из пары ключей несиметричного алгоритма"""
    encrypted_text = public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                           algorithm=hashes.SHA256(), label=None, ))
    with open(help_function.get_path("path_to_enc_key_asym"), "wb") as _file:
        _file.write(encrypted_text)


def asymmetric_decrypt(private_key, encrypted_text: bytes) -> bytes:
    """Дешифруем зашифрованный симметричный ключ с помощью закрытого ключа"""
    text = private_key.decrypt(encrypted_text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                            algorithm=hashes.SHA256(), label=None, ))
    with open(help_function.get_path("path_to_dec_key_asym"), "wb") as _file:
        _file.write(text)
    return text
