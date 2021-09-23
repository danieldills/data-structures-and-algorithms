from stacks_and_queue.queues.queue import Node, Queue


def graph_breadth_first(vertex):
    nodes = {}
    breadth = Queue()
    visited = set()

    breadth.enqueue(vertex)
    visited.add(vertex)

    while not breadth.isEmpty():
        front = breadth.dequeue()
        nodes.append(front)
        children =

        for child in front.children:
            if child not in visited:
                visited.append(child)
                breadth.enqueue(child)
    return visited
