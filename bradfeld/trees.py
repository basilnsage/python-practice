# from Bradfeld Practical Algorithms and Data Structures
# chapter on Trees
# imports go here


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = Node(value)
        else:
            sub_tree = self.left
            self.left = Node(value)
            self.left.left = sub_tree

    def insert_right(self, value):
        if self.right is None:
            self.right = Node(value)
        else:
            sub_tree = self.right
            self.right = Node(value)
            self.right.right = sub_tree


class ListTree:

    def __init__(self, value):
        # value, left child, right child
        self.tree_list = [
            value,
            [],
            []
        ]

    @staticmethod
    def insert_left(root, value):
        if len(root[1]) == 0:
            root[1] = [
                value,
                [],
                []
            ]
        else:
            sub_tree = root.pop(1)
            root.insert(1, [
                value,
                sub_tree,
                []
            ])

    @staticmethod
    def insert_right(root, value):
        if len(root[2]) == 0:
            root[2] = [
                value,
                [],
                []
            ]
        else:
            sub_tree = root.pop(2)
            root.insert(2, [
                value,
                [],
                sub_tree
            ])

    @staticmethod
    def get_value(root):
        return root[0]

    @staticmethod
    def set_value(root, value):
        root[0] = value
        return value

    @staticmethod
    def get_left(root):
        return root[1]

    @staticmethod
    def get_right(root):
        return root[2]
