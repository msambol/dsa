class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, node):
        self.data.append(node)
    
    def dequeue(self):
        self.data.pop(0)

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
