import script1


def point_1():
    script1.load_settings()
    symmetrical_key = script1.generation_key_symmetric(32, "symmetric_key")
    private_key = script1.generation_private_key()
    public_key = script1.generation_public_key(private_key)
    script1.serialiaztion_private_key(private_key, "secret_key")
    script1.serialiaztion_public_key(public_key, "public_key")
    script1.encrypted_sym_key(symmetrical_key, public_key, "enc_symmetric_key")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    point_1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
