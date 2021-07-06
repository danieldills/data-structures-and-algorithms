import pytest

from queues.queue import Queues

# Can successfully enqueue into a queue
def test_eight():
    new_queue = Queues()
    new_queue.enqueue("a")
    assert new_queue.front.value == "a"

# Can successfully enqueue multiple values into a queue
def test_nine():
    new_queue = Queues()
    new_queue.enqueue("a")
    new_queue.enqueue("b")
    new_queue.enqueue("c")
    new_queue.enqueue("d")
    assert new_queue.front.value == "a"
    assert new_queue.front.rear == "d"

# Can successfully dequeue out of a queue the expected value
def test_ten():
    pass

# Can successfully peek into a queue, seeing the expected value
def test_eleven():
    pass

# Can successfully empty a queue after multiple dequeues
def test_twelve():
    new_queue = Queues()
    new_queue.enqueue("a")
    new_queue.enqueue("b")
    new_queue.enqueue("c")
    new_queue.enqueue("d")

    while new_queue.peek():
        new_queue.dequeue()

    assert new_queue.front == None


# Can successfully instantiate an empty queue
def test_thirteen():
    new_queue = Queues()
    assert new_queue.front == None
    assert new_queue.rear == None

# Calling dequeue or peek on empty queue raises exception
def test_fourteen():
    pass
