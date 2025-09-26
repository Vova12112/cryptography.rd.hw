import random

generator = random.Random();
with open("rnd-python-unsafe.bin","wb") as f:
    for _ in range(1024 * 1024 * 256):
        f.write(generator.randint(0, 2**32 - 1).to_bytes(4, "little"));