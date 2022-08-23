class Node:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf


class BTree():
    def __init__(self, t):
        self.root = Node(True)
        self.t = t

    def search(self, key, node=None):
        node = self.root if node == None else node
    
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
        elif node.leaf:
            return None
        else:
            return self.search(key, node.children[i])

    def split_child(self, x, i):
        t = self.t

        # y is a full child of x
        y = x.children[i]
        
        # create a new node and add it to x's list of children
        z = Node(y.leaf)
        x.children.insert(i + 1, z)

        # insert the median of the full child y into x
        x.keys.insert(i, y.keys[t - 1])

        # split apart y's keys into y & z
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]

        # if y is not a leaf, we reassign y's children to y & z
        if not y.leaf:
            z.children = y.children[t: 2 * t]
            y.children = y.children[0: t - 1]

    def insert(self, k):
        t = self.t
        root = self.root

        # if root is full, create a new node - tree's height grows by 1
        if len(root.keys) == (2 * t) - 1:
            new_root = Node()
            self.root = new_root
            new_root.children.insert(0, root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        t = self.t
        i = len(x.keys) - 1

        # find the correct spot in the leaf to insert the key
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        # if not a leaf, find the correct subtree to insert the key
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            # if child node is full, split it
            if len(x.children[i].keys) == (2 * t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)

    def print_tree(self, x, level=0):
        print(f'Level {level}', end=": ")

        for i in x.keys:
            print(i, end=" ")

        print()
        level += 1

        if len(x.children) > 0:
            for i in x.children:
                self.print_tree(i, level)


def main():
    B = BTree(3)
    
    for i in range(10):
        B.insert(i)

    B.print_tree(B.root)
    print()

    keys_to_search_for = [2, 9, 11, 4]
    for key in keys_to_search_for:
        if B.search(key) is not None:
            print(f'{key} is in the tree')
        else:
            print(f'{key} is NOT in the tree')

main()
