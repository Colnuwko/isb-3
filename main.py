import script1
import script2
import script3


def point_1(bit):

    symmetrical_key = script1.generation_key_symmetric(bit, "symmetric_key.txt")
    private_key = script1.generation_private_key()
    public_key = script1.generation_public_key(private_key)
    script1.serialiaztion_private_key(private_key, "secret_key.pem")
    script1.serialiaztion_public_key(public_key, "public_key.pem")
    script1.encrypted_sym_key(symmetrical_key, public_key, "enc_symmetric_key.txt")


def point_2(bit):
    private_key = script2.deserialization_private_key("secret_key.pem")
    symmetrical_key = script2.decode_sym_key("enc_symmetric_key.txt", private_key)
    script2.encrypted_text_symmetric_algorithm(symmetrical_key, bit)
# Press the green button in the gutter to run the script.


def point_3():
    private_key = script2.deserialization_private_key("secret_key.pem")
    symmetrical_key = script2.decode_sym_key("enc_symmetric_key.txt", private_key)
    script3.decrypted_text(symmetrical_key, "encrypted_file.yaml", "decrypted_file.txt")

if __name__ == '__main__':
    point_1(16)
    point_2(16)
    point_3()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
