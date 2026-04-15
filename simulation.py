import random, time
from chord import ChordRing, sha1_id

class ChordSimulator:
    def __init__(self, m, n):
        self.m = m
        self.ring = ChordRing(m)

        max_nodes = min(n, 2**m)  # ✅ FIX

        for i in random.sample(range(2**m), max_nodes):
            self.ring.add_node(i)

    def lookup(self, key):
        key_id = sha1_id(key, self.m)
        node = next(iter(self.ring.nodes.values()))
        hops = 0
        visited = set()

        while True:
            hops += 1
            if node.id in visited:
                return node, hops
            visited.add(node.id)

            if node.in_interval(key_id, node.id, node.successor.id, True):
                return node.successor, hops

            nxt = node.closest_preceding_node(key_id)
            if nxt == node:
                return node.successor, hops
            node = nxt

    def run_lookups(self, n=30):
        res = []
        for _ in range(n):
            k = str(random.randint(1, 10000))
            t = time.time()
            node, h = self.lookup(k)
            res.append({"hops": h, "latency": time.time() - t})
        return res


# ✅ FIXED SCALABILITY
def scalability_experiment(m):
    res = []

    max_limit = 2**m  # ✅ LIMIT

    for n in [4, 8, 16, 32, 64, 128]:
        n = min(n, max_limit)  # ✅ FIX

        sim = ChordSimulator(m, n)
        data = sim.run_lookups(30)

        avg = sum(x["hops"] for x in data) / len(data)
        res.append({"nodes": n, "avg_hops": avg})

    return res