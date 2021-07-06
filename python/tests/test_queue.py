import pytest

from stacks_and_queue.queues.queue import Queues

# Can successfully enqueue into a queue
def test_eight():
    new_queue = Queues()
    new_queue.enqueue("a")
    assert new_queue.front.value == "a"
    assert new_queue.rear.value == "a"

# Can successfully enqueue multiple values into a queue
def test_nine(new_queue):
    assert new_queue.front.value == "a"
    assert new_queue.front.next.value == "b"
    assert new_queue.rear.value == "d"

# Can successfully dequeue out of a queue the expected value
def test_ten(new_queue):
    actual = new_queue.dequeue()
    expected = "a"
    assert actual == expected
    assert new_queue.front.value == "b"

# Can successfully peek into a queue, seeing the expected value
def test_eleven():
    pass

# Can successfully empty a queue after multiple dequeues
def test_twelve(new_queue):
    while not new_queue.isEmpty():
        new_queue.dequeue()
    assert new_queue.front == None

# Can successfully instantiate an empty queue
def test_thirteen():
    new_queue = Queues()
    assert new_queue.front == None
    assert new_queue.rear == None

# Calling dequeue or peek on empty queue raises exception
def test_fourteen():
    new_queue = Queues()
    with pytest.raises(Exception):
        new_queue.dequeue()

# ***Fixture***
@pytest.fixture
def new_queue():
    new_queue = Queues()
    new_queue.enqueue("a")
    new_queue.enqueue("b")
    new_queue.enqueue("c")
    new_queue.enqueue("d")
    return new_queue
