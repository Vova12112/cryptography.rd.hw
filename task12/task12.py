import hashlib
from dataclasses import dataclass, asdict
from typing import List

DIFFICULTY = 5

@dataclass
class Block:
    data: int
    prev_hash: str
    nonce: int = 0
    hash: str = ""

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def hash_block(data: int, prev_hash: str, nonce: int) -> str:
    payload = f"{data}|{prev_hash}|{nonce}".encode("utf-8")
    return sha256_hex(payload)

def mine_block(block: Block, difficulty: int = DIFFICULTY) -> Block:
    prefix = "0" * difficulty
    nonce = 0
    while True:
        h = hash_block(block.data, block.prev_hash, nonce)
        if h.startswith(prefix):
            block.nonce = nonce
            block.hash = h
            return block
        nonce += 1

class Blockchain:
    def __init__(self, difficulty: int = DIFFICULTY):
        self.difficulty = difficulty
        self.chain: List[Block] = []
        genesis = Block(data=0, prev_hash="")
        self.chain.append(mine_block(genesis, self.difficulty))

    def add_block(self, data: int) -> Block:
        prev_hash = self.chain[-1].hash
        blk = Block(data=data, prev_hash=prev_hash)
        mined = mine_block(blk, self.difficulty)
        self.chain.append(mined)
        return mined

    def is_valid(self) -> bool:
        prefix = "0" * self.difficulty
        for i, blk in enumerate(self.chain):
            if not blk.hash.startswith(prefix):
                return False
            if blk.hash != hash_block(blk.data, blk.prev_hash, blk.nonce):
                return False
            if i > 0 and blk.prev_hash != self.chain[i-1].hash:
                return False
        return True

if __name__ == "__main__":
    values = [91911, 90954, 95590, 97390, 96578, 97211, 95090]
    bc = Blockchain(difficulty=DIFFICULTY)
    for v in values:
        mined = bc.add_block(v)
        print(f"Block#{len(bc.chain)-1} data={v} nonce={mined.nonce} hash={mined.hash}")

    for i, blk in enumerate(bc.chain):
        print(f"\n[{i}] {asdict(blk)}")