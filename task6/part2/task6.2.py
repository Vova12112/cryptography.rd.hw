from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key

with open("task_pub.pem", "rb") as key_file:
    pubkey = load_pem_public_key(key_file.read())

message = "TOP SECRET MESSAGE".encode("utf-8")

encrypted = pubkey.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open("task-2-message.txt", "w") as f:
    f.write(encrypted.hex())
