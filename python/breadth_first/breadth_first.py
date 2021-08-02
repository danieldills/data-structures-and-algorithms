from typing import Collection
from stacks_and_queue.queues import Queue

def breadth_first(tree):

    if tree.root is None:
        return []

    queueu = Queue()
    queueu.enqueue(tree.root)
    collection = []

    while not queueu.isEmpty():

        front = queueu.dequeue()

        if front.left:
            queueu.enqueue(front.left)

        if front.right:
            queueu.enqueue(front.right)

        collection.append(front.value)

    return collection
