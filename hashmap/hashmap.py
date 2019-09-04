# hashmaps without LIFO order
# imports go here


class Hashmap:

    def __init__(self, scale=2, n_buckets=8):
        self.scale_factor = scale
        self.n_buckets = n_buckets
        self.buckets = []
        for i in range(0, self.n_buckets):
            self.buckets.append(Bucket())
        self.length = 0

    def __len__(self):
        return self.length

    def _grow_hashmap(self):
        self.n_buckets *= self.scale_factor
        old_buckets = self.buckets
        new_buckets = []
        for i in range(0, self.n_buckets):
            new_buckets.append(Bucket())
        self.buckets = new_buckets
        self.length = 0
        for bucket in old_buckets:
            for kv_node in bucket:
                self.put(kv_node.key, kv_node.value)

    def put(self, key, value):
        kv_node = KVNode(key, value)
        b_index = kv_node.hash % self.n_buckets
        bucket = self.buckets[b_index]
        contains = kv_node in bucket
        if not contains:
            if len(self) == self.n_buckets:
                self._grow_hashmap()
                b_index = kv_node.hash % self.n_buckets
                bucket = self.buckets[b_index]
            bucket.append_kv_node(kv_node)
            self.length += 1
        else:
            bucket.update_kv_node(kv_node)

    def get(self):
        pass

    def len(self):
        pass

    def contains(self):
        pass


class KVNode:

    def __init__(self, key, value):
        self.hash = hash(key)
        self.key = key
        self.value = value


class Bucket:

    def __init__(self):
        self.kv_nodes = []
        self.length = 0

    def __contains__(self, item: KVNode):
        k_hash = item.hash
        if self._find_node_by_hash(k_hash) is None:
            return False
        return True

    def __iter__(self):
        for kv_node in self.kv_nodes:
            yield kv_node

    def _find_node_by_hash(self, k_hash):
        for kv_node in self.kv_nodes:
            if kv_node.hash == k_hash:
                return kv_node

    def _index_node_by_hash(self, k_hash):
        for i in range(0, self.length):
            if self.kv_nodes[i].hash == k_hash:
                return i
            i += 1

    def append_kv_node(self, kv_node):
        self.kv_nodes.append(kv_node)
        self.length += 1

    def update_kv_node(self, kv_node):
        kv_node_index = self._index_node_by_hash(kv_node.hash)
        self.kv_nodes[kv_node_index] = kv_node
