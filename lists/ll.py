# linked lists


class LinkedList:
    # should consist of a series of nodes
    # each node contains a value
    # each node contains a pointer to the next node

    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        list_form = self.to_list()
        return list_form.__str__()

    def append(self, value):
        self.insert(value, self.length)

    def insert(self, value, index):
        if index > self.length:
            raise Exception(f"Index out of range: {index}")
        curr = self.head
        new_node = LinkedListNode(value)
        if curr is None or index == 0:
            self.head = new_node
            new_node.link_next(curr)
        else:
            i = 1
            next_node = curr.next
            while i < index:
                curr = next_node
                next_node = next_node.next
                i += 1
            curr.link_next(new_node)
            new_node.link_next(next_node)
        self.length += 1

    def remove(self, value):
        if self.length == 0:
            raise IndexError("Cannot remove value from 0-length LinkedList")
        curr = self.head
        if curr.value == value:
            self.head = curr.next
            self.length -= 1
        else:
            next_node = curr.next
            while next_node is not None and next_node.value != value:
                curr = next_node
                next_node = curr.next
            if next_node is None or next_node.value != value:
                raise ValueError("Unable to find value in LinkedList")
            elif next_node.value == value:
                curr.link_next(next_node.next)
                self.length -= 1
            else:
                raise ValueError("Unable to find value in LinkedList")

    def pop(self, *args):
        if self.length == 0:
            raise Exception("Cannot pop empty LinkedList")
        num_args = len(args)
        if num_args > 1:
            raise Exception(f"{num_args} optional arguments found, 1 allowed")

        curr = self.head
        if num_args == 1:
            index = args[0]
            if not isinstance(index, int):
                raise ValueError("Optional argument must be an int")
            if index >= self.length:
                raise IndexError("Index out of range")
            if index == 0:
                value = self.head.value
                self.head = self.head.next
                self.length -= 1
            else:
                i = 1
                next_node = curr.next
                while i < index:
                    curr = next_node
                    next_node = next_node.next
                    i += 1
                value = next_node.value
                curr.link_next(next_node.next)
                self.length -= 1
        else:
            value = self.pop(self.length - 1)
        return value

    def len(self):
        return self.length

    def clear(self):
        del self.head
        self.length = 0

    def index(self, value, *args):
        start = 0
        end = self.length - 1

        if self.length == 0:
            raise Exception("Cannot index over empty LinkedList")
        if len(args) > 0 and isinstance(args[0], int):
            start = args[0]
        if len(args) > 1 and isinstance(args[1], int):
            end = args[1]

        curr = self.head
        i = 0
        while i < start and curr is not None:
            curr = curr.next
            i += 1
        while i < min(end, self.length - 1) and curr is not None:
            if curr.value == value:
                return i
            curr = curr.next
            i += 1
        if curr is None or curr.value != value:
            raise ValueError(f"{value} not found in LinkedList")
        return i

    def count(self, value):
        count = 0
        curr = self.head
        while curr is not None:
            if curr.value == value:
                count += 1
            curr = curr.next
        return count

    def reverse(self):
        if self.length == 0:
            return
        old = None
        curr = self.head
        next_node = curr.next
        while True:
            curr.link_next(old)
            if next_node is None:
                break
            old = curr
            curr = next_node
            next_node = next_node.next
        self.head = curr

    def copy(self):
        new_linkedlist = LinkedList()
        curr = self.head
        while curr is not None:
            new_linkedlist.append(curr.value)
            curr = curr.next
        return new_linkedlist

    def to_list(self):
        empty_list = []
        curr = self.head
        while curr is not None:
            empty_list.append(curr.value)
            curr = curr.next
        return empty_list


class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None

    def update_value(self, value):
        self.value = value

    def link_next(self, node):
        self.next = node
