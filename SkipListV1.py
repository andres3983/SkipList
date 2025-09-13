import hashlib, random, struct

# Canonical serialization
def canonical_bytes(arg):
    if isinstance(arg, int):
        if arg == 0:
            b = b'\x00'
        else:
            b = arg.to_bytes((arg.bit_length() + 7) // 8, 'big')
        return b'I' + struct.pack('>I', len(b)) + b
    elif isinstance(arg, str):
        b = arg.encode('utf-8')
        return b'S' + struct.pack('>I', len(b)) + b
    elif isinstance(arg, bytes):
        return b'B' + struct.pack('>I', len(arg)) + arg
    elif arg is None:
        return b'N' + struct.pack('>I', 0)
    else:
        b = str(arg).encode('utf-8')
        return b'S' + struct.pack('>I', len(b)) + b

def sha256(b: bytes) -> bytes:
    return hashlib.sha256(b).digest()

# Node and AuthSkipList
class Node:
    def __init__(self, level, key=None):
        self.level = level
        self.key = key
        self.down = None
        self.right = None
        self.rank = 0
        self.label = None
        self.raw_bytes = None
        self._data = None  

class AuthSkipList:
    def __init__(self, max_level=5):
        self.max_level = max_level
        self.level_heads = [Node(l, key=None) for l in range(max_level + 1)]
        for l in range(max_level, 0, -1):
            self.level_heads[l].down = self.level_heads[l - 1]
        self.head = self.level_heads[max_level]
        self.n = 0

    def _T_of(self, m):
        return sha256(canonical_bytes(str(m)))

    def random_level(self):
        lvl = 0
        while random.random() < 0.5 and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, key, fixed_level=None):
        level = self.random_level() if fixed_level is None else fixed_level
        update = [None] * (self.max_level + 1)
        cur = self.head
        for i in reversed(range(self.max_level + 1)):
            while cur.right and cur.right.key is not None and cur.right.key < key:
                cur = cur.right
            update[i] = cur
            if cur.down:
                cur = cur.down

        down_node = None
        for i in range(level + 1):
            nd = Node(i, key=key)
            nd._data = self._T_of(key) if i == 0 else None
            nd.down = down_node
            nd.right = update[i].right
            update[i].right = nd
            down_node = nd

        self.n += 1
        self.recompute()

    def recompute(self):
        # reset
        for lvl in range(self.max_level + 1):
            node = self.level_heads[lvl]
            while node:
                node.rank = 0
                node.label = None
                node.raw_bytes = None
                node = node.right

        cnt = 0
        node = self.level_heads[0].right
        while node:
            node.rank = 1 if node.key is not None else 0
            cnt += node.rank
            node = node.right
        self.level_heads[0].rank = cnt

        for lvl in range(1, self.max_level + 1):
            cur = self.level_heads[lvl].right
            while cur:
                nxt = cur.right
                d = cur.down
                bound = nxt.down if nxt else None
                s = 0
                while d is not None and d is not bound:
                    s += d.rank
                    d = d.right
                cur.rank = s
                cur = cur.right

        for lvl in range(self.max_level + 1):
            s = 0
            cur = self.level_heads[lvl].right
            while cur:
                s += cur.rank
                cur = cur.right
            self.level_heads[lvl].rank = s

        for lvl in range(self.max_level + 1):
            nodes = []
            cur = self.level_heads[lvl]
            while cur:
                nodes.append(cur)
                cur = cur.right
            for v in reversed(nodes):
                right_hash = v.right.label if (v.right and v.right.label) else b''
                if v.level == 0:
                    data = v._data if v._data is not None else b''
                    rb = (canonical_bytes(v.level) +
                          canonical_bytes(v.rank) +
                          canonical_bytes(data) +
                          canonical_bytes(right_hash))
                else:
                    down_hash = v.down.label if (v.down and v.down.label) else b''
                    rb = (canonical_bytes(v.level) +
                          canonical_bytes(v.rank) +
                          canonical_bytes(down_hash) +
                          canonical_bytes(right_hash))
                v.raw_bytes = rb
                v.label = sha256(rb)

    def atRank_with_paper_tuples(self, i):
        assert 1 <= i <= self.n
        cur = self.head
        seen = 0
        path = []
        while cur:
            path.append(cur)
            nxt = cur.right
            if nxt and (seen + nxt.rank) < i:
                seen += nxt.rank
                cur = nxt
            else:
                cur = cur.down
        node = self.level_heads[0].right
        steps = i - 1
        while steps > 0:
            node = node.right
            steps -= 1
        if path[-1] is not node:
            path.append(node)

        rev = list(reversed(path))  
        Pi = []
        for j, v in enumerate(rev, start=1):
            l = v.level
            prev_node = rev[j - 2] if j - 2 >= 0 else None
            if j == 1:
                d = 'rgt'
            else:
                d = 'rgt' if prev_node is v.right else 'dwn'
            if j == 1:
                sib = v.right
                q = sib.rank if sib else 0
            elif j > 1 and l == 0:
                q = 1
            elif j > 1 and l > 0 and d == 'rgt':
                down = v.down
                q = down.rank if down else 0
            else:
                rgt = v.right
                q = rgt.rank if rgt else 0
            if j == 1:
                sib = v.right
                g = (sib.label if sib and sib.label else b'').hex()
            elif j > 1 and l == 0:
                g = (v._data if v._data else b'').hex()
            elif j > 1 and l > 0 and d == 'rgt':
                down = v.down
                g = (down.label if down and down.label else b'').hex()
            else:
                rgt = v.right
                g = (rgt.label if rgt and rgt.label else b'').hex()
            Pi.append({
                'l': l,
                'q': q,
                'd': d,
                'g': g,
                'raw': v.raw_bytes.hex() if v.raw_bytes else ''
            })
        leaf = rev[0]
        T_hex = (leaf._data.hex() if leaf._data else '').lower()
        return T_hex, Pi

    def get_root(self):
        return self.head.label

# Verifier: replay raw bytes
def verify_by_replaying_raw(Mc, Pi):
    if not Pi:
        return False, 0
    raw_hex = Pi[-1].get('raw', "")
    if not raw_hex:
        return False, 0
    rb = bytes.fromhex(raw_hex)
    return (sha256(rb) == Mc), len(rb)

# === DEMO: Insert + Verify Ranks ===
if __name__ == "__main__":
    random.seed(1)
    asl = AuthSkipList(max_level=5)
    values = sorted(random.sample(range(1000, 9999), 32))
    for v in values:
        asl.insert(v)

    root = asl.get_root()
    print("Root:", root.hex())
    print(f"{'Rank':<6} {'Valid':<8} {'Bytes Hashed'}")

    total_bytes = 0
    all_ok = True
    for rank in range(1, len(values) + 1):
        T_hex, Pi = asl.atRank_with_paper_tuples(rank)
        ok, nbytes = verify_by_replaying_raw(root, Pi)
        total_bytes += nbytes
        print(f"{rank:<6} {str(ok):<8} {nbytes}")
        if not ok:
            all_ok = False

    avg_bytes = total_bytes / len(values)
    print("\nAverage bytes hashed:", avg_bytes)
    print("All verified?", all_ok)
