class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class Queues:
    def __init__(self, node = None):
        self.front = node
        self.rear = node

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
            return self

        self.rear.next = node
        self.rear = node
        return self

    def dequeue(self):

        if self.front is None:
            # reaise an exception
            return None

        dequed = self.front
        self.front = self.front.next
        return dequed

    def peek(self):
        if self.front is None:
            return None

        return self.front.value

    def isEmpty(self):
        return self.front == None


    if __name__ == "__main__":
        pass
