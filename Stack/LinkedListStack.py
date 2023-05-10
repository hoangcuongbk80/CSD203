class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        popped = temp.data
        del temp
        return popped
    
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

# Create a new stack object
stack = Stack()

# Test the is_empty method
print(stack.is_empty())  # True

# Test the push method
stack.push(1)
stack.push(2)
stack.push(3)

# Test the peek method
print(stack.peek())  # 3

# Test the display method
stack.display()  # 3 2 1

# Test the pop method
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.pop())  # None

# Test the is_empty method again
print(stack.is_empty())  # True
