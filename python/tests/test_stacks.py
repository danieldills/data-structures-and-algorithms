import pytest

from stacks.stacks import Stack

# Can successfully push onto a stack
def test_one():
    initial_stack = Stack()
    initial_stack.push("a")
    actual = initial_stack.top.value
    expected = "a"
    assert actual == expected

# Can successfully push multiple values onto a stack
def test_two():
    initial_stack = Stack()
    initial_stack.push("a")
    initial_stack.push("b")
    initial_stack.push("c")
    actual = initial_stack.top.value
    expected = "b"
    assert actual == expected

# Can successfully pop off the stack
def test_three():
    initial_stack = Stack()
    initial_stack.push("a")
    initial_stack.push("b")
    initial_stack.push("c")
    actual = initial_stack.pop()
    expected = "c"
    assert actual == expected
    assert initial_stack.top.value == "b"

# Can successfully empty a stack after multiple pops
def test_four():
    initial_stack = Stack()
    initial_stack.push("a")
    initial_stack.push("b")
    initial_stack.push("c")
    initial_stack.push("d")

    while initial_stack.peek():
        initial_stack.pop()
    assert initial_stack.top == None

# Can successfully peek the next item on the stack
def test_five():
    initial_stack = Stack()
    initial_stack.push("a")
    initial_stack.push("b")
    initial_stack.push("c")
    initial_stack.push("d")

    actual = initial_stack.peek()
    expected = "d"
    assert actual == expected

# Can successfully instantiate an empty stack
def test_six():
    initial_stack = Stack()
    actual = initial_stack.top
    expected = None
    assert initial_stack.top == None

# Calling pop on empty stack raises exception
def test_seven_pop():
    initial_stack = Stack()
    assert initial_stack.pop() == None

# Calling peek on empty stack raises exception
def test_seven_peek():
    initial_stack = Stack()
    assert initial_stack.pop() == None
