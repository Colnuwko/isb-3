import Symmetric
import help_function
import Asymmetric
import script3


def work_sym_algoritm(bit: int) -> None:
    """Создание и сохранение симметричного ключа, шифрование и дешифрование текста с помощью созданого ключа
    запись в соответствующие файлы. Папка Files"""
    sym_key = Symmetric.generation_sym_key(bit)
    text_in_bytes = help_function.get_text_in_bytes("path_to_initial_file")
    Symmetric.symmetric_encrypt(sym_key, text_in_bytes)
    text_in_bytes = help_function.get_text_in_bytes("path_to_encrypted_file")
    Symmetric.symmetric_decrypt(sym_key, text_in_bytes)


def work_asym_algoritm(bit: int) -> None:
    private_key = script2.deserialization_private_key("secret_key.pem")
    symmetrical_key = script2.decode_sym_key("enc_symmetric_key.txt", private_key)
    script2.encrypted_text_symmetric_algorithm(symmetrical_key, bit)




def point_3():
    private_key = script2.deserialization_private_key("secret_key.pem")
    symmetrical_key = script2.decode_sym_key("enc_symmetric_key.txt", private_key)
    script3.decrypted_text(symmetrical_key, "encrypted_file.yaml", "decrypted_file.txt")


if __name__ == '__main__':
    point_1(16)
    point_2(16)
    point_3()


