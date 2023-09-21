import Asymmetric
import Symmetric
import help_function


def create_keys() -> tuple:
    sym_key = Symmetric.generation_sym_key(16)
    private_key = Asymmetric.generation_private_key()
    public_key = Asymmetric.generation_public_key(private_key)
