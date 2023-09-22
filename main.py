import hybrid
import symmetric
import help_function
import asymmetric



def work_sym_algoritm(bit: int) -> None:
    """Создание и сохранение симметричного ключа, шифрование и дешифрование текста с помощью созданого ключа
    запись в соответствующие файлы. Папка Files"""
    sym_key = symmetric.generation_sym_key(bit)
    symmetric.save_sym_key(sym_key)
    text_in_bytes = help_function.get_text_in_bytes("path_to_initial_file")
    symmetric.symmetric_encrypt(sym_key, text_in_bytes)
    text_in_bytes = help_function.get_text_in_bytes("path_to_encrypted_file")
    symmetric.symmetric_decrypt(sym_key, text_in_bytes)


def work_asym_algoritm() -> None:
    """Создание пары ключей асимметричного алгоритма, сериализация и десериализация ключей, шифрование и дешифрование
    симметричного ключа ассиметричным алгоритмом """
    private_key = asymmetric.generation_private_key()
    public_key = asymmetric.generation_public_key(private_key)

    asymmetric.serialiaztion_public_key(public_key)
    asymmetric.serialiaztion_private_key(private_key)

    private_key = asymmetric.deserialization_private_key()
    public_key = asymmetric.deserialization_public_key()

    sym_key = help_function.get_text_in_bytes("path_to_sym_key")
    asymmetric.asymmetric_encrypt(public_key, sym_key)

    cipher_key = help_function.get_text_in_bytes("path_to_enc_key_asym")
    asymmetric.asymmetric_decrypt(private_key, cipher_key)

def work_hybrid_algoritm() -> None:
    """Создаем и сохраняем все три вида кючей
    загружаем их из файлов и производим шифрования текста гибридным алгоритмом
    """
    keys = hybrid.create_keys()
    hybrid.save_keys(keys)
    hybrid.load_keys()
    hybrid.encrypt_text()
    hybrid.decrypt_text()
