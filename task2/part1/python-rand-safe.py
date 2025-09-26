import secrets

with open("rnd-python-safe.bin","wb") as f:
    for _ in range(1024 * 1024 * 256):
        f.write(secrets.randbits(32).to_bytes(4, "little"));