class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self, data, priority):
        new_node = Node(data, priority)
        if self.is_empty() or priority < self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.priority <= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self):
        if self.is_empty():
            return None
        else:
            node = self.head
            self.head = self.head.next
            node.next = None
            return node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

queue = PriorityQueue()
queue.insert("job 1", 3)
queue.insert("job 2", 1)
queue.insert("job 3", 2)
print(queue.peek())  # prints "job 2"
print(queue.remove())  # prints "job 2"
print(queue.peek())  # prints "job 3"
