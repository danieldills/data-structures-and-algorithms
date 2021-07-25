class Node:
    """
    Instantiate Node class
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    Create a Binary Tree class; Define a method for each of the depth first traversals: pre-order, in-order, post-order
    """

    def __init__(self):
        self.root = None

    def pre_order(self):
        # root >> left >> right
        collection = []

        def traverse(root):
            if root != None:
                collection.append(root.value)
                traverse(root.left)
                traverse(root.right)
        return collection

    def in_order():
        # left >> root >> right
        collection = []

        def traverse(root):
            if root != None:
                traverse(root.left)
                traverse(root.right)
                collection.append(root.value)
        return collection


    def post_order():
        # left >> right >> root
        pass




class BinarySearchTree(BinaryTree):
    """
    Create Binary Search Tree class; this is a sub-class of the Binary Tree Class, with additional methods: Add, Contains
    """

    def add():
        pass

    def contains():
        pass
