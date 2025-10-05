import requests
import json


def encrypt(plaintext):
    """Obtain ciphertext (encryption) for plaintext"""
    url = "http://aes.cryptohack.org/lazy_cbc/encrypt/" + plaintext;
    r = requests.get(url);
    #return r.text;
    return (json.loads(r.text));

def receive(ciphertext):
    """Receive ciphertext"""
    url = "http://aes.cryptohack.org/lazy_cbc/receive/" + ciphertext;
    r = requests.get(url);
    return (json.loads(r.text));

def get_flag(key):
    """Obtain flag if key is valid"""
    url = "http://aes.cryptohack.org/lazy_cbc/get_flag/" + key;
    r = requests.get(url);
    return (json.loads(r.text));

def print_ciphertext(ct):
    """Print ciphertext by block"""
    parts = [ct[i : i + 32] for i in range(0, len(ct), 32)]
    for p in parts:
        print(p);
        
def find_next_nibble(plaintext, ciphertext, position, blockSize):
    """Brute next IV nibble"""
    nibbles = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'];
    for possibleNibble in nibbles:
        iv = ('0' * (position)) + possibleNibble + '0' * ((blockSize * 2) - position - 1);
        pt = receive( iv + ciphertext + "00000000000000000000000000000000")['error'];
        newPlaintext = pt.replace("Invalid plaintext: ", "");
        if newPlaintext[(blockSize * 2) + position] == plaintext[position]:
            return possibleNibble;
    return '?';
        
def find_iv(ethalonPlaintext, ethalonCyphertext, blockSize = 16):
    """Brute IV by known plain and cypher texts"""
    currentIv    = "";
    knownNibbles = 0;
    while knownNibbles < blockSize * 2:
        nextNibble = find_next_nibble(ethalonPlaintext, ethalonCyphertext, knownNibbles, blockSize);
        currentIv += nextNibble;
        knownNibbles += 1;
    return currentIv;
    
    
        
#              0123456789abcdef0123456789abcdef
#ct = encrypt("000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000");  
#print(ct);
#print('---------------------------------');
#if "ciphertext" in ct:
#    print_ciphertext(ct['ciphertext']);
#
#  Get results: ffd8c93b9c3a8fb8d325f520549a551c d4d7c7f76d6541c5515721021fd7da75 a5752598167012c086c1ec13acbfc007
#

#              000000000000000000000000000000001111111111111111111111111111111100000000000000000000000000000000
#pt = receive("00000000000000000000000000000000ffd8c93b9c3a8fb8d325f520549a551c");  
#print(pt);

#print("IV: " + find_iv("00000000000000000000000000000000", "ffd8c93b9c3a8fb8d325f520549a551c", ));
#
#  Get results: 4d66727acc9652f2abc06f1718c76464
#

print(get_flag("4d66727acc9652f2abc06f1718c76464"));
#
#  Get results: {'plaintext': '63727970746f7b35306d335f703330706c335f64306e375f3768316e6b5f49565f31355f316d70307237346e375f3f7d'}
#