import ll
import unittest


class TestLinkedList(unittest.TestCase):

    def test_create_list(self):
        linked_list = ll.LinkedList()
        self.assertIsNone(linked_list.head)
        self.assertEqual(linked_list.length, 0)

    def test_append(self):
        linked_list = ll.LinkedList()
        linked_list.append(0)
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.len(), 1)
        linked_list.append(1)
        next_node = linked_list.head.next
        self.assertEqual(linked_list.head.value, 0)
        self.assertEqual(linked_list.len(), 2)
        self.assertEqual(next_node.value, 1)

    def test_insert(self):
        linked_list = ll.LinkedList()
        linked_list.append(0)
        linked_list.append(2)
        linked_list.insert(1, 1)
        self.assertEqual(linked_list.len(), 3)
        self.assertEqual(linked_list.head.next.value, 1)

    def test_remove(self):
        linked_list = ll.LinkedList()
        # [0, 1, 2, 1]
        linked_list.append(0)
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(1)
        linked_list.remove(2)
        self.assertEqual(linked_list.len(), 3)
        self.assertEqual(linked_list.to_list(), [0, 1, 1])
        linked_list.remove(1)
        self.assertEqual(linked_list.len(), 2)
        self.assertEqual(linked_list.to_list(), [0, 1])

    def test_pop(self):
        linked_list = ll.LinkedList()
        # [0, 3, 2, 1]
        linked_list.append(0)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        pop = linked_list.pop()
        self.assertEqual(pop, 1)
        self.assertEqual(linked_list.len(), 3)
        pop = linked_list.pop(1)
        self.assertEqual(pop, 3)
        self.assertEqual(linked_list.len(), 2)
        linked_list.pop()
        linked_list.pop()
        try:
            linked_list.pop()
        except Exception as e:
            self.assertEqual(str(e), "Cannot pop empty LinkedList")

    def test_index(self):
        linked_list = ll.LinkedList()
        # [0, 3, 2, 1]
        linked_list.append(0)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        i = linked_list.index(0)
        self.assertEqual(i, 0)
        i = linked_list.index(3, 0, 1)
        self.assertEqual(i, 1)
        i = linked_list.index(3, 1, 2)
        self.assertEqual(i, 1)

    def test_count(self):
        linked_list = ll.LinkedList()
        # [0, 3, 2, 1, 0]
        linked_list.append(0)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        linked_list.append(0)
        c = linked_list.count(0)
        self.assertEqual(c, 2)
        c = linked_list.count(3)
        self.assertEqual(c, 1)
        c = linked_list.count(None)
        self.assertEqual(c, 0)

    def test_reverse(self):
        linked_list = ll.LinkedList()
        # [0, 3, 2, 1]
        linked_list.append(0)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        before = linked_list.to_list()
        linked_list.reverse()
        after = linked_list.to_list()
        self.assertEqual([1, 2, 3, 0], after)
        linked_list.reverse()
        after_after = linked_list.to_list()
        self.assertEqual(before, after_after)

    def test_copy(self):
        linked_list = ll.LinkedList()
        # [0, 3, 2, 1]
        linked_list.append(0)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        before = linked_list.to_list()
        after_ll = linked_list.copy()
        after = after_ll.to_list()
        self.assertEqual(before, after)
        linked_list.append(0)
        before = linked_list.to_list()
        after = after_ll.to_list()
        self.assertEqual([0, 3, 2, 1, 0], before)
        self.assertEqual([0, 3, 2, 1], after)







if __name__ == '__main__':
    unittest.main()
