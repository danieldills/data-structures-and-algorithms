import pytest

from stacks_and_queue.stacks.stacks import Stack

# Can successfully push onto a stack
def test_one():
    initial_stack = Stack()
    initial_stack.push("a")
    actual = initial_stack.top.value
    expected = "a"
    assert actual == expected

# Can successfully push multiple values onto a stack
def test_two(initial_stack):
    actual = initial_stack.top.value
    expected = "d"
    assert actual == expected

# Can successfully pop off the stack
def test_three(initial_stack):
    actual = initial_stack.pop()
    expected = "d"
    assert actual == expected

# Can successfully empty a stack after multiple pops
def test_four(initial_stack):
    while not initial_stack.isEmpty():
        initial_stack.pop()
    assert initial_stack.top == None

# Can successfully peek the next item on the stack
def test_five(initial_stack):
    actual = initial_stack.peek()
    expected = "d"
    assert actual == expected

# Can successfully instantiate an empty stack
def test_six():
    initial_stack = Stack()
    actual = initial_stack.top
    expected = None
    assert actual == expected

# Calling pop on empty stack raises exception
def test_seven_pop():
    initial_stack = Stack()
    with pytest.raises(Exception):
        initial_stack.pop()

# Calling peek on empty stack raises exception
def test_seven_peek():
    initial_stack = Stack()
    with pytest.raises(Exception):
        initial_stack.peek()

@pytest.fixture
def initial_stack():
    initial_stack = Stack()
    initial_stack.push("a")
    initial_stack.push("b")
    initial_stack.push("c")
    initial_stack.push("d")
    return initial_stack
