class Node:
    """
    An object for storing a single node of a linked list.
    models two atributes - data and the link to the next node in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data>: {self.data}"


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

    def search(self, key):
        """
        searches for the first node containing data that matches the key
        returns the node or 'None' if not found
        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return f"value : {key} is not found"

    def search_by_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def insert(self, data, index):
        """
        inserts a new node containing data at index position
        insertion takes O(1) constant  time
        but finding the insertion position takes O(n) linear time

        takes overall O(n) time
        """

        if index == 0:
            self.add(data)
        if index > 0:

            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                if current is not None:
                    current = current.next_node
                    position -= 1
                else:
                    break

            if current is not None:
                prev_node = current
                next_node = current.next_node
                prev_node.next_node = new
                new.next_node = next_node

            else:
                return "index is out of range"

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        if current is not None:
            return current
        return f"value : {key} is not found"

    def remove_at_index(self, index):
        """
        removes at an index.
        takes for to remove O(1) constant time
        takes for search O(n) time
        overall takes O(n) time
        """
        current = self.head
        previous = None

        if index == 0:
            deleted_head = self.head
            self.head = current.next_node
            return deleted_head

        if index > 0 and index < self.size():

            position = index

            while position > 0:
                previous = current
                current = current.next_node
                position -= 1

            deleted = current
            current = previous
            current.next_node = deleted.next_node

            if deleted:
                return deleted
        return "index out of range"

    def __repr__(self):
        """
        Returns a string representation of the list
        takes O(n) time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head:{current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail:{current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node

        return "->".join(nodes)
