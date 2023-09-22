import Asymmetric
import Symmetric
import help_function


def create_keys() -> tuple:
    """Создание всех ключей"""
    sym_key = Symmetric.generation_sym_key(16)
    private_key = Asymmetric.generation_private_key()
    public_key = Asymmetric.generation_public_key(private_key)
    result = (sym_key, private_key, public_key)
    return result


def save_keys(keys: tuple) -> None:
    """Сохранение ключей в соответствующие файлы"""
    Symmetric.save_sym_key(keys[0])
    Asymmetric.serialiaztion_private_key(keys[1])
    Asymmetric.serialiaztion_public_key(keys[2])
    print(3)


def load_keys() -> tuple:
    """Функция вернет кортеж из сохраненых ключей """
    keys = (Symmetric.load_sym_key(), Asymmetric.deserialization_private_key(), Asymmetric.deserialization_public_key())
    print(keys)
    return keys


def encrypt_text() -> None:
    """Шифруем текст симетричным алгоритм, после чего шифруем симметричный ключ асимметричным алгоритмом"""
    Symmetric.symmetric_encrypt(Symmetric.load_sym_key(), help_function.get_text_in_bytes("path_to_initial_file"))
    Asymmetric.asymmetric_encrypt(Asymmetric.deserialization_public_key(), Symmetric.load_sym_key())


def decrypt_text() -> None:
    """Расшифровывем симметричный ключ асиметричным ключом. Дешифруем текст"""
    print(1)
    Asymmetric.asymmetric_decrypt(Asymmetric.deserialization_private_key(), help_function.get_text_in_bytes("path_to_enc_key_asym"))
    print(2)
    Symmetric.symmetric_decrypt(help_function.get_text_in_bytes("path_to_dec_key_asym"),
                                help_function.get_text_in_bytes("path_to_encrypted_file"))
