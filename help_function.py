import json
from cryptography.hazmat.primitives.asymmetric import rsa, padding as padding2


def create_settings() -> None:
    """Создание начальных настроек"""
    settings = {
        "path_to_decrypted_file": "files/dec_file.txt",
        "path_to_encrypted_file": "files/enc_file.txt",
        "path_to_initial_file": "files/initial_file.txt",
        "path_to_public_key": "files/public_key.pem",
        "path_to_secret_key": "files/secret_key.pem",
        "path_to_sym_key": "files/key.txt",
        "path_to_enc_sym_key": "files/enc_key.txt"
    }
    with open('settings.json', 'w') as fp:
        json.dump(settings, fp)


def get_path(file_name: str) -> str:
    """По запросу возвращает путь до файла"""
    with open('settings.json') as json_file:
        json_data = json.load(json_file)
        return json_data[file_name]


def get_text_in_bytes(path_to_file: str) -> bytes:
    """Возвращает текст в битовом формате"""
    with open(get_path(path_to_file), mode='rb') as text_file:
        text = text_file.read()
        return text


def padding_text(bit) -> str:
    """паддинг данных для работы блочного шифра (делаем длину сообщения кратной длине шифруемого блока"""
    with open(get_path("path_to_initial_file"), "r") as file:
        content = file.read()
    padder = padding2.ANSIX923(int(bit * 8)).padder()
    text = bytes(content, "UTF-8")
    padded_text = padder.update(text) + padder.finalize()
    return padded_text










