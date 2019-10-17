class ItemsView:
    def __init__(self):
        self.nodes = []
        self.keys = KeysView(self.nodes)
        self.values = ValuesView(self.nodes)

    def __len__(self):
        return len(self.nodes)

    def __contains__(self, item):
        if len(item) != 2:
            raise ValueError('Item does not appear to be a key-value pair')
        for node in self.nodes:
            if node.key == item[0] and node.value == item[1]:
                return True
        return False

    def __iter__(self):
        for node in self.nodes:
            yield (node.key, node.value)

    def __repr__(self):
        return 'ItemsView(' + [(node.key, node.value) for node in self.nodes].__repr__() + ')'

    def __eq__(self, other):
        if type(other) == ItemsView:
            return other.nodes == self.nodes
        return False

    def get_keys_view(self):
        return self.keys

    def get_values_view(self):
        return self.values

    def add_node(self, node):
        self.nodes.append(node)

    def remove_node(self, node):
        self.nodes.remove(node)

    def pop(self):
        node = self.nodes.pop()
        return (node.key, node.value)

    def reset(self):
        self.nodes = []


class KeysView:
    def __init__(self, nodes):
        self.nodes = nodes

    def __len__(self):
        return len(self.nodes)

    def __contains__(self, key):
        for node in self.nodes:
            if key == node.key:
                return True
        return False

    def __iter__(self):
        for node in self.nodes:
            yield node.key

    def __repr__(self):
        return 'KeysView(' + [node.key for node in self.nodes].__repr__() + ')'

    def __eq__(self, other):
        if type(other) == KeysView:
            if len(other) != len(self):
                return False
            for i in range(0, len(self)):
                if other.nodes[i].key != self.nodes[i].key:
                    return False
            return True
        return False


class ValuesView:
    def __init__(self, nodes):
        self.nodes = nodes

    def __len__(self):
        return len(self.nodes)

    def __contains__(self, key):
        for node in self.nodes:
            if key == node.key:
                return True
        return False

    def __iter__(self):
        for node in self.nodes:
            yield node.value

    def __repr__(self):
        return 'ValuesView(' + [node.value for node in self.nodes].__repr__() + ')'

    def __eq__(self, *args):
        return False


class KVNode:

    def __init__(self, key, value):
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __eq__(self, other):
        if isinstance(other, KVNode):
            return other.hash == self.hash and other.key == self.key and other.value == self.value
        return False


class Bucket:

    def __init__(self):
        self.kv_nodes = []

    def __contains__(self, item: KVNode):
        k_hash = item.hash
        if self.find_node_by_hash(k_hash) is None:
            return False
        return True

    def __iter__(self):
        for kv_node in self.kv_nodes:
            yield kv_node

    def __len__(self):
        return len(self.kv_nodes)

    def find_node_by_hash(self, k_hash):
        for kv_node in self.kv_nodes:
            if kv_node.hash == k_hash:
                return kv_node

    def del_node_by_hash(self, k_hash):
        i = self._index_node_by_hash(k_hash)
        if i is None:
            return None
        return self.kv_nodes.pop(i)

    def _index_node_by_hash(self, k_hash):
        for i in range(0, len(self)):
            if self.kv_nodes[i].hash == k_hash:
                return i
            i += 1

    def append_kv_node(self, kv_node):
        self.kv_nodes.append(kv_node)

    def update_kv_node(self, kv_node):
        kv_node_index = self._index_node_by_hash(kv_node.hash)
        self.kv_nodes[kv_node_index] = kv_node
