from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, node):
        self.data.append(node)
    
    def dequeue(self):
        self.data.popleft()

    def printQueue(self):
        print(self.data)


def main():
    queue = Queue()
    queue.printQueue()
    
    queue.enqueue(1)
    queue.printQueue()
    queue.enqueue(2)
    queue.printQueue()
    queue.enqueue(3)
    queue.printQueue()

    queue.dequeue()
    queue.printQueue()

    queue.enqueue(4)
    queue.printQueue()

    queue.dequeue()
    queue.printQueue()
    queue.dequeue()
    queue.printQueue()
    queue.dequeue()
    queue.printQueue()

main()
