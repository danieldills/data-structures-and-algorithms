class Node:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):

        node = Node(value)
        node.next = self.head
        self.head = node
        return self

    def includes(self, value):

        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):

        string = ""

        current = self.head

        while current is not None:
            string += f"{ {current.value} } ->"
            current = current.next

        string += f" None "

        return string

# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
    def kthFromEnd(self, n):
        temp = self.head # used temp variable

        length = 0
        while temp is not None:
            temp = temp.next
            length += 1

        # print count
        if n > length: # if entered location is greater
                       # than length of linked list
            print('Location is greater than the' +
                         ' length of LinkedList')
            return
        temp = self.head
        for i in range(0, length - n):
            temp = temp.next
        print(temp.data)


if __name__ == "__main__":

    ll1 = LinkedList()
    ll1.insert("a").insert("b").insert("c").insert("d")

    result = str(ll1)
    print(result)
