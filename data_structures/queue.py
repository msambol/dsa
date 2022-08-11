from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, node):
        self.data.append(node)
    
    def dequeue(self):
        self.data.popleft()

    def print_queue(self):
        print(self.data)


def main():
    queue = Queue()
    queue.print_queue()
    
    queue.enqueue(1)
    queue.print_queue()
    queue.enqueue(2)
    queue.print_queue()
    queue.enqueue(3)
    queue.print_queue()

    queue.dequeue()
    queue.print_queue()

    queue.enqueue(4)
    queue.print_queue()

    queue.dequeue()
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()

main()
