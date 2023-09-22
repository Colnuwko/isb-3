import asymmetric
import symmetric
import help_function


def create_keys() -> tuple:
    """Создание всех ключей"""
    sym_key = symmetric.generation_sym_key(16)
    private_key = asymmetric.generation_private_key()
    public_key = asymmetric.generation_public_key(private_key)
    result = (sym_key, private_key, public_key)
    return result


def save_keys(keys: tuple) -> None:
    """Сохранение ключей в соответствующие файлы"""
    aymmetric.save_sym_key(keys[0])
    asymmetric.serialiaztion_private_key(keys[1])
    asymmetric.serialiaztion_public_key(keys[2])
    print(3)


def load_keys() -> tuple:
    """Функция вернет кортеж из сохраненых ключей """
    keys = (symmetric.load_sym_key(), asymmetric.deserialization_private_key(), asymmetric.deserialization_public_key())
    print(keys)
    return keys


def encrypt_text() -> None:
    """Шифруем текст симетричным алгоритм, после чего шифруем симметричный ключ асимметричным алгоритмом"""
    symmetric.symmetric_encrypt(symmetric.load_sym_key(), help_function.get_text_in_bytes("path_to_initial_file"))
    asymmetric.asymmetric_encrypt(asymmetric.deserialization_public_key(), symmetric.load_sym_key())


def decrypt_text() -> None:
    """Расшифровывем симметричный ключ асиметричным ключом. Дешифруем текст"""
    print(1)
    asymmetric.asymmetric_decrypt(asymmetric.deserialization_private_key(), help_function.get_text_in_bytes("path_to_enc_key_asym"))
    print(2)
    symmetric.symmetric_decrypt(help_function.get_text_in_bytes("path_to_dec_key_asym"),
                                help_function.get_text_in_bytes("path_to_encrypted_file"))
