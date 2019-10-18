# defines List-like classes
# imports go here


class UnorderedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.head is None

    def add(self, value):
        new_node = ListNode(value)
        new_node.tail = self.head
        self.head = new_node
        self.length += 1

    def remove(self, value):
        current = self.head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.tail
                    self.length = 0
                else:
                    previous.tail = current.tail
                    self.length -= 1
            tail = current.tail
            previous = current
            current = tail

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.tail
        return False

    def size(self):
        return len(self)

    def append(self, value):
        self.insert(value, len(self))

    def index(self, value):
        index = 0
        current = self.head
        while current is not None:
            if current.value == value:
                return index
            current = current.tail
            index += 1
        return -1

    def insert(self, value, pos):
        current = self.head
        previous = None
        new_node = ListNode(value)
        index = 0
        if len(self) == 0 and pos != 0:
            raise IndexError("pos out of range")
        elif pos == 0:
            self.head = new_node
            new_node.tail = current
        else:
            while index < pos and current is not None:
                tail = current.tail
                previous = current
                current = tail
                index += 1
            previous.tail = new_node
            new_node.tail = current
        self.length += 1

    def pop(self, pos=None):
        if len(self) == 0:
            raise IndexError("cant pop empty list")
        if pos is None:
            pos = len(self) - 1
        elif pos >= len(self):
            raise IndexError("index out of range")
        if len(self) == 1 or pos == 0:
            result = self.head.value
            self.head = self.head.tail
            self.length -= 1
            return result
        index = 0
        current = self.head
        while index < pos - 1:
            current = current.tail
            index += 1
        result = current.tail.value
        current.tail = current.tail.tail
        self.length -= 1
        return result


class ListNode:
    def __init__(self, value):
        self.value = value
        self.tail = None
