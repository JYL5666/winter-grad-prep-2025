class HashTable:
    def __init__(self, capacity=8):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self._cap = capacity
        self._buckets = [[] for _ in range(capacity)]

    def _index(self, key):
        return hash(key) % self._cap

    def put(self, key, value):
        idx = self._index(key)
        bucket = self._buckets[idx]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        idx = self._index(key)
        bucket = self._buckets[idx]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(key)

    def update(self, key, value):
        self.put(key, value)


def _test():
    ht = HashTable(capacity=4)

    ht.put("a", 1)
    assert ht.get("a") == 1

    ht.put("a", 2)
    assert ht.get("a") == 2

    try:
        ht.get("missing")
        assert False, "should raise KeyError"
    except KeyError:
        pass


if __name__ == "__main__":
    _test()
    print("All tests passed.")
