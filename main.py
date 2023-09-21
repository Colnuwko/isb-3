import Symmetric
import help_function
import Asymmetric



def work_sym_algoritm(bit: int) -> None:
    """Создание и сохранение симметричного ключа, шифрование и дешифрование текста с помощью созданого ключа
    запись в соответствующие файлы. Папка Files"""
    sym_key = Symmetric.generation_sym_key(bit)
    text_in_bytes = help_function.get_text_in_bytes("path_to_initial_file")
    Symmetric.symmetric_encrypt(sym_key, text_in_bytes)
    text_in_bytes = help_function.get_text_in_bytes("path_to_encrypted_file")
    Symmetric.symmetric_decrypt(sym_key, text_in_bytes)


def work_asym_algoritm(bit: int) -> None:
    private_key = Asymmetric.generation_private_key()
    public_key = Asymmetric.generation_public_key(private_key)

    Asymmetric.serialiaztion_public_key(public_key)
    Asymmetric.serialiaztion_private_key(private_key)

    private_key = Asymmetric.deserialization_private_key()
    public_key = Asymmetric.deserialization_public_key()

    sym_key = help_function.get_text_in_bytes("path_to_sym_key")
    Asymmetric.asymmetric_encrypt(public_key, sym_key)

    cipher_key = help_function.get_text_in_bytes("path_to_enc_key_asym")
    Asymmetric.asymmetric_decrypt(private_key, cipher_key)






def work_hybrid_algoritm() -> None:
    print(1)




