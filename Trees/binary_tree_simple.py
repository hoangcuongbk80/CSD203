class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def breadth(self):
        if self.root is None:
            return

        q = Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            current = q.dequeue()

            if current.left:
                q.enqueue(current.left)

            if current.right:
                q.enqueue(current.right)

            self.visit(current)

    def pre_order(self, p):
        if p is None:
            return

        self.visit(p)
        self.pre_order(p.left)
        self.pre_order(p.right)

    def in_order(self, p):
        if p is None:
            return

        self.in_order(p.left)
        self.visit(p)
        self.in_order(p.right)

    def post_order(self, p):
        if p is None:
            return

        self.post_order(p.left)
        self.post_order(p.right)
        self.visit(p)

    def visit(self, node):
        print(node.info, end=" ")

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

# Testing the code
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Breadth-First Traversal:")
tree.breadth()

print("\nPre-Order Traversal:")
tree.pre_order(tree.root)

print("\nIn-Order Traversal:")
tree.in_order(tree.root)

print("\nPost-Order Traversal:")
tree.post_order(tree.root)
