from stacks_and_queue.queues.queue import Queues

def breadth_first(tree):

    if tree.root is None:
        return []

    queue = Queues()
    queue.enqueue(tree.root)
    collection = []

    while not queue.isEmpty():

        front = queue.dequeue()

        if front.left:
            queue.enqueue(front.left)

        if front.right:
            queue.enqueue(front.right)

        collection.append(front.value)

    return collection
