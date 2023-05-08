class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def remove_first(self):
        if self.is_empty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data

    def remove_last(self):
        if self.is_empty():
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp.data
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            temp = current.next
            current.next = None
            return temp.data

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

# create a new linked list
my_list = SinglyLinkedList()

# add some elements to the list
my_list.add_first(3)
my_list.add_first(2)
my_list.add_first(1)
my_list.add_last(4)
my_list.add_last(5)

# display the contents of the list
my_list.display()  # output: 1 2 3 4 5

# remove an element from the beginning of the list
my_list.remove_first()

# display the contents of the list again
my_list.display()  # output: 2 3 4 5

# remove an element from the end of the list
my_list.remove_last()

# display the contents of the list once more
my_list.display()  # output: 2 3 4
