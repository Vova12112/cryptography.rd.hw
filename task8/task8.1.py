from binascii import hexlify
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, x25519
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat

alice_pub_sign_key_raw = b"""-----BEGIN PUBLIC KEY-----
MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAES/35y89DRx2XEh6pJvCckadQ9Awuys84
HORPVVaDksVxWfSkngYrz/c+HwVS9tV5ivnVwCHxyJ8gTQob/0LDDg==
-----END PUBLIC KEY-----"""
alice_x_pub_hex = b'92ce3bc6d941238da92639c72a7d3bb483d3c18fdca9f42164459a3751638433'
alice_sig_hex   = b'3045022034b7944bf92bfaa2791b5fe929d915add4ee59dbd9e776c1520568fbf2503048022100f09c9113f38fadb33b05332eab9a4982f7dda35fb1f503bb46da806c8e8dbaa2'

alice_sign_pub = serialization.load_pem_public_key(alice_pub_sign_key_raw)
alice_x_pub    = bytes.fromhex(alice_x_pub_hex.decode())
alice_sig_der  = bytes.fromhex(alice_sig_hex.decode())

bob_sign_priv = ec.generate_private_key(ec.SECP256K1())
bob_sign_pub  = bob_sign_priv.public_key()

bob_x_priv = x25519.X25519PrivateKey.generate()
bob_x_pub_bytes = bob_x_priv.public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)

alice_sign_pub.verify(alice_sig_der, alice_x_pub, ec.ECDSA(hashes.SHA256()))

shared = bob_x_priv.exchange(x25519.X25519PublicKey.from_public_bytes(alice_x_pub))

bob_sig_der = bob_sign_priv.sign(bob_x_pub_bytes, ec.ECDSA(hashes.SHA256()))

bob_sign_pub_pem = bob_sign_pub.public_bytes(
    serialization.Encoding.PEM,
    serialization.PublicFormat.SubjectPublicKeyInfo,
)

bob_y_hex      = hexlify(bob_x_pub_bytes).decode()
bob_y_sig_hex  = hexlify(bob_sig_der).decode()

with open("task8_bob.txt", "w", encoding="utf-8") as f:
    f.write("=== Bob signing public key (PEM) ===\n")
    f.write(bob_sign_pub_pem.decode())
    f.write("\n=== Bob ECDH public (Y) hex ===\n")
    f.write(bob_y_hex + "\n")
    f.write("\n=== Signature(ECDSA-SECP256K1, SHA-256) of Y (DER hex) ===\n")
    f.write(bob_y_sig_hex + "\n")

print("Result saved task8_bob.txt")