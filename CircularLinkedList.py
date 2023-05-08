class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def remove(self, key):
        if self.is_empty():
            return None
        elif self.head.data == key:
            if self.head.next == self.head:
                temp = self.head
                self.head = None
                return temp.data
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                temp = self.head
                self.head = self.head.next
                current.next = self.head
                temp.next = None
                return temp.data
        else:
            current = self.head
            previous = None
            while current.next != self.head:
                if current.data == key:
                    break
                previous = current
                current = current.next
            if current.data != key:
                return None
            else:
                previous.next = current.next
                current.next = None
                return current.data

    def display(self):
        if self.is_empty():
            print("List is empty")
        else:
            current = self.head
            while True:
                print(current.data, end=' ')
                current = current.next
                if current == self.head:
                    break
            print()

# create a new circular linked list
cll = CircularLinkedList()

# add some nodes to the list
cll.add_first(3)
cll.add_first(2)
cll.add_first(1)
cll.add_last(4)
cll.add_last(5)

# display the contents of the list
cll.display()  # output: 1 2 3 4 5 

# remove a node from the list
cll.remove(3)

# display the contents of the list again
cll.display()  # output: 1 2 4 5 

# remove the first node from the list
cll.remove(1)

# display the contents of the list again
cll.display()  # output: 2 4 5 

# remove the last node from the list
cll.remove(5)

# display the contents of the list again
cll.display()  # output: 2 4 
