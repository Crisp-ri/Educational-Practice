from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.backends import default_backend
import os

message = b"Hello world"

# SHA-256 (гешування)
digest = hashes.Hash(hashes.SHA256())
digest.update(message)
hash_value = digest.finalize()
print("SHA-256:", hash_value)

# AES (симетричне шифрування)
key = os.urandom(32)
iv = os.urandom(16)

padder = sym_padding.PKCS7(128).padder()
padded_data = padder.update(message) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
encrypted = encryptor.update(padded_data) + encryptor.finalize()
print("AES encrypted:", encrypted)

decryptor = cipher.decryptor()
decrypted_padded = decryptor.update(encrypted) + decryptor.finalize()

unpadder = sym_padding.PKCS7(128).unpadder()
decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()
print("AES decrypted:", decrypted)

# RSA (ключі + підпис)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print("RSA signature:", signature)

public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Підпис перевірено")

# Різниця:
# гешування — незворотне (hash не можна відновити)
# шифрування — зворотне (можна розшифрувати ключем)
