# imports go here
import unittest

from hashmap import Hashmap


class HashMapTests(unittest.TestCase):

    def setUp(self):
        self.hashmap = Hashmap(n_buckets=1)

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


if __name__ == '__main__':
    unittest.main()
