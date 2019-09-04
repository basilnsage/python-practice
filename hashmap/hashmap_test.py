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



if __name__ == '__main__':
    unittest.main()
