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

    # coming soon
    def insert(self, k):
        pass

    # coming soon
    def insert_non_full(self, x, k):
        pass

    # coming soon
    def split_child(self, x, i):
        pass

    # coming soon
    def print_tree(self):
        pass


def main():
    B = BTree(2)
    B.search(41)

main()
