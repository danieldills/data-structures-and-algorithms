from code_challenges.linked_list.linked_list import LinkedList, Node

# Can successfully create a node
def test_a():
    node1 = Node("apple")
    actual = node1.value
    expected = "apple"
    assert actual == expected
    assert node1.next == None

# Can successfully instantiate an empty linked list
def test_one():
    linked_list1 = LinkedList()
    actual = linked_list1.head
    expected = None
    assert actual == expected

# Can properly insert into the linked list
def test_two():
    ll2 = LinkedList()
    ll2.insert("a")
    ll2.insert("b")
    actual = ll2.head.value
    expected = "b"
    assert actual == expected

# The head property will properly point to the first node in the linked list
def test_three():
    node1 = Node("a")
    ll1 = LinkedList(node1)
    actual = ll1.head.value
    expected = "a"
    assert actual == expected

# Can properly insert multiple nodes into the linked list
def test_four():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c")
    actual = ll1.head.value
    expected = "c"
    assert actual == expected

# Will return true when finding a value within the linked list that exists
def test_five():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = ll1.includes("c")
    expected = True
    assert actual == expected

# Will return false when searching for a value in the linked list that does not exist
def test_six():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = ll1.includes("h")
    expected = False
    assert actual == expected

# Can properly return a collection of all the values that exist in the linked list
def test_seven():
    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")
    actual = str(ll1)
    expected = "{'d'} ->{'c'} ->{'b'} ->{'a'} -> None "
    assert actual == expected

# Where k is greater than the length of the linked list
def test_eight():
    ll1 = LinkedList()

# Where k and the length of the list are the same

# Where k is not a positive integer

# Where the linked list is of a size 1

# “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
