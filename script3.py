import yaml
from yaml import loader

import script2, script1
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def decrypted_text(symmetric_key, path_to_enc_file, path_to_dec_file) -> str:
    """дешифрование текста"""
    with open(script1.get_path(path_to_enc_file), "r") as _file:
        content_encrypted = yaml.safe_load(_file)
    text_enc = content_encrypted["text"]
    iv_enc = content_encrypted["iv"]
    cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv_enc))
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(text_enc) + decryptor.finalize()
    with open(script1.get_path(path_to_dec_file), "wb")as f:
        f.write(dc_text)
    return dc_text