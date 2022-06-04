class Stack:
    def __init__(self):
        self.data = []

    def push(self, node):
        self.data.append(node)
    
    def pop(self):
        self.data.pop()

    def printStack(self):
        print(self.data)


def main():
    stack = Stack()
    stack.printStack()
    
    stack.push(1)
    stack.printStack()
    stack.push(2)
    stack.printStack()
    stack.push(3)
    stack.printStack()

    stack.pop()
    stack.printStack()

    stack.push(4)
    stack.printStack()

    stack.pop()
    stack.printStack()
    stack.pop()
    stack.printStack()
    stack.pop()
    stack.printStack()

main()
