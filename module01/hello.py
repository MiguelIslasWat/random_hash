'''
def add(x, y):
    'This function adds two numbers'
    return x + y

print(add(1, 1))
'''
import hashlib
import secrets

def find_hash_with_two_leading_zeros(max_tries: int = 1000) -> bool:
    """
    Genera hashes MD5 (32 chars hex) a partir de bytes aleatorios.
    Se detiene en cuanto encuentra uno que inicia con '00'.
    Retorna True si lo encontró; False si no en max_tries intentos.
    """
    for _ in range(max_tries):
        # 32 bytes aleatorios -> MD5 -> 32 caracteres hex
        h = hashlib.md5(secrets.token_bytes(32)).hexdigest()
        if h.startswith("00"):
            return True
    return False

# Ejemplo de uso:
if __name__ == "__main__":
    passed = find_hash_with_two_leading_zeros()
    print(passed)