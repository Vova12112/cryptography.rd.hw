from binascii import hexlify

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh, rsa, padding
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PublicFormat,
    PrivateFormat,
    NoEncryption,
)
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

# Загальні параметри DH спільні для всіх учасників і узгоджуються на рівні протоколу.
print("Generating parameters...")
parameters = dh.generate_parameters(generator=2, key_size=2048)
print("\nModule:\n", parameters.parameter_numbers().p)
print("\nGen:", parameters.parameter_numbers().g)

# Довгострокові 
alice_rsa = rsa.generate_private_key(public_exponent=65537, key_size=2048)
bob_rsa   = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Ефемерні 
alice_dh_priv, bob_dh_priv = parameters.generate_private_key(), parameters.generate_private_key()
alice_dh_pub,  bob_dh_pub  = alice_dh_priv.public_key(),  bob_dh_priv.public_key()

alice_dh_bytes = alice_dh_pub.public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)
bob_dh_bytes   = bob_dh_pub .public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)

alice_sig = alice_rsa.sign(
    alice_dh_bytes,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)
bob_sig = bob_rsa.sign(
    bob_dh_bytes,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)

alice_rsa_pub = alice_rsa.public_key()
bob_rsa_pub   = bob_rsa.public_key()

alice_rsa_pub.verify(
    alice_sig, alice_dh_bytes,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)

bob_rsa_pub.verify(
    bob_sig, bob_dh_bytes,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256(),
)

alice_shared = alice_dh_priv.exchange(bob_dh_pub)
bob_shared   = bob_dh_priv.exchange(alice_dh_pub)

def hkdf(x: bytes) -> bytes:
    return HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b"auth-DH").derive(x)

alice_key, bob_key = hkdf(alice_shared), hkdf(bob_shared)

print("Shared equal? ", alice_shared == bob_shared)
print("Key (Alice)  ", hexlify(alice_key))
print("Key (Bob)    ", hexlify(bob_key))