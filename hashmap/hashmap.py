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

    def __contains__(self, key):
        if self._get_kv_node(key) is None:
            return False
        return True

    def __iter__(self):
        # do we need to implement some kind of view object for this?
        pass

    def _grow_hashmap(self):
        if self.scale_factor == 1:
            raise IndexError("Hashmap requires resizing and scale factor is 1, cannot resize")
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

    def _get_kv_node(self, key):
        key_hash = hash(key)
        modulo = key_hash % self.n_buckets
        bucket = self.buckets[modulo]
        return bucket.find_node_by_hash(key_hash)

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

    def get(self, key, default=None):
        kv_node = self._get_kv_node(key)
        if kv_node is None:
            return default
        else:
            return kv_node.value

    def pop(self, *args):
        if len(args) < 1:
            raise TypeError(f'pop expected at least 1 argument, got {len(args)}')
        elif len(args) > 2:
            raise TypeError(f'pop expected 2 arguments, got {len(args)}')
        key = args[0]
        default = args[1:]
        if key not in self and len(default) == 0:
            raise KeyError('Key not found and default not specified')
        k_hash = hash(key)
        b_index = k_hash % self.n_buckets
        bucket = self.buckets[b_index]
        value = bucket.del_node_by_hash(k_hash)
        if len(default) == 1:
            return default[0]
        return value

    def setdefault(self, key, default=None):
        if key in self:
            return self.get(key)
        self.put(key, default)
        return default


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
        if self.find_node_by_hash(k_hash) is None:
            return False
        return True

    def __iter__(self):
        for kv_node in self.kv_nodes:
            yield kv_node

    def find_node_by_hash(self, k_hash):
        for kv_node in self.kv_nodes:
            if kv_node.hash == k_hash:
                return kv_node

    def del_node_by_hash(self, k_hash):
        i = self._index_node_by_hash(k_hash)
        return self.kv_nodes.pop(i)

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
