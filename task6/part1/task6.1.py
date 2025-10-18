from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key

with open("task_message.txt", "r") as msg_file:
    message = bytes.fromhex(msg_file.read())
with open("task_signature.txt", "r") as sign_file:
    sign = bytes.fromhex(sign_file.read())
with open("task_pub.pem", "rb") as key_file:
    pubkey = load_pem_public_key(key_file.read())

try:
    pubkey.verify(
        sign,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("Success")
except Exception:
    print("Failed")
