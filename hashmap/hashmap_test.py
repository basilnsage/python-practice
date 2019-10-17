# imports go here
import unittest

from hashmap import *


class HashMapTests(unittest.TestCase):

    def setUp(self):
        self.hashmap = Hashmap(n_buckets=1)
        self.lifoMap = LIFOHashMap(n_buckets=1)

    def test_put(self):
        self.hashmap.put(1, 0)
        self.hashmap.put(3, 0)
        self.assertEqual(len(self.hashmap), 2)

    def test_get(self):
        self.hashmap.put('a', 1)
        self.hashmap.put('c', 3)
        get_one = self.hashmap.get('a')
        get_none = self.hashmap.get('b')
        get_three = self.hashmap.get('c')
        get_two = self.hashmap.get('b', 2)
        self.assertEqual(get_one, 1)
        self.assertEqual(get_none, None)
        self.assertEqual(get_three, 3)
        self.assertEqual(get_two, 2)

        self.hashmap.put('a', 'a')
        get_a = self.hashmap.get('a')
        self.assertEqual(get_a, 'a')

    def test_contains(self):
        self.hashmap.put('a', 1)
        self.assertTrue('a' in self.hashmap)
        self.hashmap.put('b', None)
        self.assertTrue('b' in self.hashmap)
        self.assertFalse(None in self.hashmap)
        self.assertFalse('c' in self.hashmap)

    def test_pop(self):
        self.hashmap.put('a', 1)
        self.hashmap.put('b', 2)
        self.assertEqual(len(self.hashmap), 2)
        self.assertEqual(1, self.hashmap.pop('a'))
        self.assertEqual(len(self.hashmap), 1)
        self.assertEqual('dne', self.hashmap.pop('a', 'dne'))
        self.assertEqual(len(self.hashmap), 1)
        self.assertEqual(2, self.hashmap.pop('b', 'wrong'))
        self.assertEqual(len(self.hashmap), 0)
        self.assertEqual('wrong', self.hashmap.pop('b', 'wrong'))

    def test_items_views(self):
        nodes = [
            KVNode('a', 1),
            KVNode('b', 2),
            KVNode('c', 3)
         ]
        items_view_a = ItemsView()
        items_view_b = ItemsView()
        for node in nodes:
            items_view_a.add_node(node)
            items_view_b.add_node(node)
        self.assertEqual(items_view_a, items_view_b)
        self.assertEqual(len(items_view_a), 3)
        items_a = [item for item in items_view_a]
        self.assertEqual(items_a, [('a', 1), ('b', 2), ('c', 3)])

    def test_keys_views(self):
        nodes = [
            KVNode('a', 1),
            KVNode('b', 2),
            KVNode('c', 3)
        ]
        items_view_a = ItemsView()
        items_view_b = ItemsView()
        for node in nodes:
            items_view_a.add_node(node)
            items_view_b.add_node(node)
        keys_view_a = items_view_a.get_keys_view()
        keys_view_b = items_view_b.get_keys_view()
        keys_a = [key for key in keys_view_a]
        self.assertEqual(keys_view_a, keys_view_b)
        self.assertEqual(keys_a, ['a', 'b', 'c'])
        items_view_a.add_node(KVNode('d', 4))
        self.assertNotEqual(keys_view_a, keys_view_b)
        keys_a = [key for key in keys_view_a]
        self.assertEqual(keys_a, ['a', 'b', 'c', 'd'])

    def test_values_view(self):
        nodes = [
            KVNode('a', 1),
            KVNode('b', 2),
            KVNode('c', 3)
        ]
        items_view_a = ItemsView()
        items_view_b = ItemsView()
        for node in nodes:
            items_view_a.add_node(node)
            items_view_b.add_node(node)
        values_view_a = items_view_a.get_values_view()
        values_view_b = items_view_b.get_values_view()
        values_a = [value for value in values_view_a]
        values_b = [value for value in values_view_b]
        self.assertEqual(values_a, values_b)
        self.assertEqual(values_a, [1, 2, 3])
        items_view_a.add_node(KVNode('d', 4))
        values_a = [value for value in values_view_a]
        self.assertEqual(values_a, [1, 2, 3, 4])
        items_view_a.remove_node(KVNode('b', 2))
        values_a = [value for value in values_view_a]
        self.assertEqual(values_a, [1, 3, 4])

    def test_lifo_growth(self):
        lm = LIFOHashMap(n_buckets=1)
        lm.put('a', 1)
        self.assertEqual(len(lm), 1)
        lm.put('b', 2)
        items = [item for item in lm.items()]
        self.assertEqual(len(lm), 2)
        self.assertEqual(items, [('a', 1), ('b', 2)])
        lm.put('c', 3)
        self.assertEqual(len(lm), 3)
        self.assertEqual(lm.n_buckets, 4)
        lm.put('d', 4)
        self.assertEqual(len(lm), 4)
        self.assertEqual(lm.n_buckets, 4)
        lm.put('e', 5)
        self.assertEqual(len(lm), 5)
        self.assertEqual(lm.n_buckets, 8)

    def test_lifo_put(self):
        self.lifoMap.put('a', 1)
        keys = self.lifoMap.keys()
        keys_list = [key for key in keys]
        values = self.lifoMap.values()
        values_list = [value for value in values]
        items = self.lifoMap.items()
        items_list = [item for item in items]
        self.assertEqual(keys_list, ['a'])
        self.assertEqual(values_list, [1])
        self.assertEqual(items_list, [('a', 1)])
        self.lifoMap.put('b', 2)
        self.lifoMap.put('c', 3)
        keys_list = [key for key in keys]
        values_list = [value for value in values]
        items_list = [item for item in items]
        self.assertEqual(keys_list, ['a', 'b', 'c'])
        self.assertEqual(values_list, [1, 2, 3])
        self.assertEqual(items_list, [('a', 1), ('b', 2), ('c', 3)])

    def test_lifo_get(self):
        self.lifoMap.put('a', 1)
        self.lifoMap.put('c', 3)
        get_one = self.lifoMap.get('a')
        get_none = self.lifoMap.get('b')
        get_three = self.lifoMap.get('c')
        get_two = self.lifoMap.get('b', 2)
        self.assertEqual(get_one, 1)
        self.assertEqual(get_none, None)
        self.assertEqual(get_three, 3)
        self.assertEqual(get_two, 2)

    def test_lifo_pop(self):
        self.lifoMap.put('a', 1)
        self.lifoMap.put('b', 2)
        self.lifoMap.put('c', 3)
        items = self.lifoMap.items()
        pop_b = self.lifoMap.pop('b')
        items_list = [(k, v) for k, v in items]
        self.assertEqual(pop_b, 2)
        self.assertEqual(len(self.lifoMap), 2)
        self.assertEqual(items_list, [('a', 1), ('c', 3)])
        pop_c = self.lifoMap.pop('c', 4)
        items_list = [(k, v) for k, v in items]
        self.assertEqual(pop_c, 3)
        self.assertEqual(len(self.lifoMap), 1)
        self.assertEqual(items_list, [('a', 1)])
        pop_d = self.lifoMap.pop('d', 4)
        self.assertEqual(pop_d, 4)
        self.assertEqual(len(self.lifoMap), 1)
        self.assertEqual(items_list, [('a', 1)])
        pop_a = self.lifoMap.pop('a')
        items_list = [(k, v) for k, v in items]
        self.assertEqual(pop_a, 1)
        self.assertEqual(len(self.lifoMap), 0)
        self.assertEqual(items_list, [])

    def test_popitem(self):
        self.lifoMap.put('a', 1)
        self.lifoMap.put('b', 2)
        self.lifoMap.put('c', 3)
        popped = []
        for _ in range(len(self.lifoMap)):
            popped.append(self.lifoMap.popitem())
        self.assertEqual(popped, [('c', 3), ('b', 2), ('a', 1)])


if __name__ == '__main__':
    unittest.main()
