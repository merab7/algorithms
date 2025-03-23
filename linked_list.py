class Node:
    """
    An object for storing a single node of a linked list.
    models two atributes - data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, deta):
        self.data = deta

    def __repr__(self):
        return f"<Node data: {self.data}"


class LinkedList:
    """
    singly linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        returns the number of node in the list
        Takes linear tiem
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        adds new node containing data at head of the list
        takes 0(1)
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
