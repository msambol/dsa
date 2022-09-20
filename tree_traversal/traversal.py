from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def level_order_iterative(root):
    queue = deque()
    queue.append(root)

    while(queue): 
        node = queue.popleft()
        print(node.data, end=' ')

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def pre_order_iterative(root):
    stack = []
    stack.append(root)

    while(stack): 
        node = stack.pop()
        print(node.data, end=' ')

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def pre_order_recursive(root):
    if root:
        print(root.data, end=' ')
        pre_order_recursive(root.left)
        pre_order_recursive(root.right)


def in_order_iterative(root):
    stack = []
    node = root

    while True:
        if node:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            print(node.data, end=' ')
            node = node.right
        else: 
            break


def in_order_recursive(root):
    if root:
        in_order_recursive(root.left)
        print(root.data, end=' ')
        in_order_recursive(root.right)


def post_order_iterative(root):
    stack = []
    node = root

    while True:
        if node:
            stack.append(node)
            if node.right:
                stack.append(node.right)
            node = node.left
        elif stack:
            node = stack.pop()
            print(node.data, end=' ')
        else: 
            break


def post_order_recursive(root):
    if root:
        post_order_recursive(root.left)
        post_order_recursive(root.right)
        print(root.data, end=' ')


def print_tree():
    print(
        ''' 
                1
        2               3
    4      5        6       7  
   8 9   10 11    12 13   14 15
        '''
    )


def main():
    # height = 0
    root = Node(1)

    # height = 1
    root.left = Node(2)
    root.right = Node(3)

    # height = 2
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # height = 3
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    print_tree()

    print('--- LEVEL-ORDER iterative ---')
    level_order_iterative(root)

    print('\n\n--- PRE-ORDER iterative ---')
    pre_order_iterative(root)

    print('\n\n--- PRE-ORDER recursive ---')
    pre_order_recursive(root)

    print('\n\n--- IN-ORDER iterative ---')
    in_order_iterative(root)

    print('\n\n--- IN-ORDER recursive ---')
    in_order_recursive(root)

    print('\n\n--- POST-ORDER recursive ---')
    post_order_recursive(root)


main()
