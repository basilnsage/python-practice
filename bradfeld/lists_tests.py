import unittest
from bradfeld.lists import UnorderedList


class ListTest(unittest.TestCase):
    def setUp(self):
        self.uo_list = UnorderedList()
        self.assertIsNone(self.uo_list.head)
        for i in range(4):
            self.uo_list.add(i)

    def test_add(self):
        head = self.uo_list.head
        self.assertEqual(len(self.uo_list), 4)
        self.assertEqual(head.value, 3)
        head = head.tail
        self.assertEqual(head.value, 2)
        head = head.tail.tail
        self.assertEqual(head.value, 0)
        self.assertIsNone(head.tail)

    def test_remove(self):
        # 3 -> 2 -> 0 -> None
        self.uo_list.remove(1)
        self.assertEqual(len(self.uo_list), 3)
        head = self.uo_list.head
        self.assertEqual(head.value, 3)
        head = head.tail.tail
        self.assertEqual(head.value, 0)
        self.assertIsNone(head.tail)
        # 2 -> 0 -> None
        self.uo_list.remove(3)
        head = self.uo_list.head
        self.assertEqual(head.value, 2)
        # None
        self.uo_list.remove(2)
        self.uo_list.remove(0)
        self.assertIsNone(self.uo_list.head)

    def test_search(self):
        # 3 -> 2 -> 1 -> 0 -> None
        self.assertTrue(self.uo_list.search(3))
        self.assertTrue(self.uo_list.search(0))
        self.assertFalse(self.uo_list.search(None))

    def test_append(self):
        # 3 -> 2 -> 1 -> 0 -> 4 -> None
        self.uo_list.append(4)
        self.assertEqual(len(self.uo_list), 5)
        self.assertTrue(self.uo_list.search(4))
        head = self.uo_list.head.tail.tail.tail.tail
        self.assertEqual(head.value, 4)
        self.assertIsNone(head.tail)

    def test_insert(self):
        # 3 -> 4 -> 2 -> 1 -> 0 -> None
        self.uo_list.insert(4, 1)
        self.assertEqual(len(self.uo_list), 5)
        self.assertTrue(self.uo_list.search(4))
        head = self.uo_list.head.tail
        self.assertEqual(head.value, 4)
        self.assertTrue(head.tail.value, 2)
        # 5 -> 3 -> 4 -> 2 -> 1 -> 0 -> None
        self.uo_list.insert(5, 0)
        head = self.uo_list.head
        self.assertEqual(head.value, 5)
        self.assertEqual(head.tail.value, 3)

    def test_index(self):
        self.assertEqual(self.uo_list.index(3), 0)
        self.assertEqual(self.uo_list.index(0), 3)
        self.assertEqual(self.uo_list.index(5), -1)
        self.uo_list.append(3)
        self.assertEqual(self.uo_list.index(3), 0)

    def test_pop(self):
        # 3 -> 2 -> 1 -> 0 -> None
        self.assertEqual(self.uo_list.pop(), 0)
        self.assertEqual(len(self.uo_list), 3)
        self.assertEqual(self.uo_list.pop(), 1)
        self.assertEqual(len(self.uo_list), 2)
        self.assertEqual(self.uo_list.pop(), 2)
        self.assertEqual(len(self.uo_list), 1)
        self.assertEqual(self.uo_list.pop(), 3)
        self.assertEqual(len(self.uo_list), 0)

    def test_pop_pos(self):
        # 2 -> 1 -> 0 -> None
        self.assertEqual(self.uo_list.pop(0), 3)
        self.assertEqual(len(self.uo_list), 3)
        # 2 -> 0 -> None
        self.assertEqual(self.uo_list.pop(1), 1)
        self.assertEqual(len(self.uo_list), 2)
        head = self.uo_list.head
        self.assertEqual(head.value, 2)
        self.assertEqual(head.tail.value, 0)


if __name__ == '__main__':
    unittest.main()
