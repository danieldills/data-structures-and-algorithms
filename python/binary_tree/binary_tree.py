class Node:
    """
    Instantiate Node class
    """
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    """
    Create a Binary Tree class; Define a method for each of the depth first traversals: pre-order, in-order, post-order
    """

    def __init__(self, node=None, max_num=0):
        self.root = node
        self.max_num = max_num

    def pre_order(self):
        # root >> left >> right
        collection = []

        def traverse(root):
            if root != None:
                collection.append(root.value)
                traverse(root.left)
                traverse(root.right)
        return collection

    def in_order(self):
        # left >> root >> right
        collection = []

        def traverse(root):
            if root != None:
                traverse(root.left)
                collection.append(root.value)
                traverse(root.right)
        traverse(self.root)
        return collection

    # def max_value(self):
    #     # left >> root >> right
    #     collection = []

    #     def traverse(root):
    #         if root != None:
    #             traverse(root.left)
    #             collection.append(root.value)
    #             traverse(root.right)
    #     traverse(self.root)
    #     return max(collection)

    def max_value(self, max_num=0):
        # left >> root >> right

        def traverse(root):
            if root != None:
                traverse(root.left)
                if self.max_num < root.value:
                    self.max_num = root.value
                traverse(root.right)
        traverse(self.root)
        return self.max_num

    def post_order(self):
        # left >> right >> root
        collection = []

        def traverse(root):
            if root != None:
                traverse(root.left)
                traverse(root.right)
                collection.append(root.value)
        traverse(self.root)
        return collection


class BinarySearchTree(BinaryTree):
    """
    Create Binary Search Tree class; this is a sub-class of the Binary Tree Class, with additional methods: Add, Contains
    """

    def add(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return self

        current = self.root

        while(current):

            if value == current.value:
                raise Exception("Value already exists")

            if value > current.value:
                if current.right is None:
                    current.right = node
                    return self
                current = current.right

            else:
                if current.left is None:
                    current.left = node
                    return self
                current = current.left

    def contains(self, target):
        if self.root is None:
            return None

        current = self.root

        while current:

            if current.value == target:
                return True

            if target > current.value:
                current = current.right
            else:
                current = current.left

        return False
