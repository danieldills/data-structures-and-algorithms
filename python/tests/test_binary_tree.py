import pytest

from binary_tree.binary_tree import Node, BinaryTree, BinarySearchTree

# @pytest.mark.skip("pending")
def test_node_has_value():
    node = Node("apple")
    assert node.value == "apple"


# @pytest.mark.skip("pending")
def test_node_has_left_of_none():
    node = Node("apple")
    assert node.left is None


# @pytest.mark.skip("pending")
def test_node_has_right_of_none():
    node = Node("apple")
    assert node.right is None


# @pytest.mark.skip("pending")
def test_create_binary_tree():
    tree = BinaryTree()
    assert tree


# @pytest.mark.skip("pending")
def test_binary_tree_has_root():
    tree = BinaryTree()
    assert tree.root is None


# @pytest.mark.skip("pending")
def test_create_binary_search_tree():
    tree = BinarySearchTree()
    assert tree

# @pytest.mark.skip("pending")
def test_add_method_will_add_to_tree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(15)
    tree.add(5)
    assert tree.root.value == 10
    assert tree.root.right.value == 15
    assert tree.root.left.value == 5

# @pytest.mark.skip("pending")
def test_pre_order_will_return_correct_values(new_tree):
    actual = new_tree.pre_order()
    expected = [20, 15, 12, 17, 25, 23, 28]
    actual == expected

# @pytest.mark.skip("pending")
def test_pre_in_order_will_return_correct_values(new_tree):
    actual = new_tree.in_order()
    expected = [12, 15, 17, 20, 23, 25, 28]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_max_value_tree(new_tree):
    actual = new_tree.max_value()
    expected = 28
    assert actual == expected

# @pytest.mark.skip("pending")
def test_max_value_tree_fail(new_tree):
    actual = new_tree.max_value()
    expected = 15
    assert actual != expected

# @pytest.mark.skip("pending")
def test_post_order_will_return_correct_values(new_tree):
    actual = new_tree.post_order()
    expected = [12, 17, 15, 23, 28, 25, 20]
    assert actual == expected

# @pytest.mark.skip("pending")
def test_contains_method_will_return_true_for_present_value(new_tree):
    actual = new_tree.contains(23)
    assert actual == True

# @pytest.mark.skip("pending")
def test_contains_method_will_return_false_for_present_value(new_tree):
    actual = new_tree.contains(40)
    assert actual == False

## Fixtures ##

@pytest.fixture
def new_tree():
    new_tree = BinarySearchTree()
    new_tree.add(20)
    new_tree.add(15)
    new_tree.add(25)
    new_tree.add(12)
    new_tree.add(17)
    new_tree.add(23)
    new_tree.add(28)
    return new_tree
