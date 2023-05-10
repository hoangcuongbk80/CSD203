class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, key):
        if self.is_empty():
            return None
        elif self.head.data == key:
            temp = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            else:
                self.head.prev = None
            temp.next = None
            return temp.data
        elif self.tail.data == key:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            return temp.data
        else:
            current = self.head
            while current is not None:
                if current.data == key:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    current.next = None
                    current.prev = None
                    return current.data
                current = current.next
            return None

    def display(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=' ')
                current = current.next
            print()

# create a new doubly linked list
dll = DoublyLinkedList()

# add some nodes to the list
dll.add_first(3)
dll.add_first(2)
dll.add_first(1)
dll.add_last(4)
dll.add_last(5)

# display the contents of the list
dll.display()  # output: 1 2 3 4 5

# remove a node from the list
dll.remove(3)

# display the contents of the list again
dll.display()  # output: 1 2 4 5

# remove the first node from the list
dll.remove(1)

# display the contents of the list again
dll.display()  # output: 2 4 5

# remove the last node from the list
dll.remove(5)

# display the contents of the list again
dll.display()  # output: 2 4
