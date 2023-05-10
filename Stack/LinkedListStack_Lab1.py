class Stack:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.top_node = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def clear(self):
        self.top_node = None
        self.size = 0

    def push(self, value):
        new_node = Stack.Node(value)
        if not self.top_node:
            self.top_node = new_node
        else:
            new_node.next = self.top_node
            self.top_node = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("EmptyStackException")
        else:
            value = self.top_node.value
            self.top_node = self.top_node.next
            self.size -= 1
            return value

    def top(self):
        if self.isEmpty():
            raise Exception("EmptyStackException")
        else:
            return self.top_node.value

    def traverse(self):
        current = self.top_node
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

def decimal_to_binary(decimal):
    s = Stack()
    while decimal > 0:
        remainder = decimal % 2
        s.push(remainder)
        decimal //= 2
    binary = ""
    while not s.isEmpty():
        binary += str(s.pop())
    return binary

# test the stack
s = Stack()
print(s.isEmpty())  # True
s.push(1)
s.push(2)
s.push(3)
print(len(s))  # 3
s.traverse()  # 3 2 1
print(s.pop())  # 3
print(s.pop())  # 2
print(s.top())  # 1
print(decimal_to_binary(10))  # 1010
s.clear()
print(s.isEmpty())  # True
