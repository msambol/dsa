# derived from https://favtutor.com/blogs/avl-tree-python with permission

from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1 


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return 0 if not node else node.height

    def get_balance_factor(self, node):
        return 0 if not node else (self.get_height(node.left) - self.get_height(node.right))

    # O(logn)
    def search(self, key):
        x = self.root
        while x is not None and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # O(logn)
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Update the balance factor and balance the tree
        bf = self.get_balance_factor(root)

        if bf > 1 and key < root.left.key:
            return self.right_rotate(root)
        
        if bf < -1 and key > root.right.key:
            return self.left_rotate(root)
        
        if bf > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        if bf < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        
        return root

    def delete(self, key):
        pass

    # O(1)
    def left_rotate(self, node):
        B = node.right
        Y = B.left
        
        B.left = node
        node.right = Y
        
        node.height = 1 + max(self.get_height(node.left), 
                              self.get_height(node.right))
        B.height = 1 + max(self.get_height(B.left), 
                           self.get_height(B.right))
        
        return B

    # O(1)
    def right_rotate(self, node):
        A = node.left
        Y = A.right
        
        A.right = node
        node.left = Y
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        A.height = 1 + max(self.get_height(A.left), self.get_height(A.right))
        
        return A
    
    # Level-order tree traversal
    def print_tree(self):
        queue = deque()
        queue.append(self.root)

        level_order = ''
        level_order_with_details = ''

        while(queue):
            node = queue.popleft()
            level_order += f'{node.key} '
            level_order_with_details += f'{node.key}: '.ljust(5) + f'h = {self.get_height(node)}, bf = {self.get_balance_factor(node)}\n'

            # add children to queue
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        
        print('\nLevel-order traversal:')
        print(level_order)
        print(f'\nLevel-order traversal with height and balance factor:') 
        print(level_order_with_details)


def print_search_result(result):
    return result.key if result else 'not found'


def main():
    avl = AVLTree()   
    keys = [50, 25, 75, 15, 35, 60, 120, 10, 68, 90, 125, 83, 100]
    
    for key in keys:
        avl.root = avl.insert(avl.root, key)

    avl.print_tree()

    result = avl.search(125)
    print(f'Search for 125: {print_search_result(result)}')
    
    result = avl.search(1)
    print(f'Search for 1: {print_search_result(result)}')
    
    return avl

main()
