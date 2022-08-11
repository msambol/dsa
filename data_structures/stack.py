class Stack:
    def __init__(self):
        self.data = []

    def push(self, node):
        self.data.append(node)
    
    def pop(self):
        self.data.pop()

    def print_stack(self):
        print(self.data)


def main():
    stack = Stack()
    stack.print_stack()
    
    stack.push(1)
    stack.print_stack()
    stack.push(2)
    stack.print_stack()
    stack.push(3)
    stack.print_stack()

    stack.pop()
    stack.print_stack()

    stack.push(4)
    stack.print_stack()

    stack.pop()
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    stack.pop()
    stack.print_stack()

main()
