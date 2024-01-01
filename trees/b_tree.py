class NODE:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf


class BTREE:
    def __init__(self, t):
        self.root = NODE(True)
        # branching factor
        self.t = t

    def search(self, key, node=None):
        node = self.root if node is None else node

        it = 0
        # iterate till you find a key greater than the key:
        while it < len(node.keys) and key > node.keys[it]:
            it += 1
        # found the key:
        if it < len(node.keys) and key == node.keys[it]:
            return node, it
        # searched till the leaf node:
        if node.leaf:
            return None
        # call for the children to search:
        else:
            return self.search(key.node.children[it])

    def split_child(self, parent_node, child_index):
        t = self.t

        # we know that the i th child of the parent node is full
        child_node = parent_node.children[child_index]

        # create a new node that will now act as a sibling to the current child
        sibling = NODE(child_node.leaf)
        # need to point to this children by the parent node.
        parent_node.children.insert((child_index + 1), sibling)

        # managing the values 0-(t-1) in child and t-(2t-1) in sibling
        # also the children if the child is not leaf , the median value of t will be put in the parent
        parent_node.keys.insert(child_index, child_node.keys[t - 1])
        sibling.keys = child_node.keys[t: ((2 * t) - 1)]
        child_node.keys = child_node.keys[0:t - 1]

        if not child_node.leaf:
            sibling.children = child_node.children[t:((2 * t) - 1)]
            child_node.children = child_node.children[0:t]

    def insert_non_full(self, current_node, key):
        t = self.t
        it = len(current_node.keys) - 1

        if current_node.leaf:
            # find the index where we will put the key.
            current_node.append(None)  # this will help in shifting.
            while it >= 0 and key < current_node.keys[it]:
                current_node.keys[it + 1] = current_node.keys[it]
                it -= 1
            current_node.keys[it + 1] = key

        else:
            while it >= 0 and key < current_node.keys[it]:
                it -= 1
            it += 1
            # we need to insert the key in the it+1 child of the current node.

            if len(current_node.children[it].keys) == 2 * t - 1:
                self.split_child(current_node, it)

                # after the split the it index will have the median element from the children
                # thus we need to check if the current value is less than or greater than the key

                if current_node.keys[it] < key:
                    it += 1
            self.insert_non_full(current_node.children[it], key)

    def insert(self, key):
        t = self.t
        root = self.root

        if len(root.keys) == (2 * t) - 1:
            new_root = NODE()
            self.root = new_root
            new_root.children.insert(0, root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    def delete(self, current_node, key):
        if current_node is None:
            current_node = self.root

        t = self.t
        it = 0

        # case 1: leaf case when leaf has more than t keys.
        while it < len(current_node.keys) and key > current_node.keys[it]:
            it += 1

        if current_node.leaf:
            if it < len(current_node.keys) and current_node.keys[it] == key:
                current_node.keys.pop(it)
            return

        # case 2: if the internal node has the key , here we need to check how the children of this
        # internal node are affected by the changes caused by deletion in the node.
        if it < len(current_node.keys) and current_node.keys[it] == key:
            return self.delete_internal_node(current_node, key, it)
        # case 3: if the children has the key and that child has more than t keys.
        # then you can easily delete recursive from the child.
        elif len(current_node.children[it].keys) >= t:
            self.delete(current_node.children[it], key)

        # case4: when the key is in this child subtree but the child doesn't have more than t keys.
        # here we need to check that this child's children are disturbed and may need balancing.
        # also the case when the leaf where the key may lie has not enough keys.
        else:
            # we make the child eligible for deletion propagation by making it have enough keys.

            self.make_eligible(current_node, it)
            if it != len(current_node.keys):
                self.delete(current_node.children[it], key)
            else:
                self.delete(current_node.children[it - 1], key)

    def delete_internal_node(self, current_node, key, it):
        t = self.t

        if current_node.leaf:
            if current_node.keys[it] == key:
                current_node.keys.pop(it)
            return

        if len(current_node.children[it].keys) >= t:  # if this child has enough keys.
            current_node.keys[it] = self.delete_predecessor(current_node.children[it])
            return
        elif len(current_node.children[it + 1].keys) >= t:  # if the next child has enough keys.
            current_node.keys[it] = self.delete_successor(current_node.children[it + 1])
            return
        else:  # the case when both the children don't have enough keys.
            self.delete_merge(current_node, it, it + 1)
            # now propagate the deletion to the merged child.
            self.delete_internal_node(current_node.children[it], key, t - 1)  # t-1 is the index where the key will lie.

    def delete_predecessor(self, node):
        if node.leaf:
            return node.keys.pop()  # return the biggest key in the node.

        # now comes the propagation , if this is not a leaf then we need to
        # propagate the predecessor to now children of this node.

        # copy the last key of the leaf of this subtree and call delete for this key to propagate delete.

        current_node = node
        while not current_node.leaf:
            current_node = current_node.children[-1]
        last_key = current_node.keys[-1]
        self.delete(node.children[-1], last_key)
        return last_key

    def delete_successor(self, node):

        if node.leaf:
            return node.keys.pop(0)  # return the smallest key in the node.

        # copy the last key of the leaf of this subtree and call delete for this key to propagate delete.

        current_node = node
        while not current_node.leaf:
            current_node = current_node.children[0]
        first_key = current_node.keys[0]
        self.delete(node.children[0], first_key)
        return first_key

    def delete_merge(self, current_node, left_child_index, right_child_index):
        # merge the two children and the key at left child index of the parent node
        # to the t-1 th index and copy all the children if the children are non leaf.

        left_child = current_node.children[left_child_index]
        right_child = current_node.children[right_child_index]

        left_child.keys.append(current_node.keys[left_child_index])  # as there are less than t keys in the child
        # thus the next index must be t-1

        for k in range(len(right_child.keys)):
            left_child.keys.append(right_child.keys[k])
            if len(right_child.children) > 0:
                left_child.children.append(right_child.children[k])
        # above lines copy keys and children and the later check if child is left.
        if len(right_child.children) > 0:
            left_child.children.append(right_child.children.pop())

        # pop the node that called merges key and last child.
        current_node.keys.pop(left_child_index)
        current_node.children.pop(right_child_index)

        # if the root wanted merge then we need to acknowledge the change in the root now.
        if current_node == self.root and len(current_node.keys) == 0:
            self.root = left_child

    def make_eligible(self, current_node, it):
        # here lie three cases if we can borrow from some sibling.
        # or merge the children to have a bigger node.

        # if the left sibling can give us a borrow.
        if it != 0 and len(current_node.children[it - 1].keys) >= self.t:
            self.borrow_left(current_node, it)

        if it != len(current_node.keys) and len(current_node.children[it + 1].keys) >= self.t:
            self.borrow_right(current_node, it)

        else:
            # if we are at the last child then we need to merge it and its previous child.
            if it == len(current_node.keys):
                self.delete_merge(current_node, it - 1, it)
            # vice versa as above.
            else:
                self.delete_merge(current_node, it, it + 1)

    def borrow_left(self, current_node, it):

        receiver = current_node.children[it]
        donor = current_node.children[it + 1]

        # this is like a left rotate of keys from donor to current node to the receiver.
        receiver.keys.insert(0, current_node.keys[it - 1])
        current_node.keys[it - 1] = donor.keys[-1]
        if len(donor.children) > 0:
            receiver.children.insert(0, donor.children[-1])

        donor.keys.pop()
        donor.children.pop()

    def borrow_right(self, current_node, it):

        receiver = current_node.children[it]
        donor = current_node.children[it + 1]

        # this is like a left rotate of keys from donor to current node to the receiver.
        receiver.keys.append(current_node.keys[it])
        current_node.keys[it] = donor.keys[0]
        if len(donor.children) > 0:
            receiver.children.append(donor.children[0])

        donor.keys.pop(0)
        donor.children.pop(0)

    def print_tree(self, x, level=0):
        print(f'Level {level}', end=": ")

        for i in x.keys:
            print(i, end=" ")

        print()
        level += 1

        if len(x.children) > 0:
            for i in x.children:
                self.print_tree(i, level)


def delete_example():
    first_leaf = NODE(True)
    first_leaf.keys = [1, 9]

    second_leaf = NODE(True)
    second_leaf.keys = [17, 19, 21]

    third_leaf = NODE(True)
    third_leaf.keys = [23, 25, 27]

    fourth_leaf = NODE(True)
    fourth_leaf.keys = [31, 32, 39]

    fifth_leaf = NODE(True)
    fifth_leaf.keys = [41, 47, 50]

    sixth_leaf = NODE(True)
    sixth_leaf.keys = [56, 60]

    seventh_leaf = NODE(True)
    seventh_leaf.keys = [72, 90]

    root_left_child = NODE()
    root_left_child.keys = [15, 22, 30]
    root_left_child.children.append(first_leaf)
    root_left_child.children.append(second_leaf)
    root_left_child.children.append(third_leaf)
    root_left_child.children.append(fourth_leaf)

    root_right_child = NODE()
    root_right_child.keys = [55, 63]
    root_right_child.children.append(fifth_leaf)
    root_right_child.children.append(sixth_leaf)
    root_right_child.children.append(seventh_leaf)

    root = NODE()
    root.keys = [40]
    root.children.append(root_left_child)
    root.children.append(root_right_child)

    B = BTREE(3)
    B.root = root
    print('\n--- Original B-Tree ---\n')
    B.print_tree(B.root)

    print('\n--- Case 1: DELETED 40 ---\n')
    B.delete(B.root, 40
             )
    B.print_tree(B.root)

    print('\n--- Case 2a: DELETED 30 ---\n')
    B.delete(B.root, 30)
    B.print_tree(B.root)

    print('\n--- Case 2b: DELETED 27 ---\n')
    B.delete(B.root, 27)
    B.print_tree(B.root)

    print('\n--- Case 2c: DELETED 22 ---\n')
    B.delete(B.root, 22)
    B.print_tree(B.root)

    print('\n--- Case 3b: DELETED 17 ---\n')
    B.delete(B.root, 17)
    B.print_tree(B.root)

    print('\n--- Case 3a: DELETED 9 ---\n')
    B.delete(B.root, 9)
    B.print_tree(B.root)


def main():
    delete_example()


main()
