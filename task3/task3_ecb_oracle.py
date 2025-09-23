import requests
import json

def encrypt(hex):
    """Obtain ciphertext (encryption) for plaintext"""
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/" + hex
    r = requests.get(url)
    ct = (json.loads(r.text))["ciphertext"]
    return ct

def print_ciphertext(ct):
    """Print ciphertext by block"""
    parts = [ct[i : i + 32] for i in range(0, len(ct), 32)]
    for p in parts:
        print(p)

def is_blocks_equals(ct, blockNum1, blockNum2):
    """Check is specified blocks same"""
    parts = [ct[i : i + 32] for i in range(0, len(ct), 32)];
    if len(parts) > max(blockNum1, blockNum2):
        if parts[blockNum1] == parts[blockNum2]:
            return True;
    return False;

def find_next_byte(knownPart, rangeBytes, bufferSize = 64):
    """Find next byte of flag"""
    emptyBufferSize = bufferSize - (len(knownPart) + 2);
    stub            = "0" * emptyBufferSize;
    ethalon         = stub + knownPart;
    actualBlock     = (int)(bufferSize / 32);
    for possibleByte in rangeBytes:
        hexByte = format(possibleByte, "02x");
        cipher = encrypt(ethalon + hexByte + stub);
        if is_blocks_equals(cipher, actualBlock - 1, (actualBlock * 2) - 1):
            return knownPart + hexByte;
    return knownPart + "##";

knownPart = "";

for i in range(32):
    knownPart = find_next_byte(knownPart, range(31, 127));
    print(knownPart)