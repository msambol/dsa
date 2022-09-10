# source: https://a.co/d/7oRsCT2

from collections import deque

BLACK = True
RED = False

class Node:
    def __init__(self, key, p=None, color=RED, left=None, right=None):
        self.key = key
        self.p = p # parent
        self.color = color
        self.left = left
        self.right = right

    def print_color(self):
        if self.color == BLACK:
            return '(b)'
        return '(r)'


class RedBlackTree:
    def __init__(self, root=None):
        self.root = root

    # O(1)
    def left_rotate(self, x):
        y = x.right
        x.right = y.left 

        if y.left is not None:
            y.left.p = x
        
        y.p = x.p 

        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y 

        y.left = x 
        x.p = y

    # O(1)
    def right_rotate(self, x):
        y = x.left 
        x.left = y.right 

        if y.right is not None:
            y.right.p = x

        y.p = x.p 

        if x.p is None:
            self.root = y 
        elif x == x.p.right:
            x.p.right = y 
        else:
            x.p.right = y 

        y.right = x 
        x.p = y

    # O(logn)
    def insert(self, z):
        y = None 
        x = self.root
        
        while x is not None:
            y = x 
            if z.key < x.key:
                x = x.left 
            else:
                x = x.right 
        
        z.p = y 
        if y == None:
            self.root = z 
        elif z.key < y.key: 
            y.left = z 
        else:
            y.right = z 
        
        z.left = None 
        z.right = None 
        z.color = RED 

        self.fix_up(z)

    # O(logn)
    def fix_up(self, z):
        while z.p and z.p.color == RED:
            if z.p == z.p.p.left:
                y = z.p.p.right 
                if y and y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK 
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p 
                        self.left_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED 
                    self.right_rotate(z.p.p)
            elif z.p == z.p.p.right:
                y = z.p.p.left 
                if y and y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK 
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p 
                        self.right_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED 
                    self.left_rotate(z.p.p)

        self.root.color = BLACK

    # simple level order tree traversal
    def print_tree(self, print_color=False):
        queue = deque()
        queue.append(self.root)

        while(queue): 
            node = queue.popleft()

            if print_color:
                print(f'{node.key}{node.print_color()}', end=' ')
            else:
                print(node.key, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def make_larger_tree():
    eight = Node(8)
    RB = RedBlackTree()
    RB.insert(eight)

    five = Node(5, eight, BLACK)
    fifteen = Node(15, eight, RED)
    eight.left = five 
    eight.right = fifteen 

    twelve = Node(12, fifteen, BLACK)
    nineteen = Node(19, fifteen, BLACK)
    fifteen.left = twelve 
    fifteen.right = nineteen

    nine = Node(9, twelve, RED)
    thirteen = Node(13, twelve, RED)
    twelve.left = nine
    twelve.right = thirteen

    twentythree = Node(23, nineteen, RED)
    nineteen.right = twentythree

    return RB


# ignoring color, just demonstrating rotation
def rotations_video():
    five = Node(5)

    two = Node(2, five)
    ten = Node(10, five)
    five.left = two 
    five.right = ten

    eight = Node(8, ten)
    twelve = Node(12, ten)
    ten.left = eight 
    ten.right = twelve

    six = Node(6, eight)
    nine = Node(9, eight)
    eight.left = six 
    eight.right = nine
    
    print('\n-- ROTATIONS VIDEO --')
    RB = RedBlackTree(five)
    RB.print_tree()

    print('\n\n-- After left rotation --')
    RB.left_rotate(five)
    RB.print_tree()

    print('\n\n-- After right rotation --')
    RB.right_rotate(ten)
    RB.print_tree()


def insertions_video():
    RB = RedBlackTree()

    print('\n\n-- INSERTIONS VIDEO, after case 0 --')
    # case 0
    fifteen = Node(15)
    RB.insert(fifteen)
    RB.print_tree(True)

    print('\n\n-- Insert 5 --')
    five = Node(5)
    RB.insert(five)
    RB.print_tree(True)

    print('\n\n-- Insert 1 (case 3) --')
    # case 3
    one = Node(1)
    RB.insert(one)
    RB.print_tree(True)

    print('\n\n-- Move to larger tree --')
    RB = make_larger_tree()
    RB.print_tree(True)

    print('\n\n-- Insert 10 (case 1, 2, and 3) --')
    # case 1
    ten = Node(10)
    RB.insert(ten)
    RB.print_tree(True)


def main():
    # https://youtu.be/95s3ndZRGbk
    rotations_video()

    # https://youtu.be/A3JZinzkMpk
    insertions_video()

main()
